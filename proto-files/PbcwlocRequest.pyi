from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PbcwlocRequest(_message.Message):
    __slots__ = ("device_info", "wifi_request", "cellular_request")
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    WIFI_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_REQUEST_FIELD_NUMBER: _ClassVar[int]
    device_info: PbcwlocDeviceInfo
    wifi_request: _containers.RepeatedCompositeFieldContainer[PbcwlocWifiRequest]
    cellular_request: _containers.RepeatedCompositeFieldContainer[PbcwlocCellularRequest]
    def __init__(self, device_info: _Optional[_Union[PbcwlocDeviceInfo, _Mapping]] = ..., wifi_request: _Optional[_Iterable[_Union[PbcwlocWifiRequest, _Mapping]]] = ..., cellular_request: _Optional[_Iterable[_Union[PbcwlocCellularRequest, _Mapping]]] = ...) -> None: ...

class PbcwlocDeviceInfo(_message.Message):
    __slots__ = ("hardware_version", "os_version")
    HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    hardware_version: str
    os_version: str
    def __init__(self, hardware_version: _Optional[str] = ..., os_version: _Optional[str] = ...) -> None: ...

class PbcwlocWifiRequest(_message.Message):
    __slots__ = ("bssid", "channel", "signal_strength", "location_info", "unknown_varint7", "timestamp", "unknown_varint9")
    BSSID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT9_FIELD_NUMBER: _ClassVar[int]
    bssid: str
    channel: int
    signal_strength: int
    location_info: PbcwlocLocationInfo
    unknown_varint7: int
    timestamp: float
    unknown_varint9: int
    def __init__(self, bssid: _Optional[str] = ..., channel: _Optional[int] = ..., signal_strength: _Optional[int] = ..., location_info: _Optional[_Union[PbcwlocLocationInfo, _Mapping]] = ..., unknown_varint7: _Optional[int] = ..., timestamp: _Optional[float] = ..., unknown_varint9: _Optional[int] = ...) -> None: ...

class PbcwlocCellularRequest(_message.Message):
    __slots__ = ("mcc", "mnc", "lac", "cell_id", "EARFCN_DL", "PCI", "band_info", "location_info", "operator", "unknown_double11", "unknown_double12", "unknown_varint14", "unknown_varint15", "unknown_varint16", "string", "unknown_varint22", "unknown_varint23", "operator_bis", "unknown_varint25", "unknown_varint31", "unknown_varint32", "unknown_varint34", "unknown_varint35")
    MCC_FIELD_NUMBER: _ClassVar[int]
    MNC_FIELD_NUMBER: _ClassVar[int]
    LAC_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    EARFCN_DL_FIELD_NUMBER: _ClassVar[int]
    PCI_FIELD_NUMBER: _ClassVar[int]
    BAND_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT14_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT15_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT16_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT22_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT23_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_BIS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT25_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT31_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT34_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT35_FIELD_NUMBER: _ClassVar[int]
    mcc: int
    mnc: int
    lac: int
    cell_id: int
    EARFCN_DL: int
    PCI: int
    band_info: int
    location_info: PbcwlocLocationInfo
    operator: str
    unknown_double11: float
    unknown_double12: float
    unknown_varint14: int
    unknown_varint15: int
    unknown_varint16: int
    string: PbcwlocString
    unknown_varint22: int
    unknown_varint23: int
    operator_bis: str
    unknown_varint25: int
    unknown_varint31: int
    unknown_varint32: int
    unknown_varint34: int
    unknown_varint35: int
    def __init__(self, mcc: _Optional[int] = ..., mnc: _Optional[int] = ..., lac: _Optional[int] = ..., cell_id: _Optional[int] = ..., EARFCN_DL: _Optional[int] = ..., PCI: _Optional[int] = ..., band_info: _Optional[int] = ..., location_info: _Optional[_Union[PbcwlocLocationInfo, _Mapping]] = ..., operator: _Optional[str] = ..., unknown_double11: _Optional[float] = ..., unknown_double12: _Optional[float] = ..., unknown_varint14: _Optional[int] = ..., unknown_varint15: _Optional[int] = ..., unknown_varint16: _Optional[int] = ..., string: _Optional[_Union[PbcwlocString, _Mapping]] = ..., unknown_varint22: _Optional[int] = ..., unknown_varint23: _Optional[int] = ..., operator_bis: _Optional[str] = ..., unknown_varint25: _Optional[int] = ..., unknown_varint31: _Optional[int] = ..., unknown_varint32: _Optional[int] = ..., unknown_varint34: _Optional[int] = ..., unknown_varint35: _Optional[int] = ...) -> None: ...

class PbcwlocLocationInfo(_message.Message):
    __slots__ = ("latitude", "longitude", "horizontal_accuracy", "altitude", "vertical_accuracy", "unknown_float7", "unknown_float8", "timestamp", "unknown_varint13", "unknown_varint16", "unknown_varint17", "inner_data18", "inner_data19", "inner_data20", "unknown_float21", "unknown_float22")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT7_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT8_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT13_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT16_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT17_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA18_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA19_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA20_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT21_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT22_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    horizontal_accuracy: float
    altitude: float
    vertical_accuracy: float
    unknown_float7: float
    unknown_float8: float
    timestamp: float
    unknown_varint13: int
    unknown_varint16: int
    unknown_varint17: int
    inner_data18: PbcwlocInnerData
    inner_data19: PbcwlocInnerData
    inner_data20: PbcwlocInnerData
    unknown_float21: float
    unknown_float22: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., horizontal_accuracy: _Optional[float] = ..., altitude: _Optional[float] = ..., vertical_accuracy: _Optional[float] = ..., unknown_float7: _Optional[float] = ..., unknown_float8: _Optional[float] = ..., timestamp: _Optional[float] = ..., unknown_varint13: _Optional[int] = ..., unknown_varint16: _Optional[int] = ..., unknown_varint17: _Optional[int] = ..., inner_data18: _Optional[_Union[PbcwlocInnerData, _Mapping]] = ..., inner_data19: _Optional[_Union[PbcwlocInnerData, _Mapping]] = ..., inner_data20: _Optional[_Union[PbcwlocInnerData, _Mapping]] = ..., unknown_float21: _Optional[float] = ..., unknown_float22: _Optional[float] = ...) -> None: ...

class PbcwlocInnerData(_message.Message):
    __slots__ = ("inner_varint1", "inner_varint2")
    INNER_VARINT1_FIELD_NUMBER: _ClassVar[int]
    INNER_VARINT2_FIELD_NUMBER: _ClassVar[int]
    inner_varint1: int
    inner_varint2: int
    def __init__(self, inner_varint1: _Optional[int] = ..., inner_varint2: _Optional[int] = ...) -> None: ...

class PbcwlocString(_message.Message):
    __slots__ = ("substring",)
    SUBSTRING_FIELD_NUMBER: _ClassVar[int]
    substring: _containers.RepeatedCompositeFieldContainer[PbcwlocSubstring]
    def __init__(self, substring: _Optional[_Iterable[_Union[PbcwlocSubstring, _Mapping]]] = ...) -> None: ...

class PbcwlocSubstring(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint3", "unknown_varint4", "unknown_varint5", "unknown_varint6")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint3: int
    unknown_varint4: int
    unknown_varint5: int
    unknown_varint6: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., unknown_varint6: _Optional[int] = ...) -> None: ...
