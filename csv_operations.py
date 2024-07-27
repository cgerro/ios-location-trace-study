import google.protobuf.message
import mitmproxy.http
from utils import *
from mitmproxy import io
from mitmproxy.exceptions import FlowReadException
import datetime


def get_csv_filepath(base_path, endpoint):
    csv_requests_responses_file = {
        Endpoint.APLOC: os.path.join(base_path, 'aploc.csv'),
        Endpoint.PBCWLOC: os.path.join(base_path, 'pbcwloc.csv'),
        Endpoint.WLOC: os.path.join(base_path, 'wloc.csv'),
        Endpoint.GSP57_REVGEO: os.path.join(base_path, 'gsp57_revgeo.csv'),
        Endpoint.GSP36_REVGEO: os.path.join(base_path, 'gsp36_revgeo.csv'),
        Endpoint.GSP57_LOCUS: os.path.join(base_path, 'gsp57_locus.csv'),
        Endpoint.GSP_DISPATCHER: os.path.join(base_path, 'gsp_dispatcher.csv')
    }
    return csv_requests_responses_file.get(endpoint)


def extract_request_response_hex(csv_filepath):
    with open(csv_filepath, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Extraire la requête après le '*'
            request_hex = row['request'].split('*')[-1].strip()

            # Extraire la réponse après le '*'
            response_hex = row['response'].split('*')[-1].strip()
    return request_hex, response_hex


def parse_protobuf_from_csv(csv_filepath, endpoint, fallback_class=None):
    """Parse the CSV file and decode the raw hex request/response protobuf to Request/Response class
    Return an array of dict for requests and responses."""
    print("[INFO] parsing protobuf(s) from csv file ...")
    unique_id = 1

    array_request = []
    array_response = []

    request_class, response_class = get_protobuf_classes(endpoint)
    print("[DEBUG] request class is ", request_class)
    print("[DEBUG] response class is ", response_class)

    with open(csv_filepath, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            date_time = row['date']
            date, time = date_time.split(' ')
            request_hex = row['request'].split('*')[-1].strip()
            response_hex = row['response'].split('*')[-1].strip()

            if request_hex != "":
                msg_request = deserialize_protobuf(request_hex, request_class, fallback_class)
                request_dict = {
                    'id': unique_id,
                    'date': date,
                    'time': time,
                    'type': 'request',
                    'request': msg_request
                }
                array_request.append(request_dict)
                print("[DEBUG] request_dict is \n", request_dict)

            if response_class is not None and request_hex != "":
                msg_response = deserialize_protobuf(response_hex, response_class)

                response_dict = {
                    'id': unique_id,
                    'date': date,
                    'time': time,
                    'type': 'response',
                    'response': msg_response if msg_response is not None else response_hex
                }
                array_response.append(response_dict)
                # print("[DEBUG] response_dict is \n", response_dict)
            unique_id += 1

    return array_request, array_response


def extract_data_from_protobuf(endpoint, array_request, array_response=None):
    """Extraire les informations pertinentes d'un message protobuf en fonction de l'endpoint et du type de réseau."""
    print(f"[INFO] extract data from protobuf for {endpoint}")
    # rows = []
    rows_wifi = []
    rows_cell = []

    if endpoint == Endpoint.PBCWLOC:
        # if network == NetworkType.WIFI:
        for entry in array_request:
            msg_request = entry['request']
            if hasattr(msg_request, 'wifi_request') and msg_request.wifi_request:
                # if msg_request.wifi_request:
                for bssids_list in msg_request.wifi_request:
                    rows_wifi.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'bssid': normalize_bssid(bssids_list.bssid),
                        'channel': bssids_list.channel,
                        'signal_strength': bssids_list.signal_strength,
                        'latitude': normalize_coordinates(bssids_list.location_info.latitude),
                        'longitude': normalize_coordinates(bssids_list.location_info.longitude),
                        'horizontal_accuracy': bssids_list.location_info.horizontal_accuracy,
                        'altitude': bssids_list.location_info.altitude,
                        'vertical_accuracy': bssids_list.location_info.vertical_accuracy,
                        'unknown_float7': bssids_list.location_info.unknown_float7,
                        'unknown_float8': bssids_list.location_info.unknown_float8,
                        'timestamp_loc': convert_core_data_timestamp(bssids_list.location_info.timestamp),
                        'unknown_varint7': bssids_list.unknown_varint7,
                        'timestamp': convert_core_data_timestamp(bssids_list.timestamp),
                        'unknown_varint9': bssids_list.unknown_varint9
                    })

            if hasattr(msg_request, 'cellular_request') and msg_request.cellular_request:
                for cellular_request in msg_request.cellular_request:
                    rows_cell.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'mcc': cellular_request.mcc,
                        'mnc': cellular_request.mnc,
                        'lac': cellular_request.lac,
                        'CellID': cellular_request.cell_id,
                        'EARFCN_DL': cellular_request.EARFCN_DL,
                        'PCI': cellular_request.PCI,
                        'band_info': cellular_request.band_info,
                        'latitude': normalize_coordinates(cellular_request.location_info.latitude),
                        'longitude': normalize_coordinates(cellular_request.location_info.longitude),
                        'horizontal_accuracy': cellular_request.location_info.horizontal_accuracy,
                        'altitude': cellular_request.location_info.altitude,
                        'timestamp': convert_core_data_timestamp(cellular_request.location_info.timestamp),
                        'operator': cellular_request.operator,
                        'unknown_varint14': cellular_request.unknown_varint14,
                        'unknown_varint15': cellular_request.unknown_varint15
                    })
        # La réponse dans pbcwloc ne change pas selon le type de réseau
        for entry in array_response:
            msg_response = entry['response']
            if hasattr(msg_response, 'wifi_response'):
                rows_wifi.append({
                    'id': entry['id'],
                    'date': entry['date'],
                    'time': entry['time'],
                    'type': entry['type'],
                    'unknown_varint1': msg_response.unknown_varint1
                })

            if hasattr(msg_response, 'cellular_response'):
                rows_cell.append({
                    'id': entry['id'],
                    'date': entry['date'],
                    'time': entry['time'],
                    'type': entry['type'],
                    'unknown_varint1': msg_response.unknown_varint1
                })

    elif endpoint == Endpoint.WLOC:
        # if network == NetworkType.WIFI:
        # Collecter le(s) bssid(s) présent(s) dans la requête
        initial_bssids = set()
        # Collecter la cellule de la requête
        initial_cell = set()

        for entry in array_request:
            msg_request = entry['request']
            if hasattr(msg_request, 'wifi_request') and msg_request.wifi_request:
                for bssids_list in msg_request.wifi_request:
                    rows_wifi.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'bssid': normalize_bssid(bssids_list.bssid),
                        'infoMask': msg_request.info_mask,
                        'channel': msg_request.channel
                    })
                    initial_bssids.add(bssids_list.bssid)

            if hasattr(msg_request, 'cellular_request1') and msg_request.cellular_request1:
                for cellular_request in msg_request.cellular_request1:
                    rows_cell.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'mcc': cellular_request.mcc,
                        'mnc': cellular_request.mnc,
                        'lac': cellular_request.lac,
                        'CellID': cellular_request.cell_id
                    })
                    initial_cell.add((cellular_request.mcc, cellular_request.mnc, cellular_request.lac,
                                      cellular_request.cell_id))

            if hasattr(msg_request, 'cellular_request2') and msg_request.cellular_request2:
                for cellular_request in msg_request.cellular_request2:
                    rows_cell.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'mcc': cellular_request.mcc,
                        'mnc': cellular_request.mnc,
                        'lac': cellular_request.lac,
                        'CellID': cellular_request.cell_id
                    })
                    initial_cell.add((cellular_request.mcc, cellular_request.mnc, cellular_request.lac,
                                      cellular_request.cell_id))

        for entry in array_response:
            msg_response = entry['response']
            if hasattr(msg_response, 'wifi_response') and msg_response.wifi_response:
                for wifi_response in msg_response.wifi_response:
                    rows_wifi.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'bssid': normalize_bssid(wifi_response.bssid),
                        'initial_request': wifi_response.bssid in initial_bssids,
                        'latitude': normalize_coordinates(wifi_response.location_info.latitude),
                        'longitude': normalize_coordinates(wifi_response.location_info.longitude),
                        'horizontal_accuracy': wifi_response.location_info.horizontal_accuracy,
                        'unknown_varint4': wifi_response.location_info.unknown_varint4,
                        'altitude': normalize_value(wifi_response.location_info.altitude),
                        'vertical_accuracy': normalize_value(wifi_response.location_info.vertical_accuracy),
                        'unknown_varint11': wifi_response.location_info.unknown_varint11,
                        'unknown_varint12': wifi_response.location_info.unknown_varint12
                    })

            if hasattr(msg_response, 'cellular_response1') and msg_response.cellular_response1:
                for cellular_response in msg_response.cellular_response1:
                    rows_cell.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'mcc': cellular_response.mcc,
                        'mnc': cellular_response.mnc,
                        'lac': cellular_response.lac,
                        'CellID': cellular_response.cell_id,
                        'initial_request': (cellular_response.mcc, cellular_response.mnc, cellular_response.lac,
                                            cellular_response.cell_id) in initial_cell,
                        'latitude': normalize_coordinates(cellular_response.cell_details.latitude),
                        'longitude': normalize_coordinates(cellular_response.cell_details.longitude),
                        'horizontal_accuracy': cellular_response.cell_details.horizontal_accuracy,
                        'altitude': cellular_response.cell_details.altitude,
                        'unknown_varint11': cellular_response.cell_details.unknown_varint11,
                        'unknown_varint12': cellular_response.cell_details.unknown_varint12
                    })

            if hasattr(msg_response, 'cellular_response2') and msg_response.cellular_response2:
                for cellular_response in msg_response.cellular_response2:
                    rows_cell.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'time': entry['time'],
                        'type': entry['type'],
                        'mcc': cellular_response.mcc,
                        'mnc': cellular_response.mnc,
                        'lac': cellular_response.lac,
                        'CellID': cellular_response.cell_id,
                        'initial_request': (cellular_response.mcc, cellular_response.mnc, cellular_response.lac,
                                            cellular_response.cell_id) in initial_cell,
                        'latitude': normalize_coordinates(cellular_response.cell_details.latitude),
                        'longitude': normalize_coordinates(cellular_response.cell_details.longitude),
                        'horizontal_accuracy': cellular_response.cell_details.horizontal_accuracy,
                        'altitude': cellular_response.cell_details.altitude,
                        'unknown_varint11': cellular_response.cell_details.unknown_varint11,
                        'unknown_varint12': cellular_response.cell_details.unknown_varint12
                    })

    elif endpoint == Endpoint.APLOC:
        bssids_list = []
        location_info = []

        for entry in array_request:
            msg_request = entry['request']
            if msg_request.long_string_data:
                for long_string_data in msg_request.long_string_data:
                    for location in long_string_data.location:
                        location_info.append({
                            'id': entry['id'],
                            'date': entry['date'],
                            'type': entry['type'],
                            'time': entry['time'],
                            'latitude': normalize_coordinates(location.latitude),
                            'longitude': normalize_coordinates(location.longitude),
                            'unknown_float3': location.unknown_float3,
                            'altitude': location.altitude,
                            'unknown_float6': location.unknown_float6,
                            'timestamp_loc': convert_core_data_timestamp(location.timestamp),
                        })

                    for bssid in long_string_data.bssid_info:
                        bssids_list.append({
                            'id': entry['id'],
                            'date': entry['date'],
                            'type': entry['type'],
                            'time': entry['time'],
                            'bssid': normalize_bssid(bssid.bssid),
                            'signal_strength': bssid.signal_strength,
                            'channel': bssid.channel,
                            'unknown_double4': bssid.unknown_double4,
                            'timestamp_bssid': convert_core_data_timestamp(bssid.timestamp)
                        })

        return location_info, bssids_list

    elif endpoint == Endpoint.GSP57_LOCUS:
        bssids_list = []
        location_info = []

        for entry in array_request:
            msg_request = entry['request']
            if msg_request.substring1.substring2.substring3.location:
                for location in msg_request.substring1.substring2.substring3.location:
                    location_info.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'type': entry['type'],
                        'time': entry['time'],
                        'latitude': normalize_coordinates(location.coordinates.latitude),
                        'longitude': normalize_coordinates(location.coordinates.longitude),
                        'timestamp': convert_core_data_timestamp(location.timestamp)
                    })
            if msg_request.substring1.substring2.substring3.bssid_info:
                for bssid in msg_request.substring1.substring2.substring3.bssid_info:
                    bssids_list.append({
                        'id': entry['id'],
                        'date': entry['date'],
                        'type': entry['type'],
                        'time': entry['time'],
                        'bssid': normalize_bssid(bssid.bssid),
                        'signal_strength': bssid.signal_strength,
                        'channel': bssid.channel,
                        'timestamp_bssid': convert_core_data_timestamp(bssid.timestamp)
                    })

        # for entry in array_response:
    return rows_wifi, rows_cell


