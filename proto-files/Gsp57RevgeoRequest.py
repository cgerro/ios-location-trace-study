# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_gsp57_revgeo.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1arequest_gsp57_revgeo.proto\x12\x14gsp57.revgeo.request\"\xd8\x02\n\x12Gsp57RevgeoRequest\x12\x42\n\x0cservice_data\x18\x01 \x01(\x0b\x32,.gsp57.revgeo.request.Gsp57RevgeoServiceData\x12\x42\n\x0c\x63ountry_data\x18\x02 \x01(\x0b\x32,.gsp57.revgeo.request.Gsp57RevgeoCountryData\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12\x39\n\x07subdata\x18\x05 \x03(\x0b\x32(.gsp57.revgeo.request.Gsp57RevgeoSubdata\x12\x17\n\x0funknown_varint7\x18\x07 \x01(\x05\x12?\n\nsubstring1\x18\x08 \x01(\x0b\x32+.gsp57.revgeo.request.Gsp57RevgeoSubstring1\x12\x0f\n\x07\x63ountry\x18\t \x01(\t\"\x95\x01\n\x12Gsp57RevgeoSubdata\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x05\x12@\n\x08subdata6\x18\x05 \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata6H\x00\x88\x01\x01\x42\x0b\n\t_subdata6\"\xe3\x02\n\x16Gsp57RevgeoServiceData\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x0funknown_string3\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x13\n\x0bios_version\x18\x05 \x01(\t\x12\x17\n\x0funknown_varint7\x18\x07 \x01(\x05\x12;\n\x08subdata1\x18\x08 \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata1\x12\x17\n\x0funknown_varint9\x18\t \x01(\x05\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\x12;\n\x08subdata2\x18\r \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata2\x12\n\n\x02os\x18\x0e \x01(\t\x12\x18\n\x10unknown_double18\x18\x12 \x01(\x01\"\xb4\x03\n\x16Gsp57RevgeoCountryData\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12\x17\n\x0funknown_string9\x18\t \x01(\t\x12\x18\n\x10unknown_varint10\x18\n \x01(\x05\x12\x18\n\x10unknown_varint11\x18\x0b \x01(\x05\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\x12\x18\n\x10unknown_varint16\x18\x10 \x01(\x05\x12\x18\n\x10unknown_varint19\x18\x13 \x01(\x05\x12;\n\x08subdata3\x18\x17 \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata3\x12\x18\n\x10unknown_varint26\x18\x1a \x01(\x05\x12\x18\n\x10unknown_string28\x18\x1c \x01(\t\x12\x0f\n\x07\x63ountry\x18\x1e \x01(\t\x12\x18\n\x10unknown_varint31\x18\x1f \x01(\x05\x12;\n\x08subdata4\x18\x64 \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata4\"G\n\x13Gsp57RevgeoSubdata1\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x03\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x03\"<\n\x13Gsp57RevgeoSubdata2\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"G\n\x13Gsp57RevgeoSubdata3\x12\x17\n\x0funknown_varint1\x18\x01 \x03(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"R\n\x13Gsp57RevgeoSubdata4\x12;\n\x08subdata5\x18\x05 \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata5\"G\n\x13Gsp57RevgeoSubdata5\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"\xa1\n\n\x13Gsp57RevgeoSubdata6\x12\x42\n\tsubdata16\x18\x07 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata16H\x00\x88\x01\x01\x12\x42\n\tsubdata15\x18\x0b \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata15H\x01\x88\x01\x01\x12@\n\x08subdata8\x18\x0f \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata8H\x02\x88\x01\x01\x12\x42\n\nsubdata8_1\x18\x17 \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata8H\x03\x88\x01\x01\x12@\n\x08subdata9\x18\x1a \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata9H\x04\x88\x01\x01\x12\x1d\n\x10unknown_string30\x18\x1e \x01(\tH\x05\x88\x01\x01\x12@\n\x08subdata7\x18\x1f \x01(\x0b\x32).gsp57.revgeo.request.Gsp57RevgeoSubdata7H\x06\x88\x01\x01\x12\x42\n\tsubdata12\x18$ \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata12H\x07\x88\x01\x01\x12\x42\n\tsubdata14\x18( \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata14H\x08\x88\x01\x01\x12\x1d\n\x10unknown_string42\x18* \x01(\tH\t\x88\x01\x01\x12\x1d\n\x10unknown_string44\x18, \x01(\tH\n\x88\x01\x01\x12\x1d\n\x10unknown_string55\x18\x37 \x01(\tH\x0b\x88\x01\x01\x12\x42\n\tsubdata11\x18\x39 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata11H\x0c\x88\x01\x01\x12\x1d\n\x10unknown_string59\x18; \x01(\tH\r\x88\x01\x01\x12\x42\n\tsubdata13\x18\x41 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata13H\x0e\x88\x01\x01\x12\x44\n\x0bsubdata10_1\x18\x42 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata10H\x0f\x88\x01\x01\x12\x1d\n\x10unknown_string71\x18G \x01(\tH\x10\x88\x01\x01\x12\x42\n\tsubdata18\x18T \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata18H\x11\x88\x01\x01\x42\x0c\n\n_subdata16B\x0c\n\n_subdata15B\x0b\n\t_subdata8B\r\n\x0b_subdata8_1B\x0b\n\t_subdata9B\x13\n\x11_unknown_string30B\x0b\n\t_subdata7B\x0c\n\n_subdata12B\x0c\n\n_subdata14B\x13\n\x11_unknown_string42B\x13\n\x11_unknown_string44B\x13\n\x11_unknown_string55B\x0c\n\n_subdata11B\x13\n\x11_unknown_string59B\x0c\n\n_subdata13B\x0e\n\x0c_subdata10_1B\x13\n\x11_unknown_string71B\x0c\n\n_subdata18\".\n\x13Gsp57RevgeoSubdata8\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\"&\n\x13Gsp57RevgeoSubdata7\x12\x0f\n\x07version\x18\x01 \x01(\t\"T\n\x13Gsp57RevgeoSubdata9\x12=\n\tsubdata10\x18\x01 \x03(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata10\"H\n\x14Gsp57RevgeoSubdata10\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"U\n\x14Gsp57RevgeoSubdata11\x12=\n\tsubdata10\x18\x01 \x03(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata10\"U\n\x14Gsp57RevgeoSubdata12\x12=\n\tsubdata10\x18\x01 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata10\"H\n\x14Gsp57RevgeoSubdata13\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\"/\n\x14Gsp57RevgeoSubdata14\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\"\xee\x01\n\x14Gsp57RevgeoSubdata15\x12=\n\tsubdata16\x18\x05 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata16\x12?\n\x0bsubdata16_1\x18\x06 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata16\x12=\n\tsubdata17\x18\x07 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata17\x12\x17\n\x0funknown_varint8\x18\x08 \x01(\x05\"\xb9\x01\n\x14Gsp57RevgeoSubdata16\x12=\n\tsubdata17\x18\x01 \x01(\x0b\x32*.gsp57.revgeo.request.Gsp57RevgeoSubdata17\x12\x1c\n\x0funknown_varint2\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0funknown_varint8\x18\x08 \x01(\x05H\x01\x88\x01\x01\x42\x12\n\x10_unknown_varint2B\x12\n\x10_unknown_varint8\"H\n\x14Gsp57RevgeoSubdata17\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"H\n\x14Gsp57RevgeoSubdata18\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x05\x12\x17\n\x0funknown_varint4\x18\x04 \x01(\x05\"X\n\x15Gsp57RevgeoSubstring1\x12?\n\nsubstring2\x18\x04 \x01(\x0b\x32+.gsp57.revgeo.request.Gsp57RevgeoSubstring2\"q\n\x15Gsp57RevgeoSubstring2\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x05\x12?\n\nsubstring3\x18\x04 \x01(\x0b\x32+.gsp57.revgeo.request.Gsp57RevgeoSubstring3\"\x8a\x01\n\x15Gsp57RevgeoSubstring3\x12?\n\nsubstring4\x18\x01 \x01(\x0b\x32+.gsp57.revgeo.request.Gsp57RevgeoSubstring4\x12\x17\n\x0funknown_double3\x18\x03 \x01(\x01\x12\x17\n\x0funknown_double5\x18\x05 \x01(\x01\"<\n\x15Gsp57RevgeoSubstring4\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_gsp57_revgeo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GSP57REVGEOREQUEST']._serialized_start=53
  _globals['_GSP57REVGEOREQUEST']._serialized_end=397
  _globals['_GSP57REVGEOSUBDATA']._serialized_start=400
  _globals['_GSP57REVGEOSUBDATA']._serialized_end=549
  _globals['_GSP57REVGEOSERVICEDATA']._serialized_start=552
  _globals['_GSP57REVGEOSERVICEDATA']._serialized_end=907
  _globals['_GSP57REVGEOCOUNTRYDATA']._serialized_start=910
  _globals['_GSP57REVGEOCOUNTRYDATA']._serialized_end=1346
  _globals['_GSP57REVGEOSUBDATA1']._serialized_start=1348
  _globals['_GSP57REVGEOSUBDATA1']._serialized_end=1419
  _globals['_GSP57REVGEOSUBDATA2']._serialized_start=1421
  _globals['_GSP57REVGEOSUBDATA2']._serialized_end=1481
  _globals['_GSP57REVGEOSUBDATA3']._serialized_start=1483
  _globals['_GSP57REVGEOSUBDATA3']._serialized_end=1554
  _globals['_GSP57REVGEOSUBDATA4']._serialized_start=1556
  _globals['_GSP57REVGEOSUBDATA4']._serialized_end=1638
  _globals['_GSP57REVGEOSUBDATA5']._serialized_start=1640
  _globals['_GSP57REVGEOSUBDATA5']._serialized_end=1711
  _globals['_GSP57REVGEOSUBDATA6']._serialized_start=1714
  _globals['_GSP57REVGEOSUBDATA6']._serialized_end=3027
  _globals['_GSP57REVGEOSUBDATA8']._serialized_start=3029
  _globals['_GSP57REVGEOSUBDATA8']._serialized_end=3075
  _globals['_GSP57REVGEOSUBDATA7']._serialized_start=3077
  _globals['_GSP57REVGEOSUBDATA7']._serialized_end=3115
  _globals['_GSP57REVGEOSUBDATA9']._serialized_start=3117
  _globals['_GSP57REVGEOSUBDATA9']._serialized_end=3201
  _globals['_GSP57REVGEOSUBDATA10']._serialized_start=3203
  _globals['_GSP57REVGEOSUBDATA10']._serialized_end=3275
  _globals['_GSP57REVGEOSUBDATA11']._serialized_start=3277
  _globals['_GSP57REVGEOSUBDATA11']._serialized_end=3362
  _globals['_GSP57REVGEOSUBDATA12']._serialized_start=3364
  _globals['_GSP57REVGEOSUBDATA12']._serialized_end=3449
  _globals['_GSP57REVGEOSUBDATA13']._serialized_start=3451
  _globals['_GSP57REVGEOSUBDATA13']._serialized_end=3523
  _globals['_GSP57REVGEOSUBDATA14']._serialized_start=3525
  _globals['_GSP57REVGEOSUBDATA14']._serialized_end=3572
  _globals['_GSP57REVGEOSUBDATA15']._serialized_start=3575
  _globals['_GSP57REVGEOSUBDATA15']._serialized_end=3813
  _globals['_GSP57REVGEOSUBDATA16']._serialized_start=3816
  _globals['_GSP57REVGEOSUBDATA16']._serialized_end=4001
  _globals['_GSP57REVGEOSUBDATA17']._serialized_start=4003
  _globals['_GSP57REVGEOSUBDATA17']._serialized_end=4075
  _globals['_GSP57REVGEOSUBDATA18']._serialized_start=4077
  _globals['_GSP57REVGEOSUBDATA18']._serialized_end=4149
  _globals['_GSP57REVGEOSUBSTRING1']._serialized_start=4151
  _globals['_GSP57REVGEOSUBSTRING1']._serialized_end=4239
  _globals['_GSP57REVGEOSUBSTRING2']._serialized_start=4241
  _globals['_GSP57REVGEOSUBSTRING2']._serialized_end=4354
  _globals['_GSP57REVGEOSUBSTRING3']._serialized_start=4357
  _globals['_GSP57REVGEOSUBSTRING3']._serialized_end=4495
  _globals['_GSP57REVGEOSUBSTRING4']._serialized_start=4497
  _globals['_GSP57REVGEOSUBSTRING4']._serialized_end=4557
# @@protoc_insertion_point(module_scope)
