from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gsp36RevgeoResponse(_message.Message):
    __slots__ = ("field1", "field2", "country_language", "country_code", "field10")
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    FIELD10_FIELD_NUMBER: _ClassVar[int]
    field1: int
    field2: int
    country_language: str
    country_code: str
    field10: Gsp36RevgeoString3
    def __init__(self, field1: _Optional[int] = ..., field2: _Optional[int] = ..., country_language: _Optional[str] = ..., country_code: _Optional[str] = ..., field10: _Optional[_Union[Gsp36RevgeoString3, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoString3(_message.Message):
    __slots__ = ("unknown_varint1", "substring10")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING10_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring10: Gsp36RevgeoSubstring_10
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring10: _Optional[_Union[Gsp36RevgeoSubstring_10, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubstring_10(_message.Message):
    __slots__ = ("substring11", "substring12")
    SUBSTRING11_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING12_FIELD_NUMBER: _ClassVar[int]
    substring11: Gsp36RevgeoSubstring_11
    substring12: _containers.RepeatedCompositeFieldContainer[Gsp36RevgeoSubstring_12]
    def __init__(self, substring11: _Optional[_Union[Gsp36RevgeoSubstring_11, _Mapping]] = ..., substring12: _Optional[_Iterable[_Union[Gsp36RevgeoSubstring_12, _Mapping]]] = ...) -> None: ...

class Gsp36RevgeoSubstring_11(_message.Message):
    __slots__ = ("unknown_varint2", "string", "unknown_varint5", "field7")
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    FIELD7_FIELD_NUMBER: _ClassVar[int]
    unknown_varint2: int
    string: _containers.RepeatedCompositeFieldContainer[Gsp36RevgeoString]
    unknown_varint5: int
    field7: Gsp36RevgeoString1
    def __init__(self, unknown_varint2: _Optional[int] = ..., string: _Optional[_Iterable[_Union[Gsp36RevgeoString, _Mapping]]] = ..., unknown_varint5: _Optional[int] = ..., field7: _Optional[_Union[Gsp36RevgeoString1, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubstring_12(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: _containers.RepeatedCompositeFieldContainer[Gsp36RevgeoString]
    def __init__(self, string: _Optional[_Iterable[_Union[Gsp36RevgeoString, _Mapping]]] = ...) -> None: ...

class Gsp36RevgeoString1(_message.Message):
    __slots__ = ("substring6",)
    SUBSTRING6_FIELD_NUMBER: _ClassVar[int]
    substring6: Gsp36RevgeoSubstring6
    def __init__(self, substring6: _Optional[_Union[Gsp36RevgeoSubstring6, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoString2(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: _containers.RepeatedCompositeFieldContainer[Gsp36RevgeoString]
    def __init__(self, string: _Optional[_Iterable[_Union[Gsp36RevgeoString, _Mapping]]] = ...) -> None: ...

class Gsp36RevgeoSubstring6(_message.Message):
    __slots__ = ("location", "unknown_varint3", "unknown_varint4", "unknown_varint50")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT50_FIELD_NUMBER: _ClassVar[int]
    location: Gsp36RevgeoLocation
    unknown_varint3: int
    unknown_varint4: int
    unknown_varint50: int
    def __init__(self, location: _Optional[_Union[Gsp36RevgeoLocation, _Mapping]] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint50: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoString(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint4", "unknown_varint5", "unknown_varint6", "substring", "apple_service", "unknown_varint10", "unknown_varint12")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING_FIELD_NUMBER: _ClassVar[int]
    APPLE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint4: int
    unknown_varint5: int
    unknown_varint6: int
    substring: Gsp36RevgeoSubstring
    apple_service: _containers.RepeatedScalarFieldContainer[str]
    unknown_varint10: int
    unknown_varint12: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., unknown_varint6: _Optional[int] = ..., substring: _Optional[_Union[Gsp36RevgeoSubstring, _Mapping]] = ..., apple_service: _Optional[_Iterable[str]] = ..., unknown_varint10: _Optional[int] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubstring(_message.Message):
    __slots__ = ("substring7", "substring1", "substring9", "substring2", "substring4")
    SUBSTRING7_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING9_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING2_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    substring7: Gsp36RevgeoSubstring7
    substring1: Gsp36RevgeoSubstring1
    substring9: Gsp36RevgeoSubstring9
    substring2: Gsp36RevgeoSubstring2
    substring4: Gsp36RevgeoSubstring4
    def __init__(self, substring7: _Optional[_Union[Gsp36RevgeoSubstring7, _Mapping]] = ..., substring1: _Optional[_Union[Gsp36RevgeoSubstring1, _Mapping]] = ..., substring9: _Optional[_Union[Gsp36RevgeoSubstring9, _Mapping]] = ..., substring2: _Optional[_Union[Gsp36RevgeoSubstring2, _Mapping]] = ..., substring4: _Optional[_Union[Gsp36RevgeoSubstring4, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubstring9(_message.Message):
    __slots__ = ("locations",)
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    locations: Gsp36RevgeoLocations
    def __init__(self, locations: _Optional[_Union[Gsp36RevgeoLocations, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoLocations(_message.Message):
    __slots__ = ("latitude1", "longitude1", "latitude2", "longitude2", "unknown_varint10")
    LATITUDE1_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE1_FIELD_NUMBER: _ClassVar[int]
    LATITUDE2_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    latitude1: float
    longitude1: float
    latitude2: float
    longitude2: float
    unknown_varint10: int
    def __init__(self, latitude1: _Optional[float] = ..., longitude1: _Optional[float] = ..., latitude2: _Optional[float] = ..., longitude2: _Optional[float] = ..., unknown_varint10: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubstring7(_message.Message):
    __slots__ = ("unknown_varint1", "substring8", "unknown_varint19")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING8_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT19_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substring8: Gsp36RevgeoSubstring8
    unknown_varint19: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., substring8: _Optional[_Union[Gsp36RevgeoSubstring8, _Mapping]] = ..., unknown_varint19: _Optional[int] = ...) -> None: ...

class Gsp36RevgeoSubstring8(_message.Message):
    __slots__ = ("country_language", "city")
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    country_language: str
    city: str
    def __init__(self, country_language: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoSubstring1(_message.Message):
    __slots__ = ("location", "unknown_double2", "time_zone", "unknown_varint6", "data_source")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE2_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    location: Gsp36RevgeoLocation
    unknown_double2: float
    time_zone: Gsp36RevgeoTimeZone
    unknown_varint6: int
    data_source: Gsp36RevgeoDataSource
    def __init__(self, location: _Optional[_Union[Gsp36RevgeoLocation, _Mapping]] = ..., unknown_double2: _Optional[float] = ..., time_zone: _Optional[_Union[Gsp36RevgeoTimeZone, _Mapping]] = ..., unknown_varint6: _Optional[int] = ..., data_source: _Optional[_Union[Gsp36RevgeoDataSource, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoLocation(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Gsp36RevgeoTimeZone(_message.Message):
    __slots__ = ("time_zone",)
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    def __init__(self, time_zone: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoDataSource(_message.Message):
    __slots__ = ("data_source",)
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    data_source: str
    def __init__(self, data_source: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoSubstring2(_message.Message):
    __slots__ = ("substring3", "country", "iso3166_2_code")
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ISO3166_2_CODE_FIELD_NUMBER: _ClassVar[int]
    substring3: Gsp36RevgeoSubstring3
    country: str
    iso3166_2_code: str
    def __init__(self, substring3: _Optional[_Union[Gsp36RevgeoSubstring3, _Mapping]] = ..., country: _Optional[str] = ..., iso3166_2_code: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoSubstring3(_message.Message):
    __slots__ = ("unknown_double1", "unknown_double2")
    UNKNOWN_DOUBLE1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE2_FIELD_NUMBER: _ClassVar[int]
    unknown_double1: float
    unknown_double2: float
    def __init__(self, unknown_double1: _Optional[float] = ..., unknown_double2: _Optional[float] = ...) -> None: ...

class Gsp36RevgeoSubstring4(_message.Message):
    __slots__ = ("substring5",)
    SUBSTRING5_FIELD_NUMBER: _ClassVar[int]
    substring5: Gsp36RevgeoSubstring5
    def __init__(self, substring5: _Optional[_Union[Gsp36RevgeoSubstring5, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoSubstring5(_message.Message):
    __slots__ = ("unknown_varint1", "version", "country_code", "service_info", "street")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    version: str
    country_code: Gsp36RevgeoCountryCode
    service_info: Gsp36RevgeoServiceInfo
    street: Gsp36RevgeoStreet
    def __init__(self, unknown_varint1: _Optional[int] = ..., version: _Optional[str] = ..., country_code: _Optional[_Union[Gsp36RevgeoCountryCode, _Mapping]] = ..., service_info: _Optional[_Union[Gsp36RevgeoServiceInfo, _Mapping]] = ..., street: _Optional[_Union[Gsp36RevgeoStreet, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoCountryCode(_message.Message):
    __slots__ = ("code_country", "country_iphone", "unknown_string")
    CODE_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_IPHONE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING_FIELD_NUMBER: _ClassVar[int]
    code_country: str
    country_iphone: str
    unknown_string: str
    def __init__(self, code_country: _Optional[str] = ..., country_iphone: _Optional[str] = ..., unknown_string: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoServiceInfo(_message.Message):
    __slots__ = ("service", "unknown_varint2", "function", "version")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    service: str
    unknown_varint2: int
    function: str
    version: str
    def __init__(self, service: _Optional[str] = ..., unknown_varint2: _Optional[int] = ..., function: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoStreet(_message.Message):
    __slots__ = ("street_number", "address", "street_strange", "address_info_second", "field7", "field100")
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STREET_STRANGE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_SECOND_FIELD_NUMBER: _ClassVar[int]
    FIELD7_FIELD_NUMBER: _ClassVar[int]
    FIELD100_FIELD_NUMBER: _ClassVar[int]
    street_number: str
    address: Gsp36RevgeoAddress
    street_strange: str
    address_info_second: Gsp36RevgeoAddressInfoSecond
    field7: str
    field100: Gsp36RevgeoAddressInfoThird
    def __init__(self, street_number: _Optional[str] = ..., address: _Optional[_Union[Gsp36RevgeoAddress, _Mapping]] = ..., street_strange: _Optional[str] = ..., address_info_second: _Optional[_Union[Gsp36RevgeoAddressInfoSecond, _Mapping]] = ..., field7: _Optional[str] = ..., field100: _Optional[_Union[Gsp36RevgeoAddressInfoThird, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoAddress(_message.Message):
    __slots__ = ("address_data", "address_info_first")
    ADDRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_FIRST_FIELD_NUMBER: _ClassVar[int]
    address_data: _containers.RepeatedScalarFieldContainer[str]
    address_info_first: Gsp36RevgeoAddressInfoFirst
    def __init__(self, address_data: _Optional[_Iterable[str]] = ..., address_info_first: _Optional[_Union[Gsp36RevgeoAddressInfoFirst, _Mapping]] = ...) -> None: ...

class Gsp36RevgeoAddressInfoFirst(_message.Message):
    __slots__ = ("country", "country_code", "region", "department", "city", "postal_code", "street", "number", "street_number")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    country: str
    country_code: str
    region: str
    department: str
    city: str
    postal_code: str
    street: str
    number: str
    street_number: str
    def __init__(self, country: _Optional[str] = ..., country_code: _Optional[str] = ..., region: _Optional[str] = ..., department: _Optional[str] = ..., city: _Optional[str] = ..., postal_code: _Optional[str] = ..., street: _Optional[str] = ..., number: _Optional[str] = ..., street_number: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoAddressInfoSecond(_message.Message):
    __slots__ = ("country1", "country2", "region", "department", "city", "street", "unknown11", "unknown12")
    COUNTRY1_FIELD_NUMBER: _ClassVar[int]
    COUNTRY2_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN12_FIELD_NUMBER: _ClassVar[int]
    country1: str
    country2: str
    region: str
    department: str
    city: str
    street: str
    unknown11: str
    unknown12: str
    def __init__(self, country1: _Optional[str] = ..., country2: _Optional[str] = ..., region: _Optional[str] = ..., department: _Optional[str] = ..., city: _Optional[str] = ..., street: _Optional[str] = ..., unknown11: _Optional[str] = ..., unknown12: _Optional[str] = ...) -> None: ...

class Gsp36RevgeoAddressInfoThird(_message.Message):
    __slots__ = ("city1", "street", "street_number", "city2")
    CITY1_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CITY2_FIELD_NUMBER: _ClassVar[int]
    city1: str
    street: str
    street_number: str
    city2: str
    def __init__(self, city1: _Optional[str] = ..., street: _Optional[str] = ..., street_number: _Optional[str] = ..., city2: _Optional[str] = ...) -> None: ...
