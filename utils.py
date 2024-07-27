import binascii
import os
import csv
import re
from google.protobuf import json_format
import google.protobuf.message
from google.protobuf.json_format import MessageToDict
import pandas as pd
import pytz
from datetime import datetime, timezone, timedelta
import simplekml
from fastkml import kml
from shapely.geometry import Point
import requests
from geopy.distance import geodesic
import folium
from folium.plugins import HeatMap
from enum import Enum
from proto_files import (AplocRequest, PbcwlocRequest, PbcwlocResponse, WlocRequest, WlocResponse,
                         Gsp57LocusRequest, Gsp57LocusResponse, Gsp57RevgeoRequest, Gsp57RevgeoResponse,
                         GspDispatcherRequest, GspDispatcherResponse, Gsp36RevgeoRequest, Gsp36RevgeoResponse)


FOLDERNAME_CSV_REQUESTS_RESPONSES = "csv_requests_responses"
FOLDERNAME_FLOWS = "flows"
FOLDERNAME_FLOWS_FILTERED = "flows_filtered"
FOLDERNAME_CSV_DATAFRAMES = "csv_dataframes"
FOLDERNAME_KML_WIFI = "kml_wifi"
FOLDERNAME_KML_CELL = "kml_cell"

OPENCELLID_APIKEY = "pk.55fa6bec5958ba7b577b0a175c78d322"

ENDPOINT_CHELOU = "https://gspe85-ssl.ls.apple.com/wifi_request_tile"

ENDPOINTS = [
    "https://gsp-ssl.ls.apple.com/dispatcher.arpc",
    "https://gsp10-ssl.apple.com/hcy/pbcwloc",
    "https://gsp10-ssl.ls.apple.com/hvr/aploc",
    "https://gsp57-ssl-locus.ls.apple.com/dispatcher.arpc",
    "https://gs-loc.apple.com/clls/wloc",
    "https://gsp57-ssl-revgeo.ls.apple.com/dispatcher.arpc",
    "https://gsp36-ssl.ls.apple.com/revgeo_pr.arpc"
]


class Endpoint(Enum):
    PBCWLOC = 'pbcwloc'
    APLOC = 'aploc'
    WLOC = 'wloc'
    GSP_DISPATCHER = 'gsp_dispatcher'
    GSP36_REVGEO = 'gsp36_revgeo'
    GSP57_LOCUS = 'gsp57_locus'
    GSP57_REVGEO = 'gsp57_revgeo'


class NetworkType(Enum):
    CELL = 'cell'
    WIFI = 'wifi'
    OTHER = 'other'
    HYBRID = 'hybrid'


# Mapping entre les URLs et les valeurs de l'enum
url_to_enum = {
    "https://gsp-ssl.ls.apple.com/dispatcher.arpc": Endpoint.GSP_DISPATCHER,
    # "https://gsp-ssl.ls.apple.com/directions.arpc": Endpoint.DIRECTIONS,  # Vous devez ajouter cela si l'endpoint Directions est défini dans l'enum
    "https://gsp10-ssl.apple.com/hcy/pbcwloc": Endpoint.PBCWLOC,
    "https://gsp10-ssl.ls.apple.com/hvr/aploc": Endpoint.APLOC,
    "https://gsp57-ssl-locus.ls.apple.com/dispatcher.arpc": Endpoint.GSP57_LOCUS,
    "https://gs-loc.apple.com/clls/wloc": Endpoint.WLOC,
    "https://gsp57-ssl-revgeo.ls.apple.com/dispatcher.arpc": Endpoint.GSP57_REVGEO,
    "https://gsp36-ssl.ls.apple.com/revgeo_pr.arpc": Endpoint.GSP36_REVGEO
}

# Construction du dictionnaire inverse
enum_to_url = {v: k for k, v in url_to_enum.items()}


def get_enum_from_url(url):
    return url_to_enum.get(url, None)