def extract_hex_stream(flow_file, endpoints, output_csv_folder):
    print(f"[INFO] extract requests and responses from file: {flow_file} for all endpoints")
    result_list = []

    with open(flow_file, "rb") as f:
        freader = io.FlowReader(f)
        try:
            for flow in freader.stream():
                if isinstance(flow, mitmproxy.http.HTTPFlow):
                    request_url = flow.request.pretty_url
                    # Filtrer pour seulement les trames venant du domaine 'apple.com'
                    if any(endpoint in request_url for endpoint in endpoints):
                        request_content_hex = flow.request.content.hex() if flow.request and flow.request.content else None
                        response_content_hex = flow.response.content.hex() if flow.response and flow.response.content else None

                        # flow.client_conn.timestamp_start correspond-il à Client conn. established: sous mitmweb ?
                        date = datetime.datetime.fromtimestamp(flow.client_conn.timestamp_start)
                        date_formatted = date.strftime("%d.%m.%Y %H:%M:%S")

                        endpoint = get_enum_from_url(request_url)

                        print(f"[DEBUG] Processing flow: {flow}")
                        print("[DEBUG] date: ", date_formatted)
                        print("[DEBUG] endpoint: ", endpoint)

                        result_list.append({
                            'endpoint': request_url,
                            'date': date_formatted,
                            'request': request_content_hex,
                            'response': response_content_hex
                        })

                        request_with_marker = None
                        response_with_marker = None

                        if request_content_hex:
                            try:
                                print(f"[DEBUG] Finding protobuf start for request: {request_content_hex[:50]}...")
                                request_with_marker = find_protobuf_start(request_content_hex, endpoint, True)
                                if request_with_marker:
                                    print(f"[DEBUG] Protobuf start found for request: {request_with_marker[:50]}...")
                                else:
                                    print(f"[DEBUG] No valid Protobuf start found for request.")
                            except Exception as e:
                                print(f"[DEBUG] Error finding protobuf start for request: {e}")

                        if response_content_hex:
                            try:
                                print(f"[DEBUG] Finding protobuf start for response: {response_content_hex[:50]}...")
                                response_with_marker = find_protobuf_start(response_content_hex, endpoint, False)
                                if response_with_marker:
                                    print(f"[DEBUG] Protobuf start found for response: {response_with_marker[:50]}...")
                                else:
                                    print(f"[DEBUG] No valid Protobuf start found for response.")
                            except Exception as e:
                                print(f"[DEBUG] Error finding protobuf start for response: {e}")

                        # Écrire dans le CSV seulement si request_with_marker et response_with_marker ne sont pas nuls
                        if request_with_marker or response_with_marker:
                            csv_filename = f"{endpoint.value}.csv"
                            csv_filepath = os.path.join(os.getcwd(), output_csv_folder, csv_filename)
                            write_to_csv(csv_filepath, {
                                'date': date_formatted,
                                'request': request_with_marker,
                                'response': response_with_marker
                            })

                            print(f"[INFO] Written to CSV: {csv_filepath}")
                        else:
                            print(
                                f"[DEBUG] Both request_with_marker and response_with_marker are None. Skipping writing to CSV.")

        except FlowReadException as e:
            print(f"Flow file corrupted: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    print(f"[INFO] Finished extracting from file: {flow_file}")
    return result_list


def filter_flows_by_domain(flow_file, domain, filtered_flow_file):
    """
    Filtre les trames du fichier flow_file pour ne conserver que celles provenant du domaine spécifié
    et enregistre les trames filtrées dans un nouveau fichier.

    Arguments:
    flow_file -- le fichier flow d'origine
    domain -- le domaine à filtrer (par exemple, "apple.com")
    filtered_flow_file -- le fichier où les trames filtrées seront enregistrées
    """
    if not os.path.exists(flow_file):
        print(f"Error: The file '{flow_file}' does not exist.")
        return

    with open(flow_file, "rb") as f:
        freader = io.FlowReader(f)
        with open(filtered_flow_file, "wb") as out_f:
            fwriter = io.FlowWriter(out_f)
            try:
                for flow in freader.stream():
                    if isinstance(flow, mitmproxy.http.HTTPFlow):
                        request_url = flow.request.pretty_url
                        if re.search(r'\b' + re.escape(domain) + r'\b', request_url):
                            fwriter.add(flow)
            except FlowReadException as e:
                print(f"Flow file corrupted: {e}")


def read_csv_to_dataframe(csv_filepath):
    """
    Lit un fichier CSV et le transforme en DataFrame.

    Args:
    csv_filepath (str): Chemin vers le fichier CSV.

    Returns:
    DataFrame: Le DataFrame contenant les données du fichier CSV.
    """
    df = pd.read_csv(csv_filepath)
    return df
