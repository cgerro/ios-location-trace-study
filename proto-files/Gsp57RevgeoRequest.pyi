from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gsp57RevgeoRequest(_message.Message):
    __slots__ = ("service_data", "country_data", "country_code", "subdata", "unknown_varint7", "substring1", "country")
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBDATA_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    service_data: Gsp57RevgeoServiceData
    country_data: Gsp57RevgeoCountryData
    country_code: str
    subdata: _containers.RepeatedCompositeFieldContainer[Gsp57RevgeoSubdata]
    unknown_varint7: int
    substring1: Gsp57RevgeoSubstring1
    country: str
    def __init__(self, service_data: _Optional[_Union[Gsp57RevgeoServiceData, _Mapping]] = ..., country_data: _Optional[_Union[Gsp57RevgeoCountryData, _Mapping]] = ..., country_code: _Optional[str] = ..., subdata: _Optional[_Iterable[_Union[Gsp57RevgeoSubdata, _Mapping]]] = ..., unknown_varint7: _Optional[int] = ..., substring1: _Optional[_Union[Gsp57RevgeoSubstring1, _Mapping]] = ..., country: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubdata(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint3", "subdata6")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBDATA6_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint3: int
    subdata6: Gsp57RevgeoSubdata6
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., subdata6: _Optional[_Union[Gsp57RevgeoSubdata6, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoServiceData(_message.Message):
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
    subdata1: Gsp57RevgeoSubdata1
    unknown_varint9: int
    unknown_varint12: int
    subdata2: Gsp57RevgeoSubdata2
    os: str
    unknown_double18: float
    def __init__(self, service: _Optional[str] = ..., version: _Optional[str] = ..., unknown_string3: _Optional[str] = ..., model: _Optional[str] = ..., ios_version: _Optional[str] = ..., unknown_varint7: _Optional[int] = ..., subdata1: _Optional[_Union[Gsp57RevgeoSubdata1, _Mapping]] = ..., unknown_varint9: _Optional[int] = ..., unknown_varint12: _Optional[int] = ..., subdata2: _Optional[_Union[Gsp57RevgeoSubdata2, _Mapping]] = ..., os: _Optional[str] = ..., unknown_double18: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoCountryData(_message.Message):
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
    subdata3: Gsp57RevgeoSubdata3
    unknown_varint26: int
    unknown_string28: str
    country: str
    unknown_varint31: int
    subdata4: Gsp57RevgeoSubdata4
    def __init__(self, language: _Optional[str] = ..., country_code: _Optional[str] = ..., unknown_string9: _Optional[str] = ..., unknown_varint10: _Optional[int] = ..., unknown_varint11: _Optional[int] = ..., unknown_varint12: _Optional[int] = ..., unknown_varint16: _Optional[int] = ..., unknown_varint19: _Optional[int] = ..., subdata3: _Optional[_Union[Gsp57RevgeoSubdata3, _Mapping]] = ..., unknown_varint26: _Optional[int] = ..., unknown_string28: _Optional[str] = ..., country: _Optional[str] = ..., unknown_varint31: _Optional[int] = ..., subdata4: _Optional[_Union[Gsp57RevgeoSubdata4, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubdata1(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata2(_message.Message):
    __slots__ = ("unknown_varint1", "uuid")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    uuid: str
    def __init__(self, unknown_varint1: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubdata3(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: _containers.RepeatedScalarFieldContainer[int]
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[_Iterable[int]] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata4(_message.Message):
    __slots__ = ("subdata5",)
    SUBDATA5_FIELD_NUMBER: _ClassVar[int]
    subdata5: Gsp57RevgeoSubdata5
    def __init__(self, subdata5: _Optional[_Union[Gsp57RevgeoSubdata5, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubdata5(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata6(_message.Message):
    __slots__ = ("subdata16", "subdata15", "subdata8", "subdata8_1", "subdata9", "unknown_string30", "subdata7", "subdata12", "subdata14", "unknown_string42", "unknown_string44", "unknown_string55", "subdata11", "unknown_string59", "subdata13", "subdata10_1", "unknown_string71", "subdata18")
    SUBDATA16_FIELD_NUMBER: _ClassVar[int]
    SUBDATA15_FIELD_NUMBER: _ClassVar[int]
    SUBDATA8_FIELD_NUMBER: _ClassVar[int]
    SUBDATA8_1_FIELD_NUMBER: _ClassVar[int]
    SUBDATA9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING30_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_FIELD_NUMBER: _ClassVar[int]
    SUBDATA12_FIELD_NUMBER: _ClassVar[int]
    SUBDATA14_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING42_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING44_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING55_FIELD_NUMBER: _ClassVar[int]
    SUBDATA11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING59_FIELD_NUMBER: _ClassVar[int]
    SUBDATA13_FIELD_NUMBER: _ClassVar[int]
    SUBDATA10_1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING71_FIELD_NUMBER: _ClassVar[int]
    SUBDATA18_FIELD_NUMBER: _ClassVar[int]
    subdata16: Gsp57RevgeoSubdata16
    subdata15: Gsp57RevgeoSubdata15
    subdata8: Gsp57RevgeoSubdata8
    subdata8_1: Gsp57RevgeoSubdata8
    subdata9: Gsp57RevgeoSubdata9
    unknown_string30: str
    subdata7: Gsp57RevgeoSubdata7
    subdata12: Gsp57RevgeoSubdata12
    subdata14: Gsp57RevgeoSubdata14
    unknown_string42: str
    unknown_string44: str
    unknown_string55: str
    subdata11: Gsp57RevgeoSubdata11
    unknown_string59: str
    subdata13: Gsp57RevgeoSubdata13
    subdata10_1: Gsp57RevgeoSubdata10
    unknown_string71: str
    subdata18: Gsp57RevgeoSubdata18
    def __init__(self, subdata16: _Optional[_Union[Gsp57RevgeoSubdata16, _Mapping]] = ..., subdata15: _Optional[_Union[Gsp57RevgeoSubdata15, _Mapping]] = ..., subdata8: _Optional[_Union[Gsp57RevgeoSubdata8, _Mapping]] = ..., subdata8_1: _Optional[_Union[Gsp57RevgeoSubdata8, _Mapping]] = ..., subdata9: _Optional[_Union[Gsp57RevgeoSubdata9, _Mapping]] = ..., unknown_string30: _Optional[str] = ..., subdata7: _Optional[_Union[Gsp57RevgeoSubdata7, _Mapping]] = ..., subdata12: _Optional[_Union[Gsp57RevgeoSubdata12, _Mapping]] = ..., subdata14: _Optional[_Union[Gsp57RevgeoSubdata14, _Mapping]] = ..., unknown_string42: _Optional[str] = ..., unknown_string44: _Optional[str] = ..., unknown_string55: _Optional[str] = ..., subdata11: _Optional[_Union[Gsp57RevgeoSubdata11, _Mapping]] = ..., unknown_string59: _Optional[str] = ..., subdata13: _Optional[_Union[Gsp57RevgeoSubdata13, _Mapping]] = ..., subdata10_1: _Optional[_Union[Gsp57RevgeoSubdata10, _Mapping]] = ..., unknown_string71: _Optional[str] = ..., subdata18: _Optional[_Union[Gsp57RevgeoSubdata18, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubdata8(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata7(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubdata9(_message.Message):
    __slots__ = ("subdata10",)
    SUBDATA10_FIELD_NUMBER: _ClassVar[int]
    subdata10: _containers.RepeatedCompositeFieldContainer[Gsp57RevgeoSubdata10]
    def __init__(self, subdata10: _Optional[_Iterable[_Union[Gsp57RevgeoSubdata10, _Mapping]]] = ...) -> None: ...

class Gsp57RevgeoSubdata10(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata11(_message.Message):
    __slots__ = ("subdata10",)
    SUBDATA10_FIELD_NUMBER: _ClassVar[int]
    subdata10: _containers.RepeatedCompositeFieldContainer[Gsp57RevgeoSubdata10]
    def __init__(self, subdata10: _Optional[_Iterable[_Union[Gsp57RevgeoSubdata10, _Mapping]]] = ...) -> None: ...

class Gsp57RevgeoSubdata12(_message.Message):
    __slots__ = ("subdata10",)
    SUBDATA10_FIELD_NUMBER: _ClassVar[int]
    subdata10: Gsp57RevgeoSubdata10
    def __init__(self, subdata10: _Optional[_Union[Gsp57RevgeoSubdata10, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubdata13(_message.Message):
    __slots__ = ("unknown_varint2", "unknown_varint4")
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    unknown_varint2: int
    unknown_varint4: int
    def __init__(self, unknown_varint2: _Optional[int] = ..., unknown_varint4: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata14(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata15(_message.Message):
    __slots__ = ("subdata16", "subdata16_1", "subdata17", "unknown_varint8")
    SUBDATA16_FIELD_NUMBER: _ClassVar[int]
    SUBDATA16_1_FIELD_NUMBER: _ClassVar[int]
    SUBDATA17_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT8_FIELD_NUMBER: _ClassVar[int]
    subdata16: Gsp57RevgeoSubdata16
    subdata16_1: Gsp57RevgeoSubdata16
    subdata17: Gsp57RevgeoSubdata17
    unknown_varint8: int
    def __init__(self, subdata16: _Optional[_Union[Gsp57RevgeoSubdata16, _Mapping]] = ..., subdata16_1: _Optional[_Union[Gsp57RevgeoSubdata16, _Mapping]] = ..., subdata17: _Optional[_Union[Gsp57RevgeoSubdata17, _Mapping]] = ..., unknown_varint8: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata16(_message.Message):
    __slots__ = ("subdata17", "unknown_varint2", "unknown_varint8")
    SUBDATA17_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT8_FIELD_NUMBER: _ClassVar[int]
    subdata17: Gsp57RevgeoSubdata17
    unknown_varint2: int
    unknown_varint8: int
    def __init__(self, subdata17: _Optional[_Union[Gsp57RevgeoSubdata17, _Mapping]] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint8: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata17(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubdata18(_message.Message):
    __slots__ = ("unknown_varint3", "unknown_varint4")
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    unknown_varint3: int
    unknown_varint4: int
    def __init__(self, unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring1(_message.Message):
    __slots__ = ("substring2",)
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    substring2: Gsp57RevgeoSubstring2
    def __init__(self, substring2: _Optional[_Union[Gsp57RevgeoSubstring2, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring2(_message.Message):
    __slots__ = ("unknown_varint3", "substring3")
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint3: int
    substring3: Gsp57RevgeoSubstring3
    def __init__(self, unknown_varint3: _Optional[int] = ..., substring3: _Optional[_Union[Gsp57RevgeoSubstring3, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring3(_message.Message):
    __slots__ = ("substring4", "unknown_double3", "unknown_double5")
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE5_FIELD_NUMBER: _ClassVar[int]
    substring4: Gsp57RevgeoSubstring4
    unknown_double3: float
    unknown_double5: float
    def __init__(self, substring4: _Optional[_Union[Gsp57RevgeoSubstring4, _Mapping]] = ..., unknown_double3: _Optional[float] = ..., unknown_double5: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoSubstring4(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...