def get_url_from_enum(endpoint_enum):
    return enum_to_url.get(endpoint_enum, None)


def get_protobuf_classes(endpoint):
    if endpoint == Endpoint.APLOC:
        return AplocRequest.AplocRequest, None  # Pas de réponse pour APLOC
    elif endpoint == Endpoint.PBCWLOC:
        return PbcwlocRequest.PbcwlocRequest, PbcwlocResponse.PbcwlocResponse
    elif endpoint == Endpoint.WLOC:
        return WlocRequest.WlocRequest, WlocResponse.WlocResponse
    elif endpoint == Endpoint.GSP36_REVGEO:
        return Gsp36RevgeoRequest.Gsp36RevgeoRequest, Gsp36RevgeoResponse.Gsp36RevgeoResponse
    elif endpoint == Endpoint.GSP57_REVGEO:
        return Gsp57RevgeoRequest.Gsp57RevgeoRequest, Gsp57RevgeoResponse.Gsp57RevgeoResponse
    elif endpoint == Endpoint.GSP57_LOCUS:
        return Gsp57LocusRequest.Gsp57LocusRequest, Gsp57LocusResponse.Gsp57LocusResponse
    elif endpoint == Endpoint.GSP_DISPATCHER:
        return GspDispatcherRequest.GspDispatcherRequest, GspDispatcherResponse.GspDispatcherResponse
    else:
        raise ValueError("Unknown endpoint")


def write_to_csv(filepath, data):
    file_exists = os.path.isfile(filepath)
    with open(filepath, mode='a', newline='') as csv_file:
        fieldnames = ['date', 'request', 'response']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow(data)


def deserialize_protobuf(hex_data, primary_class, fallback_class=None):
    """Deserialize the hex data into a protobuf message class."""
    binary_data = binascii.unhexlify(hex_data)
    try:
        message = primary_class()
        message.ParseFromString(binary_data)
        return message
    except google.protobuf.message.DecodeError:
        if fallback_class is not None:
            try:
                message = fallback_class()
                message.ParseFromString(hex_data)
                return message
            except google.protobuf.message.DecodeError:
                raise ValueError("Both primary and fallback deserialization failed.")
        else:
            raise ValueError("Primary deserialization failed.")


def normalize_bssid(bssid):
    # Vérifier si le BSSID est None ou NaN
    if pd.isna(bssid):
        return bssid

    # Si le BSSID n'a pas de ':' et fait 12 caractères de long, on l'assume comme une chaîne hexadécimale continue
    if re.match(r'^[0-9a-fA-F]{12}$', bssid):
        bssid = ':'.join(bssid[i:i + 2] for i in range(0, 12, 2))

    # Séparer le bssid en octets
    parts = bssid.split(':')
    # S'assurer que chaque composant est sur 2 caractères
    normalized_parts = [part.zfill(2) for part in parts]
    # Joindre les octets
    normalized_bssid = ':'.join(normalized_parts)
    return normalized_bssid


def normalize_coordinates(coordinate):
    if coordinate > 180:
        return coordinate / 1e8
    return coordinate


def normalize_value(value):
    """
    Permet de normaliser l'altitude ou la précision verticale qui sont représentée en n x 10^-2
    """
    return value * 10**-2


def normalize_altitude(altitude):
    """
    Normalize the altitude value. If the altitude is -5000, it is considered unknown and left as is.
    Otherwise, it is divided by 100 to convert to the desired format.

    Args:
    altitude (int): The altitude value to be normalized.

    Returns:
    float: The normalized altitude.
    """
    if altitude == -5000:
        return altitude
    else:
        return altitude * 10**-2


def to_dataframe(array):
    print("converting requests and responses into Dataframe ...")
    return pd.DataFrame(array)


