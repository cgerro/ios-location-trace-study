from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gsp57LocusResponse(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "country_language", "country_code", "substring9", "substring10")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING9_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING10_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    country_language: str
    country_code: str
    substring9: Substring
    substring10: Substring1
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., country_language: _Optional[str] = ..., country_code: _Optional[str] = ..., substring9: _Optional[_Union[Substring, _Mapping]] = ..., substring10: _Optional[_Union[Substring1, _Mapping]] = ...) -> None: ...

class Substring(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Substring1(_message.Message):
    __slots__ = ("unknown_varint1", "substring2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring2: Substring2
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring2: _Optional[_Union[Substring2, _Mapping]] = ...) -> None: ...

class Substring2(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "substring4", "unknown_varint5", "substring7", "unknown_varint8", "substring9", "unknown_varint1607")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING7_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT8_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT1607_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    substring4: _containers.RepeatedCompositeFieldContainer[Substring3]
    unknown_varint5: int
    substring7: Substring22
    unknown_varint8: int
    substring9: Substring24
    unknown_varint1607: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., substring4: _Optional[_Iterable[_Union[Substring3, _Mapping]]] = ..., unknown_varint5: _Optional[int] = ..., substring7: _Optional[_Union[Substring22, _Mapping]] = ..., unknown_varint8: _Optional[int] = ..., substring9: _Optional[_Union[Substring24, _Mapping]] = ..., unknown_varint1607: _Optional[int] = ...) -> None: ...

class Substring3(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint4", "unknown_varint6", "substring8", "services", "unknown_varint10", "substring11", "unknown_varint12")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING8_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint4: int
    unknown_varint6: int
    substring8: Substring4
    services: _containers.RepeatedScalarFieldContainer[str]
    unknown_varint10: int
    substring11: Substring5
    unknown_varint12: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint6: _Optional[int] = ..., substring8: _Optional[_Union[Substring4, _Mapping]] = ..., services: _Optional[_Iterable[str]] = ..., unknown_varint10: _Optional[int] = ..., substring11: _Optional[_Union[Substring5, _Mapping]] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...

class Substring4(_message.Message):
    __slots__ = ("substring1", "substring14", "substring3", "substring31")
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING14_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING31_FIELD_NUMBER: _ClassVar[int]
    substring1: Substring6
    substring14: Substring14
    substring3: Substring15
    substring31: Substring17
    def __init__(self, substring1: _Optional[_Union[Substring6, _Mapping]] = ..., substring14: _Optional[_Union[Substring14, _Mapping]] = ..., substring3: _Optional[_Union[Substring15, _Mapping]] = ..., substring31: _Optional[_Union[Substring17, _Mapping]] = ...) -> None: ...

class Substring6(_message.Message):
    __slots__ = ("unknown_varint1", "tel_number1", "tel_number2", "website", "substring10", "substring11", "substring12", "unknown_varint17", "unknown_varint18", "unknown_varint19", "substring25", "category", "types", "unknown_varint28", "unknown_varint31", "types1", "substring38", "unknown_varint39")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    TEL_NUMBER1_FIELD_NUMBER: _ClassVar[int]
    TEL_NUMBER2_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING10_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING11_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING12_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT17_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT18_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT19_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING25_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT28_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT31_FIELD_NUMBER: _ClassVar[int]
    TYPES1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING38_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT39_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    tel_number1: str
    tel_number2: str
    website: str
    substring10: Substring7
    substring11: Substring7
    substring12: _containers.RepeatedCompositeFieldContainer[Substring8]
    unknown_varint17: int
    unknown_varint18: int
    unknown_varint19: int
    substring25: Substring10
    category: str
    types: str
    unknown_varint28: int
    unknown_varint31: int
    types1: str
    substring38: Substring12
    unknown_varint39: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., tel_number1: _Optional[str] = ..., tel_number2: _Optional[str] = ..., website: _Optional[str] = ..., substring10: _Optional[_Union[Substring7, _Mapping]] = ..., substring11: _Optional[_Union[Substring7, _Mapping]] = ..., substring12: _Optional[_Iterable[_Union[Substring8, _Mapping]]] = ..., unknown_varint17: _Optional[int] = ..., unknown_varint18: _Optional[int] = ..., unknown_varint19: _Optional[int] = ..., substring25: _Optional[_Union[Substring10, _Mapping]] = ..., category: _Optional[str] = ..., types: _Optional[str] = ..., unknown_varint28: _Optional[int] = ..., unknown_varint31: _Optional[int] = ..., types1: _Optional[str] = ..., substring38: _Optional[_Union[Substring12, _Mapping]] = ..., unknown_varint39: _Optional[int] = ...) -> None: ...

