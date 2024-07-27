from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AplocRequest(_message.Message):
    __slots__ = ("device_info", "long_string_data")
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    LONG_STRING_DATA_FIELD_NUMBER: _ClassVar[int]
    device_info: AplocDeviceInfo
    long_string_data: _containers.RepeatedCompositeFieldContainer[AplocLongStringData]
    def __init__(self, device_info: _Optional[_Union[AplocDeviceInfo, _Mapping]] = ..., long_string_data: _Optional[_Iterable[_Union[AplocLongStringData, _Mapping]]] = ...) -> None: ...

class AplocDeviceInfo(_message.Message):
    __slots__ = ("device_model", "os_version")
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    device_model: str
    os_version: str
    def __init__(self, device_model: _Optional[str] = ..., os_version: _Optional[str] = ...) -> None: ...

class AplocLongStringData(_message.Message):
    __slots__ = ("sub_data1", "location", "bssid_info")
    SUB_DATA1_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    BSSID_INFO_FIELD_NUMBER: _ClassVar[int]
    sub_data1: AplocSubData1
    location: _containers.RepeatedCompositeFieldContainer[AplocLocation]
    bssid_info: _containers.RepeatedCompositeFieldContainer[AplocBssidInfo]
    def __init__(self, sub_data1: _Optional[_Union[AplocSubData1, _Mapping]] = ..., location: _Optional[_Iterable[_Union[AplocLocation, _Mapping]]] = ..., bssid_info: _Optional[_Iterable[_Union[AplocBssidInfo, _Mapping]]] = ...) -> None: ...

class AplocSubData1(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint3", "timestamp", "unknown_varint5")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint3: int
    timestamp: float
    unknown_varint5: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., timestamp: _Optional[float] = ..., unknown_varint5: _Optional[int] = ...) -> None: ...

class AplocLocation(_message.Message):
    __slots__ = ("latitude", "longitude", "unknown_float3", "altitude", "unknown_float6", "timestamp", "unknown_varint13", "inner_data18", "inner_data19", "inner_data20")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT3_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT6_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT13_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA18_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA19_FIELD_NUMBER: _ClassVar[int]
    INNER_DATA20_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    unknown_float3: float
    altitude: float
    unknown_float6: float
    timestamp: float
    unknown_varint13: int
    inner_data18: AplocInnerData
    inner_data19: AplocInnerData
    inner_data20: AplocInnerData
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., unknown_float3: _Optional[float] = ..., altitude: _Optional[float] = ..., unknown_float6: _Optional[float] = ..., timestamp: _Optional[float] = ..., unknown_varint13: _Optional[int] = ..., inner_data18: _Optional[_Union[AplocInnerData, _Mapping]] = ..., inner_data19: _Optional[_Union[AplocInnerData, _Mapping]] = ..., inner_data20: _Optional[_Union[AplocInnerData, _Mapping]] = ...) -> None: ...

class AplocInnerData(_message.Message):
    __slots__ = ("inner_varint1", "inner_varint2")
    INNER_VARINT1_FIELD_NUMBER: _ClassVar[int]
    INNER_VARINT2_FIELD_NUMBER: _ClassVar[int]
    inner_varint1: int
    inner_varint2: int
    def __init__(self, inner_varint1: _Optional[int] = ..., inner_varint2: _Optional[int] = ...) -> None: ...

class AplocBssidInfo(_message.Message):
    __slots__ = ("bssid", "signal_strength", "channel", "unknown_double4", "timestamp")
    BSSID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE4_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    bssid: str
    signal_strength: int
    channel: int
    unknown_double4: float
    timestamp: float
    def __init__(self, bssid: _Optional[str] = ..., signal_strength: _Optional[int] = ..., channel: _Optional[int] = ..., unknown_double4: _Optional[float] = ..., timestamp: _Optional[float] = ...) -> None: ...