def save_dataframe_to_csv(df, filename, directory):
    """
    Sauvegarde un DataFrame dans un fichier CSV.

    :param df: DataFrame à sauvegarder.
    :param filename: Nom du fichier CSV.
    :param directory: Chemin du répertoire où sauvegarder le fichier CSV.
    """
    # Créer le dossier s'il n'existe pas
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Chemin complet du fichier CSV
    file_path = os.path.join(directory, filename)

    # Sauvegarder le DataFrame en CSV
    df.to_csv(file_path, index=False)
    print(f'dataframe saved in {file_path}')


def convert_core_data_timestamp(hex_value, local_tz_str='Europe/Paris'):
    """
    Convertit un timestamp de données Core en un format lisible avec un fuseau horaire local.

    Args:
    - hex_value (int): La valeur hexadécimale du timestamp.
    - local_tz_str (str): La chaîne de caractères représentant le fuseau horaire local (ex: 'Europe/Paris').

    Returns:
    - str: Le timestamp formaté avec le fuseau horaire local.
    """
    # Date de départ pour Core Data (1er janvier 2001 à minuit en UTC)
    coredata_start_date = datetime(2001, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

    # Ajouter le hex_value en secondes au timestamp de départ
    timestamp = coredata_start_date + timedelta(seconds=hex_value)

    # Définir le fuseau horaire local
    local_tz = pytz.timezone(local_tz_str)

    # Convertir l'objet datetime en fuseau horaire local
    timestamp_local = timestamp.astimezone(local_tz)

    # Formatage de la date
    formatted_date = timestamp_local.strftime("%d.%m.%Y %H:%M:%S")
    return formatted_date


def convert_to_cocoa_core_data_timestamp(base_time):
    # Date de départ pour Cocoa Core Data (1er janvier 2001 à minuit UTC)
    core_data_start_date = datetime(2001, 1, 1, 0, 0, 0, tzinfo=pytz.utc)
    return (base_time - core_data_start_date).total_seconds()


def bssid_to_decimal(bssid):
    """
    Convert a BSSID from string format with colons to a decimal number.

    Args:
    bssid (str): BSSID in the format 'f6:63:da:a4:e9:c1'.

    Returns:
    int: Decimal representation of the BSSID.
    """
    # Remove the colons
    bssid_hex = bssid.replace(':', '')
    # Convert from hexadecimal to decimal
    bssid_decimal = int(bssid_hex, 16)
    return bssid_decimal


def decimal_to_bssid(decimal):
    # Convert decimal to hexadecimal string and pad with zeros if necessary
    hex_str = format(decimal, '012x')
    # Insert colons every two characters
    bssid = ':'.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2))
    return bssid


