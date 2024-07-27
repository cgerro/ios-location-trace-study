from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GspDispatcherRequest(_message.Message):
    __slots__ = ("service_data", "country_data", "country_code", "subdata", "unknown_varint7", "substring1", "country")
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBDATA_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    service_data: GspDispatcherServiceData
    country_data: GspDispatcherCountryData
    country_code: str
    subdata: _containers.RepeatedCompositeFieldContainer[GspDispatcherSubdata]
    unknown_varint7: int
    substring1: GspDispatcherSubstring1
    country: str
    def __init__(self, service_data: _Optional[_Union[GspDispatcherServiceData, _Mapping]] = ..., country_data: _Optional[_Union[GspDispatcherCountryData, _Mapping]] = ..., country_code: _Optional[str] = ..., subdata: _Optional[_Iterable[_Union[GspDispatcherSubdata, _Mapping]]] = ..., unknown_varint7: _Optional[int] = ..., substring1: _Optional[_Union[GspDispatcherSubstring1, _Mapping]] = ..., country: _Optional[str] = ...) -> None: ...

class GspDispatcherSubdata(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint3", "subdata6")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBDATA6_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint3: int
    subdata6: GspDispatcherSubdata6
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., subdata6: _Optional[_Union[GspDispatcherSubdata6, _Mapping]] = ...) -> None: ...

class GspDispatcherSubdata6(_message.Message):
    __slots__ = ("subdata8_4", "subdata8_5", "subdata7_1", "subdata7_4", "subdata8_1", "unknown_string30", "subdata10", "subdata8_3", "subdata7_3", "unknown_string42", "unknown_string55", "subdata8_2", "unknown_string59", "subdata7_2", "subdata7_6", "unknown_string71", "subdata7_5", "unknown_string44")
    SUBDATA8_4_FIELD_NUMBER: _ClassVar[int]
    SUBDATA8_5_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_1_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_4_FIELD_NUMBER: _ClassVar[int]
    SUBDATA8_1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING30_FIELD_NUMBER: _ClassVar[int]
    SUBDATA10_FIELD_NUMBER: _ClassVar[int]
    SUBDATA8_3_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING42_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING55_FIELD_NUMBER: _ClassVar[int]
    SUBDATA8_2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING59_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_2_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_6_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING71_FIELD_NUMBER: _ClassVar[int]
    SUBDATA7_5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING44_FIELD_NUMBER: _ClassVar[int]
    subdata8_4: GspDispatcherSubdata8
    subdata8_5: GspDispatcherSubdata8
    subdata7_1: GspDispatcherSubdata7
    subdata7_4: GspDispatcherSubdata7
    subdata8_1: GspDispatcherSubdata8
    unknown_string30: str
    subdata10: GspDispatcherSubdata10
    subdata8_3: GspDispatcherSubdata8
    subdata7_3: GspDispatcherSubdata7
    unknown_string42: str
    unknown_string55: str
    subdata8_2: GspDispatcherSubdata8
    unknown_string59: str
    subdata7_2: GspDispatcherSubdata7
    subdata7_6: GspDispatcherSubdata7
    unknown_string71: str
    subdata7_5: GspDispatcherSubdata7
    unknown_string44: str
    def __init__(self, subdata8_4: _Optional[_Union[GspDispatcherSubdata8, _Mapping]] = ..., subdata8_5: _Optional[_Union[GspDispatcherSubdata8, _Mapping]] = ..., subdata7_1: _Optional[_Union[GspDispatcherSubdata7, _Mapping]] = ..., subdata7_4: _Optional[_Union[GspDispatcherSubdata7, _Mapping]] = ..., subdata8_1: _Optional[_Union[GspDispatcherSubdata8, _Mapping]] = ..., unknown_string30: _Optional[str] = ..., subdata10: _Optional[_Union[GspDispatcherSubdata10, _Mapping]] = ..., subdata8_3: _Optional[_Union[GspDispatcherSubdata8, _Mapping]] = ..., subdata7_3: _Optional[_Union[GspDispatcherSubdata7, _Mapping]] = ..., unknown_string42: _Optional[str] = ..., unknown_string55: _Optional[str] = ..., subdata8_2: _Optional[_Union[GspDispatcherSubdata8, _Mapping]] = ..., unknown_string59: _Optional[str] = ..., subdata7_2: _Optional[_Union[GspDispatcherSubdata7, _Mapping]] = ..., subdata7_6: _Optional[_Union[GspDispatcherSubdata7, _Mapping]] = ..., unknown_string71: _Optional[str] = ..., subdata7_5: _Optional[_Union[GspDispatcherSubdata7, _Mapping]] = ..., unknown_string44: _Optional[str] = ...) -> None: ...

