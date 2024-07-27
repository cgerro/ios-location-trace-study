from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WlocResponse(_message.Message):
    __slots__ = ("cellular_response1", "wifi_response", "cellular_response2")
    CELLULAR_RESPONSE1_FIELD_NUMBER: _ClassVar[int]
    WIFI_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_RESPONSE2_FIELD_NUMBER: _ClassVar[int]
    cellular_response1: _containers.RepeatedCompositeFieldContainer[WlocCellularResponse]
    wifi_response: _containers.RepeatedCompositeFieldContainer[WlocWifiResponse]
    cellular_response2: _containers.RepeatedCompositeFieldContainer[WlocCellularResponse]
    def __init__(self, cellular_response1: _Optional[_Iterable[_Union[WlocCellularResponse, _Mapping]]] = ..., wifi_response: _Optional[_Iterable[_Union[WlocWifiResponse, _Mapping]]] = ..., cellular_response2: _Optional[_Iterable[_Union[WlocCellularResponse, _Mapping]]] = ...) -> None: ...

class WlocWifiResponse(_message.Message):
    __slots__ = ("bssid", "location_info", "unknown_varint21", "unknown_varint22")
    BSSID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT21_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT22_FIELD_NUMBER: _ClassVar[int]
    bssid: str
    location_info: WlocLocation
    unknown_varint21: int
    unknown_varint22: int
    def __init__(self, bssid: _Optional[str] = ..., location_info: _Optional[_Union[WlocLocation, _Mapping]] = ..., unknown_varint21: _Optional[int] = ..., unknown_varint22: _Optional[int] = ...) -> None: ...

class WlocLocation(_message.Message):
    __slots__ = ("latitude", "longitude", "horizontal_accuracy", "unknown_varint4", "altitude", "vertical_accuracy", "unknown_varint11", "unknown_varint12")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    latitude: int
    longitude: int
    horizontal_accuracy: int
    unknown_varint4: int
    altitude: int
    vertical_accuracy: int
    unknown_varint11: int
    unknown_varint12: int
    def __init__(self, latitude: _Optional[int] = ..., longitude: _Optional[int] = ..., horizontal_accuracy: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., altitude: _Optional[int] = ..., vertical_accuracy: _Optional[int] = ..., unknown_varint11: _Optional[int] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...

class WlocCellularResponse(_message.Message):
    __slots__ = ("mcc", "mnc", "cell_id", "lac", "cell_details", "unknown_varint6", "unknown_varint7")
    MCC_FIELD_NUMBER: _ClassVar[int]
    MNC_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    LAC_FIELD_NUMBER: _ClassVar[int]
    CELL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    mcc: int
    mnc: int
    cell_id: int
    lac: int
    cell_details: WlocCellDetails
    unknown_varint6: int
    unknown_varint7: int
    def __init__(self, mcc: _Optional[int] = ..., mnc: _Optional[int] = ..., cell_id: _Optional[int] = ..., lac: _Optional[int] = ..., cell_details: _Optional[_Union[WlocCellDetails, _Mapping]] = ..., unknown_varint6: _Optional[int] = ..., unknown_varint7: _Optional[int] = ...) -> None: ...

class WlocCellDetails(_message.Message):
    __slots__ = ("latitude", "longitude", "horizontal_accuracy", "altitude", "unknown_varint11", "unknown_varint12")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    latitude: int
    longitude: int
    horizontal_accuracy: int
    altitude: int
    unknown_varint11: int
    unknown_varint12: int
    def __init__(self, latitude: _Optional[int] = ..., longitude: _Optional[int] = ..., horizontal_accuracy: _Optional[int] = ..., altitude: _Optional[int] = ..., unknown_varint11: _Optional[int] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...