def find_protobuf_start(initial_hex_data, endpoint, is_request=True):
    """
    Cherche le début du Protobuf dans une séquence hexadécimale selon le point de terminaison, le type de réseau
    et si c'est une requête ou une réponse.

    Arguments:
    initial_hex_data -- la séquence hexadécimale
    endpoint -- le point de terminaison (Endpoint Enum)
    is_request -- booléen indiquant s'il s'agit d'une requête (True) ou d'une réponse (False)

    Retourne:
    La séquence hexadécimale avec le début du Protobuf marqué par '*'.
    """

    start_patterns = {
        Endpoint.GSP57_LOCUS: {'request': '0a', 'response': '08'},
        Endpoint.GSP36_REVGEO: {'request': '0a', 'response': '08'},
        Endpoint.APLOC: {'request': '0a', 'response': ''},
        Endpoint.GSP57_REVGEO: {'request': '0a', 'response': '08'},
        Endpoint.GSP_DISPATCHER: {'request': '0a', 'response': '08'},
        Endpoint.PBCWLOC: {'request': '0a', 'response': '08'},
        Endpoint.WLOC: {
            NetworkType.WIFI: {'request': '12', 'response': '12'},
            NetworkType.CELL: {'request': 'ca', 'response': 'b2'},
            NetworkType.HYBRID: {'request': '0a', 'response': '0a'},
            NetworkType.OTHER: {'request': '08', 'response': '12'},
        }
    }

    patterns_to_try = []
    pattern = None
    index = 0
    result_hex_data = None
    request_class, response_class = get_protobuf_classes(endpoint)

    # Vérification si les classes sont définies
    # Si requête mais pas de request_class, retourne None
    if is_request and not request_class:
        print("[DEBUG] No request class available for this endpoint.")
        return None
    # Si réponse mais pas de response_class, retourne None
    if not is_request and not response_class:
        print("[DEBUG] No response class available for this endpoint.")
        return None

    # Déterminer le motif de début en fonction du point de terminaison et du type de message
    if endpoint == Endpoint.WLOC:
        # Les patterns sont différents si c'est du Wifi ou du cell pour WLOC
        patterns_to_try.append(start_patterns[endpoint][NetworkType.WIFI]['request'] if is_request else
                               start_patterns[endpoint][NetworkType.WIFI]['response'])
        patterns_to_try.append(start_patterns[endpoint][NetworkType.CELL]['request'] if is_request else
                               start_patterns[endpoint][NetworkType.CELL]['response'])
        patterns_to_try.append(start_patterns[endpoint][NetworkType.HYBRID]['request'] if is_request else
                               start_patterns[endpoint][NetworkType.HYBRID]['response'])
        patterns_to_try.append(start_patterns[endpoint][NetworkType.OTHER]['request'] if is_request else
                               start_patterns[endpoint][NetworkType.OTHER]['response'])

    else:
        pattern = start_patterns[endpoint]['request'] if is_request else start_patterns[endpoint]['response']

    print(f"[DEBUG] Patterns to try: {patterns_to_try if endpoint == Endpoint.WLOC else pattern}")
    print(f"[DEBUG] Initial hex data length: {len(initial_hex_data)}")

    while index < len(initial_hex_data):
        # Trouver le motif
        if endpoint == Endpoint.WLOC:
            for p in patterns_to_try:
                index = 0
                while index < len(initial_hex_data):
                    # Trouver le motif
                    position = initial_hex_data.find(p, index)
                    if position == -1:
                        break
                    try:
                        tmp_output = initial_hex_data[position:]
                        print(f"[DEBUG] Trying to deserialize at position {position} with pattern {p}")
                        if p == '08':
                            msg = deserialize_protobuf(tmp_output, WlocRequest.StrangeWlocRequest if is_request else response_class)
                        else:
                            msg = deserialize_protobuf(tmp_output, request_class if is_request else response_class)
                        result_hex_data = initial_hex_data[:position] + '*' + initial_hex_data[position:]
                        print(f"[DEBUG] Deserialization OK for {endpoint}")
                        return result_hex_data

                    except (google.protobuf.message.DecodeError, ValueError) as e:
                        # Si la fonction deserialize_protobuf lève une exception, continuez à chercher
                        print(f"[DEBUG] Deserialization error at position {position}: {e}")
                        index = position + len(p)
        else:
            position = initial_hex_data.find(pattern, index)
            if position == -1:
                break
            try:
                tmp_output = initial_hex_data[position:]
                print(f"[DEBUG] Trying to deserialize at position {position} with pattern {pattern}")
                msg = deserialize_protobuf(tmp_output, request_class if is_request else response_class)
                result_hex_data = initial_hex_data[:position] + '*' + initial_hex_data[position:]
                print(f"[DEBUG] Deserialization OK for {endpoint}")
                return result_hex_data

            except (google.protobuf.message.DecodeError, ValueError) as e:
                print(f"[DEBUG] Deserialization error at position {position}: {e}")
                index = position + len(pattern)


def extract_cellular_responses(msg_wloc_cell):
    """
    Extrait les réponses cellulaires d'un message protobuf.

    Args:
    msg_wloc_cell: Le message protobuf contenant les réponses cellulaires.

    Returns:
    List[dict]: Une liste de dictionnaires représentant les réponses cellulaires.
    """
    cellular_responses = []
    for response in msg_wloc_cell.cellular_response2:
        response_dict = MessageToDict(response)
        cellular_responses.append(response_dict)
    return cellular_responses