class GspDispatcherSubdata7(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint3", "unknown_varint4")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint3: int
    unknown_varint4: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata8(_message.Message):
    __slots__ = ("subdata12", "unknown_varint2", "subdata13_1", "subdata13_2", "subdata13_3", "unknown_varint8")
    SUBDATA12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    SUBDATA13_1_FIELD_NUMBER: _ClassVar[int]
    SUBDATA13_2_FIELD_NUMBER: _ClassVar[int]
    SUBDATA13_3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT8_FIELD_NUMBER: _ClassVar[int]
    subdata12: _containers.RepeatedCompositeFieldContainer[GspDispatcherSubdata12]
    unknown_varint2: int
    subdata13_1: GspDispatcherSubdata13
    subdata13_2: GspDispatcherSubdata13
    subdata13_3: GspDispatcherSubdata13
    unknown_varint8: int
    def __init__(self, subdata12: _Optional[_Iterable[_Union[GspDispatcherSubdata12, _Mapping]]] = ..., unknown_varint2: _Optional[int] = ..., subdata13_1: _Optional[_Union[GspDispatcherSubdata13, _Mapping]] = ..., subdata13_2: _Optional[_Union[GspDispatcherSubdata13, _Mapping]] = ..., subdata13_3: _Optional[_Union[GspDispatcherSubdata13, _Mapping]] = ..., unknown_varint8: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata10(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class GspDispatcherSubdata11(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata12(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata13(_message.Message):
    __slots__ = ("subdata14", "unknown_varint2")
    SUBDATA14_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    subdata14: GspDispatcherSubdata14
    unknown_varint2: int
    def __init__(self, subdata14: _Optional[_Union[GspDispatcherSubdata14, _Mapping]] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata14(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherServiceData(_message.Message):
    __slots__ = ("service", "version", "unknown_string3", "model", "ios_version", "unknown_varint7", "subdata1", "unknown_varint9", "unknown_varint12", "subdata2", "os", "subdata17", "unknown_double18")
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
    SUBDATA17_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE18_FIELD_NUMBER: _ClassVar[int]
    service: str
    version: str
    unknown_string3: str
    model: str
    ios_version: str
    unknown_varint7: int
    subdata1: GspDispatcherSubdata1
    unknown_varint9: int
    unknown_varint12: int
    subdata2: GspDispatcherSubdata2
    os: str
    subdata17: GspDispatcherSubdata15
    unknown_double18: float
    def __init__(self, service: _Optional[str] = ..., version: _Optional[str] = ..., unknown_string3: _Optional[str] = ..., model: _Optional[str] = ..., ios_version: _Optional[str] = ..., unknown_varint7: _Optional[int] = ..., subdata1: _Optional[_Union[GspDispatcherSubdata1, _Mapping]] = ..., unknown_varint9: _Optional[int] = ..., unknown_varint12: _Optional[int] = ..., subdata2: _Optional[_Union[GspDispatcherSubdata2, _Mapping]] = ..., os: _Optional[str] = ..., subdata17: _Optional[_Union[GspDispatcherSubdata15, _Mapping]] = ..., unknown_double18: _Optional[float] = ...) -> None: ...

class GspDispatcherSubdata1(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata2(_message.Message):
    __slots__ = ("unknown_varint1", "uuid")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    uuid: str
    def __init__(self, unknown_varint1: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...

class GspDispatcherCountryData(_message.Message):
    __slots__ = ("language", "country_language", "unknown_string9", "unknown_varint10", "unknown_varint11", "unknown_varint12", "unknown_varint16", "unknown_varint19", "subdata3", "unknown_varint26", "unknown_string28", "country_code", "unknown_varint31", "subdata4")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT16_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT19_FIELD_NUMBER: _ClassVar[int]
    SUBDATA3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT26_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING28_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT31_FIELD_NUMBER: _ClassVar[int]
    SUBDATA4_FIELD_NUMBER: _ClassVar[int]
    language: str
    country_language: str
    unknown_string9: str
    unknown_varint10: int
    unknown_varint11: int
    unknown_varint12: int
    unknown_varint16: int
    unknown_varint19: int
    subdata3: GspDispatcherSubdata3
    unknown_varint26: int
    unknown_string28: str
    country_code: str
    unknown_varint31: int
    subdata4: GspDispatcherSubdata4
    def __init__(self, language: _Optional[str] = ..., country_language: _Optional[str] = ..., unknown_string9: _Optional[str] = ..., unknown_varint10: _Optional[int] = ..., unknown_varint11: _Optional[int] = ..., unknown_varint12: _Optional[int] = ..., unknown_varint16: _Optional[int] = ..., unknown_varint19: _Optional[int] = ..., subdata3: _Optional[_Union[GspDispatcherSubdata3, _Mapping]] = ..., unknown_varint26: _Optional[int] = ..., unknown_string28: _Optional[str] = ..., country_code: _Optional[str] = ..., unknown_varint31: _Optional[int] = ..., subdata4: _Optional[_Union[GspDispatcherSubdata4, _Mapping]] = ...) -> None: ...

class GspDispatcherSubdata3(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: _containers.RepeatedScalarFieldContainer[int]
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[_Iterable[int]] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherSubdata4(_message.Message):
    __slots__ = ("subdata5",)
    SUBDATA5_FIELD_NUMBER: _ClassVar[int]
    subdata5: GspDispatcherSubdata5
    def __init__(self, subdata5: _Optional[_Union[GspDispatcherSubdata5, _Mapping]] = ...) -> None: ...

class GspDispatcherSubdata5(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring1(_message.Message):
    __slots__ = ("substring2",)
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    substring2: GspDispatcherSubstring2
    def __init__(self, substring2: _Optional[_Union[GspDispatcherSubstring2, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring2(_message.Message):
    __slots__ = ("unknown_varint2", "address")
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    unknown_varint2: int
    address: GspDispatcherAddress
    def __init__(self, unknown_varint2: _Optional[int] = ..., address: _Optional[_Union[GspDispatcherAddress, _Mapping]] = ...) -> None: ...

class GspDispatcherAddress(_message.Message):
    __slots__ = ("country", "language", "city", "postal_code", "street_number")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    country: str
    language: str
    city: str
    postal_code: str
    street_number: str
    def __init__(self, country: _Optional[str] = ..., language: _Optional[str] = ..., city: _Optional[str] = ..., postal_code: _Optional[str] = ..., street_number: _Optional[str] = ...) -> None: ...

class GspDispatcherSubdata15(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_float2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_float2: float
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_float2: _Optional[float] = ...) -> None: ...