class Substring7(_message.Message):
    __slots__ = ("language", "city", "entity_name")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    language: str
    city: str
    entity_name: str
    def __init__(self, language: _Optional[str] = ..., city: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...

class Substring8(_message.Message):
    __slots__ = ("unknown_varint1", "substring3", "type")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring3: Substring9
    type: str
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring3: _Optional[_Union[Substring9, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...

class Substring9(_message.Message):
    __slots__ = ("language", "category")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    language: str
    category: str
    def __init__(self, language: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class Substring10(_message.Message):
    __slots__ = ("substring1",)
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    substring1: _containers.RepeatedCompositeFieldContainer[Substring11]
    def __init__(self, substring1: _Optional[_Iterable[_Union[Substring11, _Mapping]]] = ...) -> None: ...

class Substring11(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class Substring12(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint3")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint3: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ...) -> None: ...

class Substring5(_message.Message):
    __slots__ = ("unknown_varint1", "substring3")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring3: Substring13
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring3: _Optional[_Union[Substring13, _Mapping]] = ...) -> None: ...

class Substring13(_message.Message):
    __slots__ = ("unknown_double", "unknown_varint7")
    UNKNOWN_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    unknown_double: float
    unknown_varint7: int
    def __init__(self, unknown_double: _Optional[float] = ..., unknown_varint7: _Optional[int] = ...) -> None: ...

class Substring14(_message.Message):
    __slots__ = ("coordinates", "timezone", "datasource")
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_FIELD_NUMBER: _ClassVar[int]
    coordinates: Coordinates
    timezone: Timezone
    datasource: Datasource
    def __init__(self, coordinates: _Optional[_Union[Coordinates, _Mapping]] = ..., timezone: _Optional[_Union[Timezone, _Mapping]] = ..., datasource: _Optional[_Union[Datasource, _Mapping]] = ...) -> None: ...

class Coordinates(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Timezone(_message.Message):
    __slots__ = ("timezone",)
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    def __init__(self, timezone: _Optional[str] = ...) -> None: ...

class Datasource(_message.Message):
    __slots__ = ("datasource",)
    DATASOURCE_FIELD_NUMBER: _ClassVar[int]
    datasource: str
    def __init__(self, datasource: _Optional[str] = ...) -> None: ...

class Substring15(_message.Message):
    __slots__ = ("substring1",)
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    substring1: _containers.RepeatedCompositeFieldContainer[Substring16]
    def __init__(self, substring1: _Optional[_Iterable[_Union[Substring16, _Mapping]]] = ...) -> None: ...

class Substring16(_message.Message):
    __slots__ = ("coordinates", "unknown_varint3")
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    coordinates: Coordinates
    unknown_varint3: int
    def __init__(self, coordinates: _Optional[_Union[Coordinates, _Mapping]] = ..., unknown_varint3: _Optional[int] = ...) -> None: ...

class Substring17(_message.Message):
    __slots__ = ("substring1",)
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    substring1: Substring18
    def __init__(self, substring1: _Optional[_Union[Substring18, _Mapping]] = ...) -> None: ...

class Substring18(_message.Message):
    __slots__ = ("unknown_varint1", "version", "substring3", "substring4", "substring101")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING101_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    version: str
    substring3: Substring19
    substring4: Substring20
    substring101: Substring21
    def __init__(self, unknown_varint1: _Optional[int] = ..., version: _Optional[str] = ..., substring3: _Optional[_Union[Substring19, _Mapping]] = ..., substring4: _Optional[_Union[Substring20, _Mapping]] = ..., substring101: _Optional[_Union[Substring21, _Mapping]] = ...) -> None: ...

class Substring19(_message.Message):
    __slots__ = ("language", "unknown_string2", "unknown_string3")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING3_FIELD_NUMBER: _ClassVar[int]
    language: str
    unknown_string2: str
    unknown_string3: str
    def __init__(self, language: _Optional[str] = ..., unknown_string2: _Optional[str] = ..., unknown_string3: _Optional[str] = ...) -> None: ...

class Substring20(_message.Message):
    __slots__ = ("service", "unknown_varint2", "unknown_string3", "version")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING3_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    service: str
    unknown_varint2: int
    unknown_string3: str
    version: str
    def __init__(self, service: _Optional[str] = ..., unknown_varint2: _Optional[int] = ..., unknown_string3: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class Substring21(_message.Message):
    __slots__ = ("location", "unknown_string5", "unknown_string7")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING7_FIELD_NUMBER: _ClassVar[int]
    location: Location
    unknown_string5: str
    unknown_string7: str
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., unknown_string5: _Optional[str] = ..., unknown_string7: _Optional[str] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("info_location", "infoloc")
    INFO_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INFOLOC_FIELD_NUMBER: _ClassVar[int]
    info_location: _containers.RepeatedScalarFieldContainer[str]
    infoloc: InfoLocation
    def __init__(self, info_location: _Optional[_Iterable[str]] = ..., infoloc: _Optional[_Union[InfoLocation, _Mapping]] = ...) -> None: ...

class InfoLocation(_message.Message):
    __slots__ = ("country", "country_code", "state", "state_code", "city1", "city2")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY1_FIELD_NUMBER: _ClassVar[int]
    CITY2_FIELD_NUMBER: _ClassVar[int]
    country: str
    country_code: str
    state: str
    state_code: str
    city1: str
    city2: str
    def __init__(self, country: _Optional[str] = ..., country_code: _Optional[str] = ..., state: _Optional[str] = ..., state_code: _Optional[str] = ..., city1: _Optional[str] = ..., city2: _Optional[str] = ...) -> None: ...

class Substring22(_message.Message):
    __slots__ = ("substring1",)
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    substring1: Substring23
    def __init__(self, substring1: _Optional[_Union[Substring23, _Mapping]] = ...) -> None: ...

class Substring23(_message.Message):
    __slots__ = ("unknown_varint1", "coordinates", "unknown_varint3", "unknown_varint50")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT50_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    coordinates: Coordinates
    unknown_varint3: int
    unknown_varint50: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., coordinates: _Optional[_Union[Coordinates, _Mapping]] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint50: _Optional[int] = ...) -> None: ...

class Substring24(_message.Message):
    __slots__ = ("substring1",)
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    substring1: _containers.RepeatedCompositeFieldContainer[Substring25]
    def __init__(self, substring1: _Optional[_Iterable[_Union[Substring25, _Mapping]]] = ...) -> None: ...

class Substring25(_message.Message):
    __slots__ = ("unknown_varint1", "substring2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring2: Substring26
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring2: _Optional[_Union[Substring26, _Mapping]] = ...) -> None: ...

class Substring26(_message.Message):
    __slots__ = ("substring9",)
    SUBSTRING9_FIELD_NUMBER: _ClassVar[int]
    substring9: Substring27
    def __init__(self, substring9: _Optional[_Union[Substring27, _Mapping]] = ...) -> None: ...

class Substring27(_message.Message):
    __slots__ = ("substring1", "substring2")
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    substring1: _containers.RepeatedCompositeFieldContainer[Substring28]
    substring2: Substring31
    def __init__(self, substring1: _Optional[_Iterable[_Union[Substring28, _Mapping]]] = ..., substring2: _Optional[_Union[Substring31, _Mapping]] = ...) -> None: ...

class Substring28(_message.Message):
    __slots__ = ("unknown_varint1", "substring3")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring3: Substring29
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring3: _Optional[_Union[Substring29, _Mapping]] = ...) -> None: ...

class Substring29(_message.Message):
    __slots__ = ("unknown_varint1", "substring3")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring3: _containers.RepeatedCompositeFieldContainer[Substring30]
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring3: _Optional[_Iterable[_Union[Substring30, _Mapping]]] = ...) -> None: ...

class Substring30(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Substring31(_message.Message):
    __slots__ = ("substring1",)
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    substring1: _containers.RepeatedCompositeFieldContainer[Substring32]
    def __init__(self, substring1: _Optional[_Iterable[_Union[Substring32, _Mapping]]] = ...) -> None: ...

class Substring32(_message.Message):
    __slots__ = ("service", "unknown_varint3", "substring4")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    service: str
    unknown_varint3: int
    substring4: _containers.RepeatedCompositeFieldContainer[Substring33]
    def __init__(self, service: _Optional[str] = ..., unknown_varint3: _Optional[int] = ..., substring4: _Optional[_Iterable[_Union[Substring33, _Mapping]]] = ...) -> None: ...

class Substring33(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...