def find_common_responses(responses1, responses2):
    """
    Trouve les réponses cellulaires communes entre deux listes.

    Args:
    responses1: La première liste de réponses cellulaires.
    responses2: La deuxième liste de réponses cellulaires.

    Returns:
    List[dict]: Une liste de réponses cellulaires communes aux deux listes.
    """
    common_responses = [resp for resp in responses1 if resp in responses2]
    return common_responses


def calculate_bounding_box_area(df):
    if df.empty:
        print("Dataframe is empty")
        return 0

    latitudes = df['latitude']
    longitudes = df['longitude']

    min_lat = latitudes.min()
    max_lat = latitudes.max()
    min_lon = longitudes.min()
    max_lon = longitudes.max()

    # Calculate the distance between the corners of the bounding box
    bottom_left = (min_lat, min_lon)
    bottom_right = (min_lat, max_lon)
    top_left = (max_lat, min_lon)
    top_right = (max_lat, max_lon)

    width = geodesic(bottom_left, bottom_right).meters
    height = geodesic(bottom_left, top_left).meters

    return width, height






# FONCTIONS GÉNÉRATION FICHIERS KML
# Fonction pour mapper la force du signal à une taille d'icône
def signal_to_size(signal_strength):
    # Adapter les valeurs selon vos besoins
    if signal_strength >= -50:
        return 2.0  # Grande taille pour les signaux forts
    elif signal_strength >= -70:
        return 1.5  # Taille moyenne pour les signaux moyens
    else:
        return 1.0  # Petite taille pour les signaux faibles


def signal_to_color(signal_strength):
    """
    Cette fonction prend la force du signal et renvoie une couleur hexadécimale.
    Plus la force du signal est forte, plus la couleur est verte. Plus la force du signal est faible, plus la couleur est rouge.
    """
    if signal_strength >= -60:
        return 'ff00ff00'  # Vert
    elif signal_strength >= -70:
        return 'ff66ff00'  # Jaune-vert
    elif signal_strength >= -80:
        return 'ffccff00'  # Jaune
    elif signal_strength >= -90:
        return 'ffff6600'  # Orange
    else:
        return 'ffff0000'  # Rouge


def add_coordinates_to_kml(kml_file_path, bssid_coordinates):
    # Charger le fichier KML existant avec fastkml
    with open(kml_file_path, 'rt', encoding='utf-8') as file:
        kml_content = file.read()

    k = kml.KML()
    k.from_string(kml_content)

    # Trouver le document KML
    ns = '{http://www.opengis.net/kml/2.2}'
    document = next(k.features())

    # Créer un nouvel objet simplekml.Kml pour ajouter de nouveaux points
    new_kml = simplekml.Kml()

    # Ajouter les anciens points au nouvel objet simplekml.Kml
    for feature in document.features():
        placemark = new_kml.newpoint(
            name=feature.name,
            coords=[(feature.geometry.x, feature.geometry.y)]
        )
        placemark.description = feature.description
        if hasattr(feature, 'style') and feature.style is not None:
            placemark.style.iconstyle.color = feature.style.iconstyle.color

    # Définir le style pour les nouvelles épingles violettes
    style_violet = simplekml.Style()
    style_violet.iconstyle.color = simplekml.Color.purple

    # Ajouter les nouvelles épingles avec les coordonnées
    for bssid, latitude, longitude in bssid_coordinates:
        # Vérifier si les coordonnées ne sont pas NaN et ne sont pas -1.800000e+10
        if pd.isna(latitude) or pd.isna(longitude) or latitude == -1.800000e+10 or longitude == -1.800000e+10:
            print(f"Invalid coordinates for BSSID {bssid}: Latitude {latitude}, Longitude {longitude}")
            continue

        # Vérifier si les coordonnées sont dans une plage valide (exemple pour latitude et longitude)
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            print(f"Out of range coordinates for BSSID {bssid}: Latitude {latitude}, Longitude {longitude}")
            continue

        point = new_kml.newpoint(
            coords=[(longitude, latitude)]
        )
        point.description = bssid  # BSSID comme description
        point.style = style_violet

    # Sauvegarder le fichier KML mis à jour
    new_kml.save(kml_file_path)
    print(f"KML file updated and saved to {kml_file_path}")


