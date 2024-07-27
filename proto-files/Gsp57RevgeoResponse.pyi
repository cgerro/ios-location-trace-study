from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gsp57RevgeoResponse(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "str", "country_language", "country_code", "str1", "str2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    STR1_FIELD_NUMBER: _ClassVar[int]
    STR2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    str: Gsp57RevgeoString
    country_language: str
    country_code: str
    str1: Gsp57RevgeoString1
    str2: Gsp57RevgeoString2
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., str: _Optional[_Union[Gsp57RevgeoString, _Mapping]] = ..., country_language: _Optional[str] = ..., country_code: _Optional[str] = ..., str1: _Optional[_Union[Gsp57RevgeoString1, _Mapping]] = ..., str2: _Optional[_Union[Gsp57RevgeoString2, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoString(_message.Message):
    __slots__ = ("substr",)
    SUBSTR_FIELD_NUMBER: _ClassVar[int]
    substr: Gsp57RevgeoSubstring
    def __init__(self, substr: _Optional[_Union[Gsp57RevgeoSubstring, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoString1(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoString2(_message.Message):
    __slots__ = ("unknown_varint1", "substr1")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr1: Gsp57RevgeoSubstring_a
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr1: _Optional[_Union[Gsp57RevgeoSubstring_a, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring(_message.Message):
    __slots__ = ("unknown_varint100",)
    UNKNOWN_VARINT100_FIELD_NUMBER: _ClassVar[int]
    unknown_varint100: int
    def __init__(self, unknown_varint100: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring_a(_message.Message):
    __slots__ = ("unknown_varint2", "substr2", "unknown_varint5")
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    SUBSTR2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    unknown_varint2: int
    substr2: _containers.RepeatedCompositeFieldContainer[Gsp57RevgeoSubstring2]
    unknown_varint5: int
    def __init__(self, unknown_varint2: _Optional[int] = ..., substr2: _Optional[_Iterable[_Union[Gsp57RevgeoSubstring2, _Mapping]]] = ..., unknown_varint5: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring2(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint4", "unknown_varint5", "unknown_varint6", "substr3", "apple_service", "unknown_varint10", "substr6", "unknown_varint12")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    SUBSTR3_FIELD_NUMBER: _ClassVar[int]
    APPLE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    SUBSTR6_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint4: int
    unknown_varint5: int
    unknown_varint6: int
    substr3: Gsp57RevgeoSubstring3
    apple_service: _containers.RepeatedScalarFieldContainer[str]
    unknown_varint10: int
    substr6: Gsp57RevgeoSubstring6
    unknown_varint12: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., unknown_varint6: _Optional[int] = ..., substr3: _Optional[_Union[Gsp57RevgeoSubstring3, _Mapping]] = ..., apple_service: _Optional[_Iterable[str]] = ..., unknown_varint10: _Optional[int] = ..., substr6: _Optional[_Union[Gsp57RevgeoSubstring6, _Mapping]] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring3(_message.Message):
    __slots__ = ("substr4", "substr33", "substr15", "substr14", "substr17", "substr7", "substr13", "substr20", "substr23", "substr21")
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    SUBSTR33_FIELD_NUMBER: _ClassVar[int]
    SUBSTR15_FIELD_NUMBER: _ClassVar[int]
    SUBSTR14_FIELD_NUMBER: _ClassVar[int]
    SUBSTR17_FIELD_NUMBER: _ClassVar[int]
    SUBSTR7_FIELD_NUMBER: _ClassVar[int]
    SUBSTR13_FIELD_NUMBER: _ClassVar[int]
    SUBSTR20_FIELD_NUMBER: _ClassVar[int]
    SUBSTR23_FIELD_NUMBER: _ClassVar[int]
    SUBSTR21_FIELD_NUMBER: _ClassVar[int]
    substr4: Gsp57RevgeoSubstring4
    substr33: Gsp57RevgeoSubstring33
    substr15: Gsp57RevgeoSubstring_15
    substr14: Gsp57RevgeoSubstring_14
    substr17: Gsp57RevgeoSubstring_17
    substr7: Gsp57RevgeoSubstring7
    substr13: Gsp57RevgeoSubstring_13
    substr20: Gsp57RevgeoSubstring20
    substr23: Gsp57RevgeoSubstring23
    substr21: Gsp57RevgeoSubstring21
    def __init__(self, substr4: _Optional[_Union[Gsp57RevgeoSubstring4, _Mapping]] = ..., substr33: _Optional[_Union[Gsp57RevgeoSubstring33, _Mapping]] = ..., substr15: _Optional[_Union[Gsp57RevgeoSubstring_15, _Mapping]] = ..., substr14: _Optional[_Union[Gsp57RevgeoSubstring_14, _Mapping]] = ..., substr17: _Optional[_Union[Gsp57RevgeoSubstring_17, _Mapping]] = ..., substr7: _Optional[_Union[Gsp57RevgeoSubstring7, _Mapping]] = ..., substr13: _Optional[_Union[Gsp57RevgeoSubstring_13, _Mapping]] = ..., substr20: _Optional[_Union[Gsp57RevgeoSubstring20, _Mapping]] = ..., substr23: _Optional[_Union[Gsp57RevgeoSubstring23, _Mapping]] = ..., substr21: _Optional[_Union[Gsp57RevgeoSubstring21, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring4(_message.Message):
    __slots__ = ("unknown_varint1", "substr5", "unknown_varint19")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT19_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr5: Gsp57RevgeoSubstring5
    unknown_varint19: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr5: _Optional[_Union[Gsp57RevgeoSubstring5, _Mapping]] = ..., unknown_varint19: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring5(_message.Message):
    __slots__ = ("country_language", "address_request")
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    country_language: str
    address_request: str
    def __init__(self, country_language: _Optional[str] = ..., address_request: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring6(_message.Message):
    __slots__ = ("place_request_id",)
    PLACE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    place_request_id: str
    def __init__(self, place_request_id: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring7(_message.Message):
    __slots__ = ("substr8",)
    SUBSTR8_FIELD_NUMBER: _ClassVar[int]
    substr8: Gsp57RevgeoSubstring8
    def __init__(self, substr8: _Optional[_Union[Gsp57RevgeoSubstring8, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring8(_message.Message):
    __slots__ = ("substr10", "unknown_varint7", "substr9")
    SUBSTR10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    SUBSTR9_FIELD_NUMBER: _ClassVar[int]
    substr10: Gsp57RevgeoSubstring_10
    unknown_varint7: int
    substr9: Gsp57RevgeoSubstring9
    def __init__(self, substr10: _Optional[_Union[Gsp57RevgeoSubstring_10, _Mapping]] = ..., unknown_varint7: _Optional[int] = ..., substr9: _Optional[_Union[Gsp57RevgeoSubstring9, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring9(_message.Message):
    __slots__ = ("substr11",)
    SUBSTR11_FIELD_NUMBER: _ClassVar[int]
    substr11: Gsp57RevgeoSubstring_11
    def __init__(self, substr11: _Optional[_Union[Gsp57RevgeoSubstring_11, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring_10(_message.Message):
    __slots__ = ("service",)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str
    def __init__(self, service: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring_11(_message.Message):
    __slots__ = ("unknown_varint3", "substr12")
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBSTR12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint3: int
    substr12: Gsp57RevgeoSubstring_12
    def __init__(self, unknown_varint3: _Optional[int] = ..., substr12: _Optional[_Union[Gsp57RevgeoSubstring_12, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring_12(_message.Message):
    __slots__ = ("loc_request", "unknown_double3", "unknown_double5")
    LOC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE5_FIELD_NUMBER: _ClassVar[int]
    loc_request: Gsp57RevgeoLocationRequest
    unknown_double3: float
    unknown_double5: float
    def __init__(self, loc_request: _Optional[_Union[Gsp57RevgeoLocationRequest, _Mapping]] = ..., unknown_double3: _Optional[float] = ..., unknown_double5: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoLocationRequest(_message.Message):
    __slots__ = ("lat_request", "long_request")
    LAT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LONG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    lat_request: float
    long_request: float
    def __init__(self, lat_request: _Optional[float] = ..., long_request: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoSubstring_13(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring_14(_message.Message):
    __slots__ = ("locations", "locations1")
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS1_FIELD_NUMBER: _ClassVar[int]
    locations: Gsp57RevgeoLocations
    locations1: Gsp57RevgeoLocations
    def __init__(self, locations: _Optional[_Union[Gsp57RevgeoLocations, _Mapping]] = ..., locations1: _Optional[_Union[Gsp57RevgeoLocations, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoLocations(_message.Message):
    __slots__ = ("lat1", "long1", "lat2", "long2", "unknown_varint4")
    LAT1_FIELD_NUMBER: _ClassVar[int]
    LONG1_FIELD_NUMBER: _ClassVar[int]
    LAT2_FIELD_NUMBER: _ClassVar[int]
    LONG2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    lat1: float
    long1: float
    lat2: float
    long2: float
    unknown_varint4: int
    def __init__(self, lat1: _Optional[float] = ..., long1: _Optional[float] = ..., lat2: _Optional[float] = ..., long2: _Optional[float] = ..., unknown_varint4: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring_15(_message.Message):
    __slots__ = ("substr16",)
    SUBSTR16_FIELD_NUMBER: _ClassVar[int]
    substr16: Gsp57RevgeoSubstring_16
    def __init__(self, substr16: _Optional[_Union[Gsp57RevgeoSubstring_16, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring_16(_message.Message):
    __slots__ = ("loc_request", "unknown_varint2", "unknown_varint3", "unknown_varint4", "unknown_varint13")
    LOC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT13_FIELD_NUMBER: _ClassVar[int]
    loc_request: Gsp57RevgeoLocationRequest
    unknown_varint2: int
    unknown_varint3: int
    unknown_varint4: int
    unknown_varint13: int
    def __init__(self, loc_request: _Optional[_Union[Gsp57RevgeoLocationRequest, _Mapping]] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint13: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring_17(_message.Message):
    __slots__ = ("substr18",)
    SUBSTR18_FIELD_NUMBER: _ClassVar[int]
    substr18: Gsp57RevgeoSubstring_18
    def __init__(self, substr18: _Optional[_Union[Gsp57RevgeoSubstring_18, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring_18(_message.Message):
    __slots__ = ("unknown_varint1", "version", "substr19", "service_info", "street")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBSTR19_FIELD_NUMBER: _ClassVar[int]
    SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    version: str
    substr19: Gsp57RevgeoSubstring_19
    service_info: Gsp57RevgeoServiceInfo
    street: Gsp57RevgeoStreet
    def __init__(self, unknown_varint1: _Optional[int] = ..., version: _Optional[str] = ..., substr19: _Optional[_Union[Gsp57RevgeoSubstring_19, _Mapping]] = ..., service_info: _Optional[_Union[Gsp57RevgeoServiceInfo, _Mapping]] = ..., street: _Optional[_Union[Gsp57RevgeoStreet, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring_19(_message.Message):
    __slots__ = ("country_language", "country_code", "unknown_string3")
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING3_FIELD_NUMBER: _ClassVar[int]
    country_language: str
    country_code: str
    unknown_string3: str
    def __init__(self, country_language: _Optional[str] = ..., country_code: _Optional[str] = ..., unknown_string3: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoServiceInfo(_message.Message):
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

class Gsp57RevgeoStreet(_message.Message):
    __slots__ = ("street_number", "address", "street_strange", "address_info_second", "substring6", "address_info_third")
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STREET_STRANGE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_SECOND_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING6_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_THIRD_FIELD_NUMBER: _ClassVar[int]
    street_number: str
    address: Gsp57RevgeoAddress
    street_strange: str
    address_info_second: Gsp57RevgeoAddressInfoSecond
    substring6: Gsp57RevgeoSubstring6
    address_info_third: Gsp57RevgeoAddressInfoThird
    def __init__(self, street_number: _Optional[str] = ..., address: _Optional[_Union[Gsp57RevgeoAddress, _Mapping]] = ..., street_strange: _Optional[str] = ..., address_info_second: _Optional[_Union[Gsp57RevgeoAddressInfoSecond, _Mapping]] = ..., substring6: _Optional[_Union[Gsp57RevgeoSubstring6, _Mapping]] = ..., address_info_third: _Optional[_Union[Gsp57RevgeoAddressInfoThird, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoAddress(_message.Message):
    __slots__ = ("address_data", "address_info_first")
    ADDRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_FIRST_FIELD_NUMBER: _ClassVar[int]
    address_data: _containers.RepeatedScalarFieldContainer[str]
    address_info_first: Gsp57RevgeoAddressInfoFirst
    def __init__(self, address_data: _Optional[_Iterable[str]] = ..., address_info_first: _Optional[_Union[Gsp57RevgeoAddressInfoFirst, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoAddressInfoFirst(_message.Message):
    __slots__ = ("country", "country_code", "region", "department", "city1", "city2", "postal_code", "quartier", "street", "number", "street_number", "district_info")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CITY1_FIELD_NUMBER: _ClassVar[int]
    CITY2_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    QUARTIER_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISTRICT_INFO_FIELD_NUMBER: _ClassVar[int]
    country: str
    country_code: str
    region: str
    department: str
    city1: str
    city2: str
    postal_code: str
    quartier: str
    street: str
    number: str
    street_number: str
    district_info: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, country: _Optional[str] = ..., country_code: _Optional[str] = ..., region: _Optional[str] = ..., department: _Optional[str] = ..., city1: _Optional[str] = ..., city2: _Optional[str] = ..., postal_code: _Optional[str] = ..., quartier: _Optional[str] = ..., street: _Optional[str] = ..., number: _Optional[str] = ..., street_number: _Optional[str] = ..., district_info: _Optional[_Iterable[str]] = ...) -> None: ...

class Gsp57RevgeoAddressInfoSecond(_message.Message):
    __slots__ = ("country1", "country2", "region1", "region2", "city1", "city2", "district", "street", "street_strange1", "street_strange2", "district_info")
    COUNTRY1_FIELD_NUMBER: _ClassVar[int]
    COUNTRY2_FIELD_NUMBER: _ClassVar[int]
    REGION1_FIELD_NUMBER: _ClassVar[int]
    REGION2_FIELD_NUMBER: _ClassVar[int]
    CITY1_FIELD_NUMBER: _ClassVar[int]
    CITY2_FIELD_NUMBER: _ClassVar[int]
    DISTRICT_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    STREET_STRANGE1_FIELD_NUMBER: _ClassVar[int]
    STREET_STRANGE2_FIELD_NUMBER: _ClassVar[int]
    DISTRICT_INFO_FIELD_NUMBER: _ClassVar[int]
    country1: str
    country2: str
    region1: str
    region2: str
    city1: str
    city2: str
    district: str
    street: str
    street_strange1: str
    street_strange2: str
    district_info: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, country1: _Optional[str] = ..., country2: _Optional[str] = ..., region1: _Optional[str] = ..., region2: _Optional[str] = ..., city1: _Optional[str] = ..., city2: _Optional[str] = ..., district: _Optional[str] = ..., street: _Optional[str] = ..., street_strange1: _Optional[str] = ..., street_strange2: _Optional[str] = ..., district_info: _Optional[_Iterable[str]] = ...) -> None: ...

class Gsp57RevgeoAddressInfoThird(_message.Message):
    __slots__ = ("city1", "street", "address", "city2")
    CITY1_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY2_FIELD_NUMBER: _ClassVar[int]
    city1: str
    street: str
    address: str
    city2: str
    def __init__(self, city1: _Optional[str] = ..., street: _Optional[str] = ..., address: _Optional[str] = ..., city2: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring20(_message.Message):
    __slots__ = ("unknown_varint1", "location_info")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    location_info: Gsp57RevgeoLocationInfo
    def __init__(self, unknown_varint1: _Optional[int] = ..., location_info: _Optional[_Union[Gsp57RevgeoLocationInfo, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoLocationInfo(_message.Message):
    __slots__ = ("street_number", "district", "unknown_double3", "unknown_double4", "city")
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISTRICT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE4_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    street_number: str
    district: str
    unknown_double3: float
    unknown_double4: float
    city: str
    def __init__(self, street_number: _Optional[str] = ..., district: _Optional[str] = ..., unknown_double3: _Optional[float] = ..., unknown_double4: _Optional[float] = ..., city: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring21(_message.Message):
    __slots__ = ("substr22", "country_code", "country_state_code")
    SUBSTR22_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_STATE_CODE_FIELD_NUMBER: _ClassVar[int]
    substr22: Gsp57RevgeoSubstring22
    country_code: str
    country_state_code: str
    def __init__(self, substr22: _Optional[_Union[Gsp57RevgeoSubstring22, _Mapping]] = ..., country_code: _Optional[str] = ..., country_state_code: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring22(_message.Message):
    __slots__ = ("unknown_float1", "unknown_float2")
    UNKNOWN_FLOAT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT2_FIELD_NUMBER: _ClassVar[int]
    unknown_float1: float
    unknown_float2: float
    def __init__(self, unknown_float1: _Optional[float] = ..., unknown_float2: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoSubstring23(_message.Message):
    __slots__ = ("substr24",)
    SUBSTR24_FIELD_NUMBER: _ClassVar[int]
    substr24: Gsp57RevgeoSubstring24
    def __init__(self, substr24: _Optional[_Union[Gsp57RevgeoSubstring24, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring24(_message.Message):
    __slots__ = ("substr25", "loc_request", "location")
    SUBSTR25_FIELD_NUMBER: _ClassVar[int]
    LOC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    substr25: Gsp57RevgeoSubstring25
    loc_request: Gsp57RevgeoLocationRequest
    location: Gsp57RevgeoLocation
    def __init__(self, substr25: _Optional[_Union[Gsp57RevgeoSubstring25, _Mapping]] = ..., loc_request: _Optional[_Union[Gsp57RevgeoLocationRequest, _Mapping]] = ..., location: _Optional[_Union[Gsp57RevgeoLocation, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring25(_message.Message):
    __slots__ = ("unknown_varint1", "substr26", "unknown_varint4", "unknown_varint5", "location", "substr29", "substr30", "substr31", "substr32")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR26_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUBSTR29_FIELD_NUMBER: _ClassVar[int]
    SUBSTR30_FIELD_NUMBER: _ClassVar[int]
    SUBSTR31_FIELD_NUMBER: _ClassVar[int]
    SUBSTR32_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr26: _containers.RepeatedCompositeFieldContainer[Gsp57RevgeoSubstring26]
    unknown_varint4: int
    unknown_varint5: int
    location: Gsp57RevgeoLocation
    substr29: Gsp57RevgeoSubstring29
    substr30: Gsp57RevgeoSubstring30
    substr31: Gsp57RevgeoSubstring31
    substr32: Gsp57RevgeoSubstring32
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr26: _Optional[_Iterable[_Union[Gsp57RevgeoSubstring26, _Mapping]]] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., location: _Optional[_Union[Gsp57RevgeoLocation, _Mapping]] = ..., substr29: _Optional[_Union[Gsp57RevgeoSubstring29, _Mapping]] = ..., substr30: _Optional[_Union[Gsp57RevgeoSubstring30, _Mapping]] = ..., substr31: _Optional[_Union[Gsp57RevgeoSubstring31, _Mapping]] = ..., substr32: _Optional[_Union[Gsp57RevgeoSubstring32, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoSubstring26(_message.Message):
    __slots__ = ("unknown_varint1", "substr27", "substr28", "unknown_varint6")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR27_FIELD_NUMBER: _ClassVar[int]
    SUBSTR28_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr27: Gsp57RevgeoSubstring27
    substr28: Gsp57RevgeoSubstring28
    unknown_varint6: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr27: _Optional[_Union[Gsp57RevgeoSubstring27, _Mapping]] = ..., substr28: _Optional[_Union[Gsp57RevgeoSubstring28, _Mapping]] = ..., unknown_varint6: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring27(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_double2", "unknown_double3", "unknown_double4", "unknown_double5", "unknown_double6", "unknown_double7", "unknown_double8", "unknown_double9", "unknown_double10")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE6_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE7_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE8_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE10_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_double2: float
    unknown_double3: float
    unknown_double4: float
    unknown_double5: float
    unknown_double6: float
    unknown_double7: float
    unknown_double8: float
    unknown_double9: float
    unknown_double10: float
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_double2: _Optional[float] = ..., unknown_double3: _Optional[float] = ..., unknown_double4: _Optional[float] = ..., unknown_double5: _Optional[float] = ..., unknown_double6: _Optional[float] = ..., unknown_double7: _Optional[float] = ..., unknown_double8: _Optional[float] = ..., unknown_double9: _Optional[float] = ..., unknown_double10: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoSubstring28(_message.Message):
    __slots__ = ("unknown_double1", "unknown_double2", "unknown_double3", "unknown_double4", "unknown_double5", "unknown_double6")
    UNKNOWN_DOUBLE1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE6_FIELD_NUMBER: _ClassVar[int]
    unknown_double1: float
    unknown_double2: float
    unknown_double3: float
    unknown_double4: float
    unknown_double5: float
    unknown_double6: float
    def __init__(self, unknown_double1: _Optional[float] = ..., unknown_double2: _Optional[float] = ..., unknown_double3: _Optional[float] = ..., unknown_double4: _Optional[float] = ..., unknown_double5: _Optional[float] = ..., unknown_double6: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoLocation(_message.Message):
    __slots__ = ("lat", "long", "altitude")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    lat: float
    long: float
    altitude: float
    def __init__(self, lat: _Optional[float] = ..., long: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class Gsp57RevgeoSubstring29(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint3", "unknown_varint4", "unknown_varint5", "unknown_varint6", "unknown_varint9", "unknown_varint10", "unknown_varint11", "unknown_varint12")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT9_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint3: int
    unknown_varint4: int
    unknown_varint5: int
    unknown_varint6: int
    unknown_varint9: int
    unknown_varint10: int
    unknown_varint11: int
    unknown_varint12: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., unknown_varint6: _Optional[int] = ..., unknown_varint9: _Optional[int] = ..., unknown_varint10: _Optional[int] = ..., unknown_varint11: _Optional[int] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring30(_message.Message):
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

class Gsp57RevgeoSubstring31(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint3")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint3: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ...) -> None: ...

class Gsp57RevgeoSubstring32(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unknown_varint1: _Optional[_Iterable[int]] = ...) -> None: ...

class Gsp57RevgeoSubstring33(_message.Message):
    __slots__ = ("location", "timezone", "unknown_varint6", "substring34")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING34_FIELD_NUMBER: _ClassVar[int]
    location: Gsp57RevgeoLocation
    timezone: Gsp57RevgeoTimezone
    unknown_varint6: int
    substring34: Gsp57RevgeoSubstring34
    def __init__(self, location: _Optional[_Union[Gsp57RevgeoLocation, _Mapping]] = ..., timezone: _Optional[_Union[Gsp57RevgeoTimezone, _Mapping]] = ..., unknown_varint6: _Optional[int] = ..., substring34: _Optional[_Union[Gsp57RevgeoSubstring34, _Mapping]] = ...) -> None: ...

class Gsp57RevgeoTimezone(_message.Message):
    __slots__ = ("timezone",)
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    def __init__(self, timezone: _Optional[str] = ...) -> None: ...

class Gsp57RevgeoSubstring34(_message.Message):
    __slots__ = ("unknown_string1",)
    UNKNOWN_STRING1_FIELD_NUMBER: _ClassVar[int]
    unknown_string1: str
    def __init__(self, unknown_string1: _Optional[str] = ...) -> None: ...
