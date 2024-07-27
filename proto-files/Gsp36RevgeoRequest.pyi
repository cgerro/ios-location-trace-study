from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gsp36RevgeoRequest(_message.Message):
    __slots__ = ("service_data", "country_data", "country_code", "subdata", "unknown_varint7", "substring1", "country")
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBDATA_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    service_data: Gsp36RevgeoServiceData
    country_data: Gsp36RevgeoCountryData
    country_code: str
    subdata: _containers.RepeatedCompositeFieldContainer[Gsp36RevgeoSubdata]
    unknown_varint7: int
    substring1: Gsp36RevgeoSubstring1
    country: str
    def __init__(self, service_data: _Optional[_Union[Gsp36RevgeoServiceData, _Mapping]] = ..., country_data: _Optional[_Union[Gsp36RevgeoCountryData, _Mapping]] = ..., country_code: _Optional[str] = ..., subdata: _Optional[_Iterable[_Union[Gsp36RevgeoSubdata, _Mapping]]] = ..., unknown_varint7: _Optional[int] = ..., substring1: _Optional[_Union[Gsp36RevgeoSubstring1, _Mapping]] = ..., country: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoSubdata(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint3", "subdata6")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBDATA6_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint3: int
    subdata6: Gsp36RevgeoSubdata6
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., subdata6: _Optional[_Union[Gsp36RevgeoSubdata6, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoServiceData(_message.Message):
    __slots__ = ("service", "version", "unknown_string3", "model", "ios_version", "unknown_varint7", "subdata1", "unknown_varint9", "unknown_varint12", "subdata2", "os", "unknown_double18")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING3_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    IOS_VERSION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    SUBDATA1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    SUBDATA2_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE18_FIELD_NUMBER: _ClassVar[int]
    service: str
    version: str
    unknown_string3: str
    model: str
    ios_version: str
    unknown_varint7: int
    subdata1: Gsp36RevgeoSubdata1
    unknown_varint9: int
    unknown_varint12: int
    subdata2: Gsp36RevgeoSubdata2
    os: Gsp36RevgeoOs
    unknown_double18: float
    def __init__(self, service: _Optional[str] = ..., version: _Optional[str] = ..., unknown_string3: _Optional[str] = ..., model: _Optional[str] = ..., ios_version: _Optional[str] = ..., unknown_varint7: _Optional[int] = ..., subdata1: _Optional[_Union[Gsp36RevgeoSubdata1, _Mapping]] = ..., unknown_varint9: _Optional[int] = ..., unknown_varint12: _Optional[int] = ..., subdata2: _Optional[_Union[Gsp36RevgeoSubdata2, _Mapping]] = ..., os: _Optional[_Union[Gsp36RevgeoOs, _Mapping]] = ..., unknown_double18: _Optional[float] = ...) -> None: ...

class Gsp36RevgeoCountryData(_message.Message):
    __slots__ = ("language", "country_code", "unknown_string9", "unknown_varint10", "unknown_varint11", "unknown_varint12", "unknown_varint16", "unknown_varint19", "subdata3", "unknown_varint26", "unknown_string28", "country", "unknown_varint31", "subdata4")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT16_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT19_FIELD_NUMBER: _ClassVar[int]
    SUBDATA3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT26_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING28_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT31_FIELD_NUMBER: _ClassVar[int]
    SUBDATA4_FIELD_NUMBER: _ClassVar[int]
    language: str
    country_code: str
    unknown_string9: str
    unknown_varint10: int
    unknown_varint11: int
    unknown_varint12: int
    unknown_varint16: int
    unknown_varint19: int
    subdata3: Gsp36RevgeoSubdata3
    unknown_varint26: int
    unknown_string28: str
    country: str
    unknown_varint31: int
    subdata4: Gsp36RevgeoSubdata4
    def __init__(self, language: _Optional[str] = ..., country_code: _Optional[str] = ..., unknown_string9: _Optional[str] = ..., unknown_varint10: _Optional[int] = ..., unknown_varint11: _Optional[int] = ..., unknown_varint12: _Optional[int] = ..., unknown_varint16: _Optional[int] = ..., unknown_varint19: _Optional[int] = ..., subdata3: _Optional[_Union[Gsp36RevgeoSubdata3, _Mapping]] = ..., unknown_varint26: _Optional[int] = ..., unknown_string28: _Optional[str] = ..., country: _Optional[str] = ..., unknown_varint31: _Optional[int] = ..., subdata4: _Optional[_Union[Gsp36RevgeoSubdata4, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoOs(_message.Message):
    __slots__ = ("unknown_double13",)
    UNKNOWN_DOUBLE13_FIELD_NUMBER: _ClassVar[int]
    unknown_double13: float
    def __init__(self, unknown_double13: _Optional[float] = ...) -> None: ...

class Gsp36RevgeoSubdata1(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubdata2(_message.Message):
    __slots__ = ("unknown_varint1", "uuid")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    uuid: str
    def __init__(self, unknown_varint1: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoSubdata3(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: _containers.RepeatedScalarFieldContainer[int]
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[_Iterable[int]] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubdata4(_message.Message):
    __slots__ = ("subdata5",)
    SUBDATA5_FIELD_NUMBER: _ClassVar[int]
    subdata5: Gsp36RevgeoSubdata5
    def __init__(self, subdata5: _Optional[_Union[Gsp36RevgeoSubdata5, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubdata5(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubdata6(_message.Message):
    __slots__ = ("subdata7",)
    SUBDATA7_FIELD_NUMBER: _ClassVar[int]
    subdata7: Gsp36RevgeoSubdata7
    def __init__(self, subdata7: _Optional[_Union[Gsp36RevgeoSubdata7, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubdata7(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoSubstring1(_message.Message):
    __slots__ = ("substring2",)
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    substring2: Gsp36RevgeoSubstring2
    def __init__(self, substring2: _Optional[_Union[Gsp36RevgeoSubstring2, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubstring2(_message.Message):
    __slots__ = ("substring3", "unknown_varint2")
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    substring3: _containers.RepeatedCompositeFieldContainer[Gsp36RevgeoSubstring3]
    unknown_varint2: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, substring3: _Optional[_Iterable[_Union[Gsp36RevgeoSubstring3, _Mapping]]] = ..., unknown_varint2: _Optional[_Iterable[int]] = ...) -> None: ...

class Gsp36RevgeoSubstring3(_message.Message):
    __slots__ = ("substring4", "unknown_double5")
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE5_FIELD_NUMBER: _ClassVar[int]
    substring4: Gsp36RevgeoSubstring4
    unknown_double5: float
    def __init__(self, substring4: _Optional[_Union[Gsp36RevgeoSubstring4, _Mapping]] = ..., unknown_double5: _Optional[float] = ...) -> None: ...

class Gsp36RevgeoBssidInfo(_message.Message):
    __slots__ = ("bssid", "signal_strength", "channel", "timestamp", "unknown_varint5")
    BSSID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    bssid: str
    signal_strength: int
    channel: int
    timestamp: int
    unknown_varint5: int
    def __init__(self, bssid: _Optional[str] = ..., signal_strength: _Optional[int] = ..., channel: _Optional[int] = ..., timestamp: _Optional[int] = ..., unknown_varint5: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubstring4(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...