def create_kml_from_df_cell(filtered_df, date, output_file, endpoint):
    print("creating kml file from cell dataframe ...")
    # Créer le dossier parent 'kml_files_cell' s'il n'existe pas déjà
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), FOLDERNAME_KML_CELL)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Chemin complet du fichier de sortie
    output_path = os.path.join(output_dir, output_file)

    # Supprimer le fichier existant s'il existe déjà
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"existing file {output_path} has been removed.")

    if filtered_df.empty:
        print(f"no data found on date {date}")
        return

    # Créer l'objet KML
    kml = simplekml.Kml()

    # Définir les styles pour les épingles
    style_initial = simplekml.Style()
    style_initial.iconstyle.color = simplekml.Color.red

    style_response = simplekml.Style()
    style_response.iconstyle.color = simplekml.Color.yellow

    style_unknown = simplekml.Style()
    style_unknown.iconstyle.color = simplekml.Color.violet

    for index, row in filtered_df.iterrows():
        # Vérifier si les coordonnées ne sont pas NaN et ne sont pas -1.800000e+10
        if (pd.isna(row['latitude']) or pd.isna(row['longitude']) or row['latitude'] == -1.800000e+10
                or row['longitude'] == -1.800000e+10):
            continue

        # Vérifier si la colonne 'altitude' est présente
        if 'altitude' in filtered_df.columns:
            coords = [(row['longitude'], row['latitude'], row['altitude'])]
        else:
            coords = [(row['longitude'], row['latitude'])]

        point = kml.newpoint(
            coords=coords
        )
        point.description = (f"MCC: {row['mcc']}, MNC: {row['mnc']}, LAC: {row['lac']}, CellID: {row['CellID']}\n")

        if row['CellID'] == -1:
            point.style = style_unknown  # Couleur bleue pour les CellID inconnus (-1)
        elif endpoint == "wloc" and 'initial_request' in row and row['initial_request']:
            point.style = style_initial  # Couleur rouge pour les BSSID initiaux
        else:
            point.style = style_response  # Couleur jaune pour les réponses

    kml.save(output_path)
    print(f"kml file saved to {output_path}")


def create_kml_from_df_wifi(filtered_df, date, output_file, endpoint):
    print("creating kml file from wifi dataframe ...")
    # Créer le dossier parent 'kml_files_wifi' s'il n'existe pas déjà
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), FOLDERNAME_KML_WIFI)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Chemin complet du fichier de sortie
    output_path = os.path.join(output_dir, output_file)

    # Supprimer le fichier existant s'il existe déjà
    if os.path.exists(output_path):
        os.remove(output_path)
        print(f"existing file {output_path} has been removed.")

    if filtered_df.empty:
        print(f"no data found on date {date}")
        return

    # Créer l'objet KML
    kml = simplekml.Kml()

    for index, row in filtered_df.iterrows():
        # Vérifier si les coordonnées ne sont pas NaN et ne sont pas -1.800000e+10
        if (pd.isna(row['latitude']) or pd.isna(row['longitude']) or row['latitude'] == -1.800000e+10
                or row['longitude'] == -1.800000e+10):
            continue

        # Vérifier si la colonne 'altitude' est présente
        if 'altitude' in filtered_df.columns:
            coords = [(row['longitude'], row['latitude'], row['altitude'])]
        else:
            coords = [(row['longitude'], row['latitude'])]

        # Utiliser un nom vide ou générique pour les points
        point_name = ""

        point = kml.newpoint(
            name=point_name,
            coords=coords
        )

        # Description du point
        if endpoint == "aploc":
            point.description = f"Timestamp: {row['timestamp_loc']}"
        elif endpoint == "wloc":
            point.description = f"BSSID: {row['bssid']}\n"

        if endpoint == "pbcwloc":
            point.style.iconstyle.color = signal_to_color(row['signal_strength'])

        # Vérifie si endpoint est wloc, si clé 'initial_request' existe
        # dans row et si valeur associée à la clé 'initial_request' vaut True
        elif endpoint == "wloc" and 'initial_request' in row and row['initial_request']:
            point.style.iconstyle.color = simplekml.Color.red  # Couleur rouge pour les BSSID initiaux

    kml.save(output_path)
    print(f"kml file saved to {output_path}")


