from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GspDispatcherResponse(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "substring3", "country_language", "country_code", "substring9", "substring10")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING3_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING9_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING10_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    substring3: Substring1
    country_language: str
    country_code: str
    substring9: Substring
    substring10: GspDispatcherString
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., substring3: _Optional[_Union[Substring1, _Mapping]] = ..., country_language: _Optional[str] = ..., country_code: _Optional[str] = ..., substring9: _Optional[_Union[Substring, _Mapping]] = ..., substring10: _Optional[_Union[GspDispatcherString, _Mapping]] = ...) -> None: ...

class Substring(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class Substring1(_message.Message):
    __slots__ = ("substring4", "substring15")
    SUBSTRING4_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING15_FIELD_NUMBER: _ClassVar[int]
    substring4: Substring3
    substring15: Substring2
    def __init__(self, substring4: _Optional[_Union[Substring3, _Mapping]] = ..., substring15: _Optional[_Union[Substring2, _Mapping]] = ...) -> None: ...

class Substring2(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: str
    def __init__(self, action: _Optional[str] = ...) -> None: ...

class Substring3(_message.Message):
    __slots__ = ("unknown_varint100",)
    UNKNOWN_VARINT100_FIELD_NUMBER: _ClassVar[int]
    unknown_varint100: int
    def __init__(self, unknown_varint100: _Optional[int] = ...) -> None: ...

class GspDispatcherString(_message.Message):
    __slots__ = ("unknown_varint1", "substr2")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR2_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr2: GspDispatcherSubstring
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr2: _Optional[_Union[GspDispatcherSubstring, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring1(_message.Message):
    __slots__ = ("unknown_varint100",)
    UNKNOWN_VARINT100_FIELD_NUMBER: _ClassVar[int]
    unknown_varint100: int
    def __init__(self, unknown_varint100: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring(_message.Message):
    __slots__ = ("unknown_varint2", "substr4", "unknown_varint5", "substr7")
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    SUBSTR7_FIELD_NUMBER: _ClassVar[int]
    unknown_varint2: int
    substr4: _containers.RepeatedCompositeFieldContainer[GspDispatcherSubstring2]
    unknown_varint5: int
    substr7: GspDispatcherSubstring39
    def __init__(self, unknown_varint2: _Optional[int] = ..., substr4: _Optional[_Iterable[_Union[GspDispatcherSubstring2, _Mapping]]] = ..., unknown_varint5: _Optional[int] = ..., substr7: _Optional[_Union[GspDispatcherSubstring39, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring39(_message.Message):
    __slots__ = ("substr1",)
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    substr1: GspDispatcherSubstring40
    def __init__(self, substr1: _Optional[_Union[GspDispatcherSubstring40, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring40(_message.Message):
    __slots__ = ("location", "unknown_varint3", "unknown_varint4", "unknown_varint50")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT50_FIELD_NUMBER: _ClassVar[int]
    location: GspDispatcherLocation
    unknown_varint3: int
    unknown_varint4: int
    unknown_varint50: int
    def __init__(self, location: _Optional[_Union[GspDispatcherLocation, _Mapping]] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint50: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring2(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint4", "unknown_varint5", "unknown_varint6", "substr8", "apple_service", "unknown_varint10", "substr11", "unknown_varint12")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    SUBSTR8_FIELD_NUMBER: _ClassVar[int]
    APPLE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT10_FIELD_NUMBER: _ClassVar[int]
    SUBSTR11_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint4: int
    unknown_varint5: int
    unknown_varint6: int
    substr8: GspDispatcherSubstring3
    apple_service: _containers.RepeatedScalarFieldContainer[str]
    unknown_varint10: int
    substr11: GspDispatcherSubstring4
    unknown_varint12: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., unknown_varint6: _Optional[int] = ..., substr8: _Optional[_Union[GspDispatcherSubstring3, _Mapping]] = ..., apple_service: _Optional[_Iterable[str]] = ..., unknown_varint10: _Optional[int] = ..., substr11: _Optional[_Union[GspDispatcherSubstring4, _Mapping]] = ..., unknown_varint12: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring3(_message.Message):
    __slots__ = ("substr1", "substr2", "substr3", "substr4", "substr31", "substr41", "substr44", "substr56", "substr59", "substr66", "substr77")
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR2_FIELD_NUMBER: _ClassVar[int]
    SUBSTR3_FIELD_NUMBER: _ClassVar[int]
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    SUBSTR31_FIELD_NUMBER: _ClassVar[int]
    SUBSTR41_FIELD_NUMBER: _ClassVar[int]
    SUBSTR44_FIELD_NUMBER: _ClassVar[int]
    SUBSTR56_FIELD_NUMBER: _ClassVar[int]
    SUBSTR59_FIELD_NUMBER: _ClassVar[int]
    SUBSTR66_FIELD_NUMBER: _ClassVar[int]
    SUBSTR77_FIELD_NUMBER: _ClassVar[int]
    substr1: GspdispatcherSubstring5
    substr2: GspDispatcherSubstring6
    substr3: GspDispatcherSubstring7
    substr4: GspDispatcherSubstring8
    substr31: GspDispatcherSubstring9
    substr41: GspDispatcherSubstring10
    substr44: GspDispatcherSubstring11
    substr56: GspDispatcherSubstring12
    substr59: GspDispatcherSubstring13
    substr66: GspDispatcherSubstring36
    substr77: GspDispatcherSubstring14
    def __init__(self, substr1: _Optional[_Union[GspdispatcherSubstring5, _Mapping]] = ..., substr2: _Optional[_Union[GspDispatcherSubstring6, _Mapping]] = ..., substr3: _Optional[_Union[GspDispatcherSubstring7, _Mapping]] = ..., substr4: _Optional[_Union[GspDispatcherSubstring8, _Mapping]] = ..., substr31: _Optional[_Union[GspDispatcherSubstring9, _Mapping]] = ..., substr41: _Optional[_Union[GspDispatcherSubstring10, _Mapping]] = ..., substr44: _Optional[_Union[GspDispatcherSubstring11, _Mapping]] = ..., substr56: _Optional[_Union[GspDispatcherSubstring12, _Mapping]] = ..., substr59: _Optional[_Union[GspDispatcherSubstring13, _Mapping]] = ..., substr66: _Optional[_Union[GspDispatcherSubstring36, _Mapping]] = ..., substr77: _Optional[_Union[GspDispatcherSubstring14, _Mapping]] = ...) -> None: ...

class GspdispatcherSubstring5(_message.Message):
    __slots__ = ("unknown_varint1", "substr5", "substr10", "unknown_varint19")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR5_FIELD_NUMBER: _ClassVar[int]
    SUBSTR10_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT19_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr5: GspDispatcherSubstring15
    substr10: GspDispatcherSubstring35
    unknown_varint19: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr5: _Optional[_Union[GspDispatcherSubstring15, _Mapping]] = ..., substr10: _Optional[_Union[GspDispatcherSubstring35, _Mapping]] = ..., unknown_varint19: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring15(_message.Message):
    __slots__ = ("country_language", "address_request")
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    country_language: str
    address_request: str
    def __init__(self, country_language: _Optional[str] = ..., address_request: _Optional[str] = ...) -> None: ...

class GspDispatcherSubstring35(_message.Message):
    __slots__ = ("country_language", "place")
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PLACE_FIELD_NUMBER: _ClassVar[int]
    country_language: str
    place: str
    def __init__(self, country_language: _Optional[str] = ..., place: _Optional[str] = ...) -> None: ...

class GspDispatcherSubstring36(_message.Message):
    __slots__ = ("substr1", "unknown_varint2")
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    substr1: _containers.RepeatedCompositeFieldContainer[GspDispatcherSubstring37]
    unknown_varint2: int
    def __init__(self, substr1: _Optional[_Iterable[_Union[GspDispatcherSubstring37, _Mapping]]] = ..., unknown_varint2: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring37(_message.Message):
    __slots__ = ("substr1",)
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    substr1: GspDispatcherSubstring38
    def __init__(self, substr1: _Optional[_Union[GspDispatcherSubstring38, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring38(_message.Message):
    __slots__ = ("unknown_varint1", "location", "unknown_varint3", "unknown_varint50")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT50_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    location: GspDispatcherLocation
    unknown_varint3: int
    unknown_varint50: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., location: _Optional[_Union[GspDispatcherLocation, _Mapping]] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint50: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring4(_message.Message):
    __slots__ = ("place_request_id",)
    PLACE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    place_request_id: str
    def __init__(self, place_request_id: _Optional[str] = ...) -> None: ...

class GspDispatcherSubstring10(_message.Message):
    __slots__ = ("substr10000",)
    SUBSTR10000_FIELD_NUMBER: _ClassVar[int]
    substr10000: GspDispatcherSubstring16
    def __init__(self, substr10000: _Optional[_Union[GspDispatcherSubstring16, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring16(_message.Message):
    __slots__ = ("substr1", "unknown_varint7", "substr8")
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT7_FIELD_NUMBER: _ClassVar[int]
    SUBSTR8_FIELD_NUMBER: _ClassVar[int]
    substr1: GspDispatcherSubstring17
    unknown_varint7: int
    substr8: GspDispatcherSubstring18
    def __init__(self, substr1: _Optional[_Union[GspDispatcherSubstring17, _Mapping]] = ..., unknown_varint7: _Optional[int] = ..., substr8: _Optional[_Union[GspDispatcherSubstring18, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring18(_message.Message):
    __slots__ = ("substr4",)
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    substr4: GspDispatcherSubstring19
    def __init__(self, substr4: _Optional[_Union[GspDispatcherSubstring19, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring17(_message.Message):
    __slots__ = ("service",)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str
    def __init__(self, service: _Optional[str] = ...) -> None: ...

class GspDispatcherSubstring19(_message.Message):
    __slots__ = ("unknown_varint3", "substr4")
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    unknown_varint3: int
    substr4: GspDispatcherSubstring20
    def __init__(self, unknown_varint3: _Optional[int] = ..., substr4: _Optional[_Union[GspDispatcherSubstring20, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring20(_message.Message):
    __slots__ = ("loc_request", "unknown_double3", "unknown_double5")
    LOC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DOUBLE5_FIELD_NUMBER: _ClassVar[int]
    loc_request: GspDispatcherLocationRequest
    unknown_double3: float
    unknown_double5: float
    def __init__(self, loc_request: _Optional[_Union[GspDispatcherLocationRequest, _Mapping]] = ..., unknown_double3: _Optional[float] = ..., unknown_double5: _Optional[float] = ...) -> None: ...

class GspDispatcherLocationRequest(_message.Message):
    __slots__ = ("lat_request", "long_request")
    LAT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LONG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    lat_request: float
    long_request: float
    def __init__(self, lat_request: _Optional[float] = ..., long_request: _Optional[float] = ...) -> None: ...

class GspDispatcherSubstring11(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    def __init__(self, unknown_varint1: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring8(_message.Message):
    __slots__ = ("locations", "locations1")
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS1_FIELD_NUMBER: _ClassVar[int]
    locations: GspDispatcherLocations
    locations1: GspDispatcherLocations
    def __init__(self, locations: _Optional[_Union[GspDispatcherLocations, _Mapping]] = ..., locations1: _Optional[_Union[GspDispatcherLocations, _Mapping]] = ...) -> None: ...

class GspDispatcherLocations(_message.Message):
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

class GspDispatcherSubstring7(_message.Message):
    __slots__ = ("substr1",)
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    substr1: GspDispatcherSubstring21
    def __init__(self, substr1: _Optional[_Union[GspDispatcherSubstring21, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring21(_message.Message):
    __slots__ = ("loc_request", "unknown_varint2", "unknown_varint3", "unknown_varint4", "unknown_varint13")
    LOC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT13_FIELD_NUMBER: _ClassVar[int]
    loc_request: GspDispatcherLocationRequest
    unknown_varint2: int
    unknown_varint3: int
    unknown_varint4: int
    unknown_varint13: int
    def __init__(self, loc_request: _Optional[_Union[GspDispatcherLocationRequest, _Mapping]] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint13: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring9(_message.Message):
    __slots__ = ("substr1",)
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    substr1: GspDispatcherSubstring22
    def __init__(self, substr1: _Optional[_Union[GspDispatcherSubstring22, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring22(_message.Message):
    __slots__ = ("unknown_varint1", "version", "substr3", "service_info", "street")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBSTR3_FIELD_NUMBER: _ClassVar[int]
    SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    version: str
    substr3: GspDispatcherSubstring23
    service_info: GspDispatcherServiceInfo
    street: GspDispatcherStreet
    def __init__(self, unknown_varint1: _Optional[int] = ..., version: _Optional[str] = ..., substr3: _Optional[_Union[GspDispatcherSubstring23, _Mapping]] = ..., service_info: _Optional[_Union[GspDispatcherServiceInfo, _Mapping]] = ..., street: _Optional[_Union[GspDispatcherStreet, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring23(_message.Message):
    __slots__ = ("country_language", "country_code", "unknown_string3")
    COUNTRY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STRING3_FIELD_NUMBER: _ClassVar[int]
    country_language: str
    country_code: str
    unknown_string3: str
    def __init__(self, country_language: _Optional[str] = ..., country_code: _Optional[str] = ..., unknown_string3: _Optional[str] = ...) -> None: ...

class GspDispatcherServiceInfo(_message.Message):
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

class GspDispatcherStreet(_message.Message):
    __slots__ = ("street_number", "address", "street_strange", "address_info_second", "substring7", "address_info_third")
    STREET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STREET_STRANGE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_SECOND_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING7_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_THIRD_FIELD_NUMBER: _ClassVar[int]
    street_number: str
    address: GspDispatcherAddress
    street_strange: str
    address_info_second: GspDispatcherAddressInfoSecond
    substring7: GspDispatcherSubstring4
    address_info_third: GspDispatcherAddressInfoThird
    def __init__(self, street_number: _Optional[str] = ..., address: _Optional[_Union[GspDispatcherAddress, _Mapping]] = ..., street_strange: _Optional[str] = ..., address_info_second: _Optional[_Union[GspDispatcherAddressInfoSecond, _Mapping]] = ..., substring7: _Optional[_Union[GspDispatcherSubstring4, _Mapping]] = ..., address_info_third: _Optional[_Union[GspDispatcherAddressInfoThird, _Mapping]] = ...) -> None: ...

class GspDispatcherAddress(_message.Message):
    __slots__ = ("address_data", "address_info_first")
    ADDRESS_DATA_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_INFO_FIRST_FIELD_NUMBER: _ClassVar[int]
    address_data: _containers.RepeatedScalarFieldContainer[str]
    address_info_first: GspDispatcherAddressInfoFirst
    def __init__(self, address_data: _Optional[_Iterable[str]] = ..., address_info_first: _Optional[_Union[GspDispatcherAddressInfoFirst, _Mapping]] = ...) -> None: ...

class GspDispatcherAddressInfoFirst(_message.Message):
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

class GspDispatcherAddressInfoSecond(_message.Message):
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

class GspDispatcherAddressInfoThird(_message.Message):
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

class GspDispatcherSubstring12(_message.Message):
    __slots__ = ("unknown_varint1", "location_info")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    location_info: GspDispatcherLocationInfo
    def __init__(self, unknown_varint1: _Optional[int] = ..., location_info: _Optional[_Union[GspDispatcherLocationInfo, _Mapping]] = ...) -> None: ...

class GspDispatcherLocationInfo(_message.Message):
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

class GspDispatcherSubstring14(_message.Message):
    __slots__ = ("substr1", "country_code", "country_state_code")
    SUBSTR1_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_STATE_CODE_FIELD_NUMBER: _ClassVar[int]
    substr1: GspDispatcherSubstring24
    country_code: str
    country_state_code: str
    def __init__(self, substr1: _Optional[_Union[GspDispatcherSubstring24, _Mapping]] = ..., country_code: _Optional[str] = ..., country_state_code: _Optional[str] = ...) -> None: ...

class GspDispatcherSubstring24(_message.Message):
    __slots__ = ("unknown_float1", "unknown_float2")
    UNKNOWN_FLOAT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FLOAT2_FIELD_NUMBER: _ClassVar[int]
    unknown_float1: float
    unknown_float2: float
    def __init__(self, unknown_float1: _Optional[float] = ..., unknown_float2: _Optional[float] = ...) -> None: ...

class GspDispatcherSubstring13(_message.Message):
    __slots__ = ("substr4",)
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    substr4: GspDispatcherSubstring25
    def __init__(self, substr4: _Optional[_Union[GspDispatcherSubstring25, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring25(_message.Message):
    __slots__ = ("substr2", "loc_request", "location")
    SUBSTR2_FIELD_NUMBER: _ClassVar[int]
    LOC_REQUEST_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    substr2: GspDispatcherSubstring26
    loc_request: GspDispatcherLocationRequest
    location: GspDispatcherLocation
    def __init__(self, substr2: _Optional[_Union[GspDispatcherSubstring26, _Mapping]] = ..., loc_request: _Optional[_Union[GspDispatcherLocationRequest, _Mapping]] = ..., location: _Optional[_Union[GspDispatcherLocation, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring26(_message.Message):
    __slots__ = ("unknown_varint1", "substr2", "unknown_varint4", "unknown_varint5", "location", "substr8", "substr10", "substr11", "substr12")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT4_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT5_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUBSTR8_FIELD_NUMBER: _ClassVar[int]
    SUBSTR10_FIELD_NUMBER: _ClassVar[int]
    SUBSTR11_FIELD_NUMBER: _ClassVar[int]
    SUBSTR12_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr2: _containers.RepeatedCompositeFieldContainer[GspDispatcherSubstring34]
    unknown_varint4: int
    unknown_varint5: int
    location: GspDispatcherLocation
    substr8: GspDispatcherSubstring27
    substr10: GspDispatcherSubstring28
    substr11: GspDispatcherSubstring29
    substr12: GspDispatcherSubstring30
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr2: _Optional[_Iterable[_Union[GspDispatcherSubstring34, _Mapping]]] = ..., unknown_varint4: _Optional[int] = ..., unknown_varint5: _Optional[int] = ..., location: _Optional[_Union[GspDispatcherLocation, _Mapping]] = ..., substr8: _Optional[_Union[GspDispatcherSubstring27, _Mapping]] = ..., substr10: _Optional[_Union[GspDispatcherSubstring28, _Mapping]] = ..., substr11: _Optional[_Union[GspDispatcherSubstring29, _Mapping]] = ..., substr12: _Optional[_Union[GspDispatcherSubstring30, _Mapping]] = ...) -> None: ...

class GspDispatcherSubstring34(_message.Message):
    __slots__ = ("unknown_varint1", "substr4", "substr5", "unknown_varint6")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    SUBSTR4_FIELD_NUMBER: _ClassVar[int]
    SUBSTR5_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    substr4: GspDispatcherSubstring31
    substr5: GspDispatcherSubstring32
    unknown_varint6: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., substr4: _Optional[_Union[GspDispatcherSubstring31, _Mapping]] = ..., substr5: _Optional[_Union[GspDispatcherSubstring32, _Mapping]] = ..., unknown_varint6: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring31(_message.Message):
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

class GspDispatcherSubstring32(_message.Message):
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

class GspDispatcherLocation(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class GspDispatcherSubstring27(_message.Message):
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

class GspDispatcherSubstring28(_message.Message):
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

class GspDispatcherSubstring29(_message.Message):
    __slots__ = ("unknown_varint1", "unknown_varint2", "unknown_varint3")
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT3_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: int
    unknown_varint2: int
    unknown_varint3: int
    def __init__(self, unknown_varint1: _Optional[int] = ..., unknown_varint2: _Optional[int] = ..., unknown_varint3: _Optional[int] = ...) -> None: ...

class GspDispatcherSubstring30(_message.Message):
    __slots__ = ("unknown_varint1",)
    UNKNOWN_VARINT1_FIELD_NUMBER: _ClassVar[int]
    unknown_varint1: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unknown_varint1: _Optional[_Iterable[int]] = ...) -> None: ...

class GspDispatcherSubstring6(_message.Message):
    __slots__ = ("location", "timezone", "unknown_varint6", "substring7")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_VARINT6_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING7_FIELD_NUMBER: _ClassVar[int]
    location: GspDispatcherLocation
    timezone: GspDispatcherTimezone
    unknown_varint6: int
    substring7: GspDispatcherSubstring33
    def __init__(self, location: _Optional[_Union[GspDispatcherLocation, _Mapping]] = ..., timezone: _Optional[_Union[GspDispatcherTimezone, _Mapping]] = ..., unknown_varint6: _Optional[int] = ..., substring7: _Optional[_Union[GspDispatcherSubstring33, _Mapping]] = ...) -> None: ...

class GspDispatcherTimezone(_message.Message):
    __slots__ = ("timezone",)
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    def __init__(self, timezone: _Optional[str] = ...) -> None: ...

class GspDispatcherSubstring33(_message.Message):
    __slots__ = ("unknown_string1",)
    UNKNOWN_STRING1_FIELD_NUMBER: _ClassVar[int]
    unknown_string1: str
    def __init__(self, unknown_string1: _Optional[str] = ...) -> None: ...
