from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WlocRequest(_message.Message):
    __slots__ = ("cellular_request1", "wifi_request", "cellular_request2", "info_mask", "channel", "unknown_varint31", "unknown_varint32", "client_info")
    CELLULAR_REQUEST1_FIELD_NUMBER: _ClassVar[int]
    WIFI_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_REQUEST2_FIELD_NUMBER: _ClassVar[int]
    INFO_MASK_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT31_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT32_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    cellular_request1: _containers.RepeatedCompositeFieldContainer[WlocCellularRequest]
    wifi_request: _containers.RepeatedCompositeFieldContainer[WlocWifiRequest]
    cellular_request2: _containers.RepeatedCompositeFieldContainer[WlocCellularRequest]
    info_mask: int
    channel: int
    unknown_varint31: int
    unknown_varint32: int
    client_info: WlocClientInfo
    def __init__(self, cellular_request1: _Optional[_Iterable[_Union[WlocCellularRequest, _Mapping]]] = ..., wifi_request: _Optional[_Iterable[_Union[WlocWifiRequest, _Mapping]]] = ..., cellular_request2: _Optional[_Iterable[_Union[WlocCellularRequest, _Mapping]]] = ..., info_mask: _Optional[int] = ..., channel: _Optional[int] = ..., unknown_varint31: _Optional[int] = ..., unknown_varint32: _Optional[int] = ..., client_info: _Optional[_Union[WlocClientInfo, _Mapping]] = ...) -> None: ...

class WlocWifiRequest(_message.Message):
    __slots__ = ("bssid",)
    BSSID_FIELD_NUMBER: _ClassVar[int]
    bssid: str
    def __init__(self, bssid: _Optional[str] = ...) -> None: ...

class WlocCellularRequest(_message.Message):
    __slots__ = ("mcc", "mnc", "cell_id", "lac")
    MCC_FIELD_NUMBER: _ClassVar[int]
    MNC_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    LAC_FIELD_NUMBER: _ClassVar[int]
    mcc: int
    mnc: int
    cell_id: int
    lac: int
    def __init__(self, mcc: _Optional[int] = ..., mnc: _Optional[int] = ..., cell_id: _Optional[int] = ..., lac: _Optional[int] = ...) -> None: ...

class WlocClientInfo(_message.Message):
    __slots__ = ("os_version", "device_model")
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    os_version: str
    device_model: str
    def __init__(self, os_version: _Optional[str] = ..., device_model: _Optional[str] = ...) -> None: ...

class StrangeWlocRequest(_message.Message):
    __slots__ = ("latitude", "longitude", "info_mask", "channel", "unknown_varint31", "unknown_varint32", "unknown_varint33", "unknown_varint34")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    INFO_MASK_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT31_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT32_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT33_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT34_FIELD_NUMBER: _ClassVar[int]
    latitude: int
    longitude: int
    info_mask: int
    channel: int
    unknown_varint31: int
    unknown_varint32: int
    unknown_varint33: int
    unknown_varint34: int
    def __init__(self, latitude: _Optional[int] = ..., longitude: _Optional[int] = ..., info_mask: _Optional[int] = ..., channel: _Optional[int] = ..., unknown_varint31: _Optional[int] = ..., unknown_varint32: _Optional[int] = ..., unknown_varint33: _Optional[int] = ..., unknown_varint34: _Optional[int] = ...) -> None: ...