def create_heatmap_html(data, center_location=[46.316486, 6.955419], zoom_start=15, output_file="heatmap.html"):
    """
    Crée une carte HeatMap à partir des données fournies et l'enregistre en HTML.

    Args:
    - data (list of dicts): Liste de dictionnaires contenant les données de latitude, longitude et force du signal.
    - center_location (list, optional): Coordonnées de l'emplacement central de la carte. Par défaut, [46.316486, 6.955419].
    - zoom_start (int, optional): Niveau de zoom initial de la carte. Par défaut, 15.
    - output_file (str, optional): Chemin de sortie du fichier HTML. Par défaut, "heatmap.html".
    """
    # Créer une carte folium
    m = folium.Map(location=center_location, zoom_start=zoom_start)

    heat_data = []
    for index, row in data.iterrows():
        # Vérifier si les coordonnées ne sont pas NaN et ne sont pas -1.800000e+10
        if pd.isna(row['latitude']) or pd.isna(row['longitude']) or row['latitude'] == -1.800000e+10 or row['longitude'] == -1.800000e+10:
            continue

        # Préparer les données pour la HeatMap
        heat_data.append([row["latitude"], row["longitude"], row["signal_strength"]])

        # Ajouter des marqueurs pour chaque BSSID
        # Ajouter des marqueurs pour chaque BSSID avec une petite icône sans ombre
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"BSSID: {row['bssid']}\nSignal Strength: {row['signal_strength']} dBm",
            icon=folium.DivIcon(html=f'<div style="background-color:blue; width:5px; height:5px; border-radius:50%;"></div>')
        ).add_to(m)

    # Ajouter la HeatMap à la carte
    HeatMap(heat_data).add_to(m)

    # Enregistrer la carte dans un fichier HTML
    m.save(output_file)
    print(f"Carte HeatMap enregistrée sous '{output_file}'")


# def create_kml_for_antennas(dataframe, date, output_file):
#     # Créer le dossier parent 'kml_files_wifi' s'il n'existe pas déjà
#     output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kml_files_wifi')
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     filtered_df = dataframe[(dataframe['type'] == 'request') & (dataframe['date'] == date)]
#
#     if filtered_df.empty:
#         print(f"No data found for type 'request' on date {date}")
#         return
#
#     # Créer l'objet KML
#     kml = simplekml.Kml()
#
#     for index, row in filtered_df.iterrows():
#         point = kml.newpoint(
#             name=f"Cell ID: {row['cell_id']}",
#             description=f"MCC: {row['mcc']}, MNC: {antenna['mnc']}, LAC: {antenna['lac']}",
#             coords=[(antenna['longitude'], antenna['latitude'], antenna['altitude'])]
#         )
#
#     kml.save(output_file)
#     print(f"KML file saved to {output_file}")

def get_cell_info(mcc, mnc, lac, cell_id, api_key):
    url = f'https://us1.unwiredlabs.com/v2/process.php'
    params = {
        'token': api_key,
        'radio': 'lte',
        'mcc': mcc,
        'mnc': mnc,
        'cells': [{'lac': lac, 'cid': cell_id}],
        'address': 1
    }
    response = requests.post(url, json=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

