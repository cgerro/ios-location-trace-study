# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_gsp57_revgeo.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bresponse_gsp57_revgeo.proto\x12\x15gsp57.revgeo.response\"\xa0\x02\n\x13Gsp57RevgeoResponse\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12\x35\n\x03str\x18\x03 \x01(\x0b\x32(.gsp57.revgeo.response.Gsp57RevgeoString\x12\x18\n\x10\x63ountry_language\x18\x05 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x06 \x01(\t\x12\x37\n\x04str1\x18\t \x01(\x0b\x32).gsp57.revgeo.response.Gsp57RevgeoString1\x12\x37\n\x04str2\x18\n \x01(\x0b\x32).gsp57.revgeo.response.Gsp57RevgeoString2\"P\n\x11Gsp57RevgeoString\x12;\n\x06substr\x18\x04 \x01(\x0b\x32+.gsp57.revgeo.response.Gsp57RevgeoSubstring\"-\n\x12Gsp57RevgeoString1\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\"m\n\x12Gsp57RevgeoString2\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12>\n\x07substr1\x18\x02 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring_a\"1\n\x14Gsp57RevgeoSubstring\x12\x19\n\x11unknown_varint100\x18\x64 \x01(\x05\"\x89\x01\n\x16Gsp57RevgeoSubstring_a\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12=\n\x07substr2\x18\x04 \x03(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring2\x12\x17\n\x0funknown_varint5\x18\x05 \x01(\x05\"\xe4\x03\n\x15Gsp57RevgeoSubstring2\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12\x1c\n\x0funknown_varint4\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0funknown_varint5\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12\x1c\n\x0funknown_varint6\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x42\n\x07substr3\x18\x08 \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring3H\x03\x88\x01\x01\x12\x15\n\rapple_service\x18\t \x03(\t\x12\x1d\n\x10unknown_varint10\x18\n \x01(\x05H\x04\x88\x01\x01\x12\x42\n\x07substr6\x18\x0b \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring6H\x05\x88\x01\x01\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\x42\x12\n\x10_unknown_varint4B\x12\n\x10_unknown_varint5B\x12\n\x10_unknown_varint6B\n\n\x08_substr3B\x13\n\x11_unknown_varint10B\n\n\x08_substr6\"\xd3\x06\n\x15Gsp57RevgeoSubstring3\x12\x42\n\x07substr4\x18\x01 \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring4H\x00\x88\x01\x01\x12\x44\n\x08substr33\x18\x02 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring33H\x01\x88\x01\x01\x12\x45\n\x08substr15\x18\x03 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_15H\x02\x88\x01\x01\x12\x45\n\x08substr14\x18\x04 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_14H\x03\x88\x01\x01\x12\x45\n\x08substr17\x18\x1f \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_17H\x04\x88\x01\x01\x12\x42\n\x07substr7\x18) \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring7H\x05\x88\x01\x01\x12\x45\n\x08substr13\x18, \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_13H\x06\x88\x01\x01\x12\x44\n\x08substr20\x18\x38 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring20H\x07\x88\x01\x01\x12\x44\n\x08substr23\x18; \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring23H\x08\x88\x01\x01\x12\x44\n\x08substr21\x18M \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring21H\t\x88\x01\x01\x42\n\n\x08_substr4B\x0b\n\t_substr33B\x0b\n\t_substr15B\x0b\n\t_substr14B\x0b\n\t_substr17B\n\n\x08_substr7B\x0b\n\t_substr13B\x0b\n\t_substr20B\x0b\n\t_substr23B\x0b\n\t_substr21\"\x89\x01\n\x15Gsp57RevgeoSubstring4\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12=\n\x07substr5\x18\n \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring5\x12\x18\n\x10unknown_varint19\x18\x13 \x01(\x05\"J\n\x15Gsp57RevgeoSubstring5\x12\x18\n\x10\x63ountry_language\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x64\x64ress_request\x18\x03 \x01(\t\"1\n\x15Gsp57RevgeoSubstring6\x12\x18\n\x10place_request_id\x18\x02 \x01(\t\"W\n\x15Gsp57RevgeoSubstring7\x12>\n\x07substr8\x18\x90N \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring8\"\xb1\x01\n\x15Gsp57RevgeoSubstring8\x12@\n\x08substr10\x18\x01 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_10\x12\x17\n\x0funknown_varint7\x18\x07 \x01(\x05\x12=\n\x07substr9\x18\x08 \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring9\"Y\n\x15Gsp57RevgeoSubstring9\x12@\n\x08substr11\x18\x04 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_11\"*\n\x17Gsp57RevgeoSubstring_10\x12\x0f\n\x07service\x18\x01 \x01(\t\"t\n\x17Gsp57RevgeoSubstring_11\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x05\x12@\n\x08substr12\x18\x04 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_12\"\x93\x01\n\x17Gsp57RevgeoSubstring_12\x12\x46\n\x0bloc_request\x18\x01 \x01(\x0b\x32\x31.gsp57.revgeo.response.Gsp57RevgeoLocationRequest\x12\x17\n\x0funknown_double3\x18\x03 \x01(\x01\x12\x17\n\x0funknown_double5\x18\x05 \x01(\x01\"G\n\x1aGsp57RevgeoLocationRequest\x12\x13\n\x0blat_request\x18\x01 \x01(\x01\x12\x14\n\x0clong_request\x18\x02 \x01(\x01\"2\n\x17Gsp57RevgeoSubstring_13\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\"\x9a\x01\n\x17Gsp57RevgeoSubstring_14\x12>\n\tlocations\x18\x01 \x01(\x0b\x32+.gsp57.revgeo.response.Gsp57RevgeoLocations\x12?\n\nlocations1\x18\x02 \x01(\x0b\x32+.gsp57.revgeo.response.Gsp57RevgeoLocations\"i\n\x14Gsp57RevgeoLocations\x12\x0c\n\x04lat1\x18\x05 \x01(\x01\x12\r\n\x05long1\x18\x06 \x01(\x01\x12\x0c\n\x04lat2\x18\x07 \x01(\x01\x12\r\n\x05long2\x18\x08 \x01(\x01\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\"[\n\x17Gsp57RevgeoSubstring_15\x12@\n\x08substr16\x18\x01 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_16\"\xc6\x01\n\x17Gsp57RevgeoSubstring_16\x12\x46\n\x0bloc_request\x18\x01 \x01(\x0b\x32\x31.gsp57.revgeo.response.Gsp57RevgeoLocationRequest\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x05\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\x12\x18\n\x10unknown_varint13\x18\r \x01(\x05\"[\n\x17Gsp57RevgeoSubstring_17\x12@\n\x08substr18\x18\x01 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_18\"\x84\x02\n\x17Gsp57RevgeoSubstring_18\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\t\x12@\n\x08substr19\x18\x03 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoSubstring_19\x12\x43\n\x0cservice_info\x18\x04 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoServiceInfo\x12\x38\n\x06street\x18\x65 \x01(\x0b\x32(.gsp57.revgeo.response.Gsp57RevgeoStreet\"b\n\x17Gsp57RevgeoSubstring_19\x12\x18\n\x10\x63ountry_language\x18\x01 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x17\n\x0funknown_string3\x18\x03 \x01(\t\"e\n\x16Gsp57RevgeoServiceInfo\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x03\x12\x10\n\x08\x66unction\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"\xe2\x02\n\x11Gsp57RevgeoStreet\x12\x15\n\rstreet_number\x18\x01 \x01(\t\x12:\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32).gsp57.revgeo.response.Gsp57RevgeoAddress\x12\x16\n\x0estreet_strange\x18\x04 \x01(\t\x12P\n\x13\x61\x64\x64ress_info_second\x18\x05 \x01(\x0b\x32\x33.gsp57.revgeo.response.Gsp57RevgeoAddressInfoSecond\x12@\n\nsubstring6\x18\x07 \x01(\x0b\x32,.gsp57.revgeo.response.Gsp57RevgeoSubstring6\x12N\n\x12\x61\x64\x64ress_info_third\x18\x64 \x01(\x0b\x32\x32.gsp57.revgeo.response.Gsp57RevgeoAddressInfoThird\"z\n\x12Gsp57RevgeoAddress\x12\x14\n\x0c\x61\x64\x64ress_data\x18\x0b \x03(\t\x12N\n\x12\x61\x64\x64ress_info_first\x18\x0f \x01(\x0b\x32\x32.gsp57.revgeo.response.Gsp57RevgeoAddressInfoFirst\"\xfb\x01\n\x1bGsp57RevgeoAddressInfoFirst\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x12\n\ndepartment\x18\x04 \x01(\t\x12\r\n\x05\x63ity1\x18\x05 \x01(\t\x12\r\n\x05\x63ity2\x18\x06 \x01(\t\x12\x13\n\x0bpostal_code\x18\x07 \x01(\t\x12\x10\n\x08quartier\x18\x08 \x01(\t\x12\x0e\n\x06street\x18\n \x01(\t\x12\x0e\n\x06number\x18\x0b \x01(\t\x12\x15\n\rstreet_number\x18\x0c \x01(\t\x12\x15\n\rdistrict_info\x18\x11 \x03(\t\"\x86\x02\n\x1cGsp57RevgeoAddressInfoSecond\x12\x10\n\x08\x63ountry1\x18\x01 \x01(\t\x12\x10\n\x08\x63ountry2\x18\x02 \x01(\t\x12\x0f\n\x07region1\x18\x03 \x01(\t\x12\x0f\n\x07region2\x18\x04 \x01(\t\x12\r\n\x05\x63ity1\x18\x05 \x01(\t\x12\r\n\x05\x63ity2\x18\x06 \x01(\t\x12\x10\n\x08\x64istrict\x18\x08 \x01(\t\x12\x0e\n\x06street\x18\n \x01(\t\x12\x1c\n\x0fstreet_strange1\x18\x0b \x01(\tH\x00\x88\x01\x01\x12\x17\n\x0fstreet_strange2\x18\x0c \x01(\t\x12\x15\n\rdistrict_info\x18\x11 \x03(\tB\x12\n\x10_street_strange1\"\\\n\x1bGsp57RevgeoAddressInfoThird\x12\r\n\x05\x63ity1\x18\x01 \x01(\t\x12\x0e\n\x06street\x18\n \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\r\n\x05\x63ity2\x18\x06 \x01(\t\"x\n\x16Gsp57RevgeoSubstring20\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x45\n\rlocation_info\x18\x02 \x01(\x0b\x32..gsp57.revgeo.response.Gsp57RevgeoLocationInfo\"\x82\x01\n\x17Gsp57RevgeoLocationInfo\x12\x15\n\rstreet_number\x18\x01 \x01(\t\x12\x10\n\x08\x64istrict\x18\x02 \x01(\t\x12\x17\n\x0funknown_double3\x18\x03 \x01(\x01\x12\x17\n\x0funknown_double4\x18\x04 \x01(\x01\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\"\x8b\x01\n\x16Gsp57RevgeoSubstring21\x12?\n\x08substr22\x18\x01 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring22\x12\x14\n\x0c\x63ountry_code\x18\x02 \x01(\t\x12\x1a\n\x12\x63ountry_state_code\x18\x03 \x01(\t\"H\n\x16Gsp57RevgeoSubstring22\x12\x16\n\x0eunknown_float1\x18\x01 \x01(\x02\x12\x16\n\x0eunknown_float2\x18\x02 \x01(\x02\"k\n\x16Gsp57RevgeoSubstring23\x12\x44\n\x08substr24\x18\x04 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring24H\x00\x88\x01\x01\x42\x0b\n\t_substr24\"\xdf\x01\n\x16Gsp57RevgeoSubstring24\x12?\n\x08substr25\x18\x02 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring25\x12\x46\n\x0bloc_request\x18\x06 \x01(\x0b\x32\x31.gsp57.revgeo.response.Gsp57RevgeoLocationRequest\x12<\n\x08location\x18\x07 \x01(\x0b\x32*.gsp57.revgeo.response.Gsp57RevgeoLocation\"\xe6\x03\n\x16Gsp57RevgeoSubstring25\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x03\x12?\n\x08substr26\x18\x02 \x03(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring26\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\x12\x17\n\x0funknown_varint5\x18\x05 \x01(\x03\x12<\n\x08location\x18\x06 \x01(\x0b\x32*.gsp57.revgeo.response.Gsp57RevgeoLocation\x12?\n\x08substr29\x18\x08 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring29\x12?\n\x08substr30\x18\n \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring30\x12?\n\x08substr31\x18\x0b \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring31\x12?\n\x08substr32\x18\x0c \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring32\"\xcc\x01\n\x16Gsp57RevgeoSubstring26\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12?\n\x08substr27\x18\x04 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring27\x12?\n\x08substr28\x18\x05 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring28\x12\x17\n\x0funknown_varint6\x18\x06 \x01(\x05\"\x93\x02\n\x16Gsp57RevgeoSubstring27\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_double2\x18\x02 \x01(\x01\x12\x17\n\x0funknown_double3\x18\x03 \x01(\x01\x12\x17\n\x0funknown_double4\x18\x04 \x01(\x01\x12\x17\n\x0funknown_double5\x18\x05 \x01(\x01\x12\x17\n\x0funknown_double6\x18\x06 \x01(\x01\x12\x17\n\x0funknown_double7\x18\x07 \x01(\x01\x12\x17\n\x0funknown_double8\x18\x08 \x01(\x01\x12\x17\n\x0funknown_double9\x18\t \x01(\x01\x12\x18\n\x10unknown_double10\x18\n \x01(\x01\"\xae\x01\n\x16Gsp57RevgeoSubstring28\x12\x17\n\x0funknown_double1\x18\x01 \x01(\x01\x12\x17\n\x0funknown_double2\x18\x02 \x01(\x01\x12\x17\n\x0funknown_double3\x18\x03 \x01(\x01\x12\x17\n\x0funknown_double4\x18\x04 \x01(\x01\x12\x17\n\x0funknown_double5\x18\x05 \x01(\x01\x12\x17\n\x0funknown_double6\x18\x06 \x01(\x01\"T\n\x13Gsp57RevgeoLocation\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0c\n\x04long\x18\x02 \x01(\x01\x12\x15\n\x08\x61ltitude\x18\x03 \x01(\x01H\x00\x88\x01\x01\x42\x0b\n\t_altitude\"\xfc\x01\n\x16Gsp57RevgeoSubstring29\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x03\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\x12\x17\n\x0funknown_varint5\x18\x05 \x01(\x05\x12\x17\n\x0funknown_varint6\x18\x06 \x01(\x05\x12\x17\n\x0funknown_varint9\x18\t \x01(\x05\x12\x18\n\x10unknown_varint10\x18\n \x01(\x05\x12\x18\n\x10unknown_varint11\x18\x0b \x01(\x05\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\"\xae\x01\n\x16Gsp57RevgeoSubstring30\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x03\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\x12\x17\n\x0funknown_varint5\x18\x05 \x01(\x05\x12\x17\n\x0funknown_varint6\x18\x06 \x01(\x05\"c\n\x16Gsp57RevgeoSubstring31\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x03\"1\n\x16Gsp57RevgeoSubstring32\x12\x17\n\x0funknown_varint1\x18\x01 \x03(\x05\"\xf1\x01\n\x16Gsp57RevgeoSubstring33\x12<\n\x08location\x18\x01 \x01(\x0b\x32*.gsp57.revgeo.response.Gsp57RevgeoLocation\x12<\n\x08timezone\x18\x04 \x01(\x0b\x32*.gsp57.revgeo.response.Gsp57RevgeoTimezone\x12\x17\n\x0funknown_varint6\x18\x06 \x01(\x05\x12\x42\n\x0bsubstring34\x18\x07 \x01(\x0b\x32-.gsp57.revgeo.response.Gsp57RevgeoSubstring34\"\'\n\x13Gsp57RevgeoTimezone\x12\x10\n\x08timezone\x18\x01 \x01(\t\"1\n\x16Gsp57RevgeoSubstring34\x12\x17\n\x0funknown_string1\x18\x01 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_gsp57_revgeo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GSP57REVGEORESPONSE']._serialized_start=55
  _globals['_GSP57REVGEORESPONSE']._serialized_end=343
  _globals['_GSP57REVGEOSTRING']._serialized_start=345
  _globals['_GSP57REVGEOSTRING']._serialized_end=425
  _globals['_GSP57REVGEOSTRING1']._serialized_start=427
  _globals['_GSP57REVGEOSTRING1']._serialized_end=472
  _globals['_GSP57REVGEOSTRING2']._serialized_start=474
  _globals['_GSP57REVGEOSTRING2']._serialized_end=583
  _globals['_GSP57REVGEOSUBSTRING']._serialized_start=585
  _globals['_GSP57REVGEOSUBSTRING']._serialized_end=634
  _globals['_GSP57REVGEOSUBSTRING_A']._serialized_start=637
  _globals['_GSP57REVGEOSUBSTRING_A']._serialized_end=774
  _globals['_GSP57REVGEOSUBSTRING2']._serialized_start=777
  _globals['_GSP57REVGEOSUBSTRING2']._serialized_end=1261
  _globals['_GSP57REVGEOSUBSTRING3']._serialized_start=1264
  _globals['_GSP57REVGEOSUBSTRING3']._serialized_end=2115
  _globals['_GSP57REVGEOSUBSTRING4']._serialized_start=2118
  _globals['_GSP57REVGEOSUBSTRING4']._serialized_end=2255
  _globals['_GSP57REVGEOSUBSTRING5']._serialized_start=2257
  _globals['_GSP57REVGEOSUBSTRING5']._serialized_end=2331
  _globals['_GSP57REVGEOSUBSTRING6']._serialized_start=2333
  _globals['_GSP57REVGEOSUBSTRING6']._serialized_end=2382
  _globals['_GSP57REVGEOSUBSTRING7']._serialized_start=2384
  _globals['_GSP57REVGEOSUBSTRING7']._serialized_end=2471
  _globals['_GSP57REVGEOSUBSTRING8']._serialized_start=2474
  _globals['_GSP57REVGEOSUBSTRING8']._serialized_end=2651
  _globals['_GSP57REVGEOSUBSTRING9']._serialized_start=2653
  _globals['_GSP57REVGEOSUBSTRING9']._serialized_end=2742
  _globals['_GSP57REVGEOSUBSTRING_10']._serialized_start=2744
  _globals['_GSP57REVGEOSUBSTRING_10']._serialized_end=2786
  _globals['_GSP57REVGEOSUBSTRING_11']._serialized_start=2788
  _globals['_GSP57REVGEOSUBSTRING_11']._serialized_end=2904
  _globals['_GSP57REVGEOSUBSTRING_12']._serialized_start=2907
  _globals['_GSP57REVGEOSUBSTRING_12']._serialized_end=3054
  _globals['_GSP57REVGEOLOCATIONREQUEST']._serialized_start=3056
  _globals['_GSP57REVGEOLOCATIONREQUEST']._serialized_end=3127
  _globals['_GSP57REVGEOSUBSTRING_13']._serialized_start=3129
  _globals['_GSP57REVGEOSUBSTRING_13']._serialized_end=3179
  _globals['_GSP57REVGEOSUBSTRING_14']._serialized_start=3182
  _globals['_GSP57REVGEOSUBSTRING_14']._serialized_end=3336
  _globals['_GSP57REVGEOLOCATIONS']._serialized_start=3338
  _globals['_GSP57REVGEOLOCATIONS']._serialized_end=3443
  _globals['_GSP57REVGEOSUBSTRING_15']._serialized_start=3445
  _globals['_GSP57REVGEOSUBSTRING_15']._serialized_end=3536
  _globals['_GSP57REVGEOSUBSTRING_16']._serialized_start=3539
  _globals['_GSP57REVGEOSUBSTRING_16']._serialized_end=3737
  _globals['_GSP57REVGEOSUBSTRING_17']._serialized_start=3739
  _globals['_GSP57REVGEOSUBSTRING_17']._serialized_end=3830
  _globals['_GSP57REVGEOSUBSTRING_18']._serialized_start=3833
  _globals['_GSP57REVGEOSUBSTRING_18']._serialized_end=4093
  _globals['_GSP57REVGEOSUBSTRING_19']._serialized_start=4095
  _globals['_GSP57REVGEOSUBSTRING_19']._serialized_end=4193
  _globals['_GSP57REVGEOSERVICEINFO']._serialized_start=4195
  _globals['_GSP57REVGEOSERVICEINFO']._serialized_end=4296
  _globals['_GSP57REVGEOSTREET']._serialized_start=4299
  _globals['_GSP57REVGEOSTREET']._serialized_end=4653
  _globals['_GSP57REVGEOADDRESS']._serialized_start=4655
  _globals['_GSP57REVGEOADDRESS']._serialized_end=4777
  _globals['_GSP57REVGEOADDRESSINFOFIRST']._serialized_start=4780
  _globals['_GSP57REVGEOADDRESSINFOFIRST']._serialized_end=5031
  _globals['_GSP57REVGEOADDRESSINFOSECOND']._serialized_start=5034
  _globals['_GSP57REVGEOADDRESSINFOSECOND']._serialized_end=5296
  _globals['_GSP57REVGEOADDRESSINFOTHIRD']._serialized_start=5298
  _globals['_GSP57REVGEOADDRESSINFOTHIRD']._serialized_end=5390
  _globals['_GSP57REVGEOSUBSTRING20']._serialized_start=5392
  _globals['_GSP57REVGEOSUBSTRING20']._serialized_end=5512
  _globals['_GSP57REVGEOLOCATIONINFO']._serialized_start=5515
  _globals['_GSP57REVGEOLOCATIONINFO']._serialized_end=5645
  _globals['_GSP57REVGEOSUBSTRING21']._serialized_start=5648
  _globals['_GSP57REVGEOSUBSTRING21']._serialized_end=5787
  _globals['_GSP57REVGEOSUBSTRING22']._serialized_start=5789
  _globals['_GSP57REVGEOSUBSTRING22']._serialized_end=5861
  _globals['_GSP57REVGEOSUBSTRING23']._serialized_start=5863
  _globals['_GSP57REVGEOSUBSTRING23']._serialized_end=5970
  _globals['_GSP57REVGEOSUBSTRING24']._serialized_start=5973
  _globals['_GSP57REVGEOSUBSTRING24']._serialized_end=6196
  _globals['_GSP57REVGEOSUBSTRING25']._serialized_start=6199
  _globals['_GSP57REVGEOSUBSTRING25']._serialized_end=6685
  _globals['_GSP57REVGEOSUBSTRING26']._serialized_start=6688
  _globals['_GSP57REVGEOSUBSTRING26']._serialized_end=6892
  _globals['_GSP57REVGEOSUBSTRING27']._serialized_start=6895
  _globals['_GSP57REVGEOSUBSTRING27']._serialized_end=7170
  _globals['_GSP57REVGEOSUBSTRING28']._serialized_start=7173
  _globals['_GSP57REVGEOSUBSTRING28']._serialized_end=7347
  _globals['_GSP57REVGEOLOCATION']._serialized_start=7349
  _globals['_GSP57REVGEOLOCATION']._serialized_end=7433
  _globals['_GSP57REVGEOSUBSTRING29']._serialized_start=7436
  _globals['_GSP57REVGEOSUBSTRING29']._serialized_end=7688
  _globals['_GSP57REVGEOSUBSTRING30']._serialized_start=7691
  _globals['_GSP57REVGEOSUBSTRING30']._serialized_end=7865
  _globals['_GSP57REVGEOSUBSTRING31']._serialized_start=7867
  _globals['_GSP57REVGEOSUBSTRING31']._serialized_end=7966
  _globals['_GSP57REVGEOSUBSTRING32']._serialized_start=7968
  _globals['_GSP57REVGEOSUBSTRING32']._serialized_end=8017
  _globals['_GSP57REVGEOSUBSTRING33']._serialized_start=8020
  _globals['_GSP57REVGEOSUBSTRING33']._serialized_end=8261
  _globals['_GSP57REVGEOTIMEZONE']._serialized_start=8263
  _globals['_GSP57REVGEOTIMEZONE']._serialized_end=8302
  _globals['_GSP57REVGEOSUBSTRING34']._serialized_start=8304
  _globals['_GSP57REVGEOSUBSTRING34']._serialized_end=8353
# @@protoc_insertion_point(module_scope)
