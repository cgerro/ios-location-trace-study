# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_wloc.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13response_wloc.proto\x12\rwloc.response\"\xc8\x01\n\x0cWlocResponse\x12?\n\x12\x63\x65llular_response1\x18\x01 \x03(\x0b\x32#.wloc.response.WlocCellularResponse\x12\x36\n\rwifi_response\x18\x02 \x03(\x0b\x32\x1f.wloc.response.WlocWifiResponse\x12?\n\x12\x63\x65llular_response2\x18\x16 \x03(\x0b\x32#.wloc.response.WlocCellularResponse\"\x89\x01\n\x10WlocWifiResponse\x12\r\n\x05\x62ssid\x18\x01 \x01(\t\x12\x32\n\rlocation_info\x18\x02 \x01(\x0b\x32\x1b.wloc.response.WlocLocation\x12\x18\n\x10unknown_varint21\x18\x15 \x01(\x05\x12\x18\n\x10unknown_varint22\x18\x16 \x01(\x05\"\x97\x02\n\x0cWlocLocation\x12\x10\n\x08latitude\x18\x01 \x01(\x03\x12\x11\n\tlongitude\x18\x02 \x01(\x03\x12\x1b\n\x13horizontal_accuracy\x18\x03 \x01(\x03\x12\x1c\n\x0funknown_varint4\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x08\x61ltitude\x18\x05 \x01(\x03\x12\x19\n\x11vertical_accuracy\x18\x06 \x01(\x03\x12\x1d\n\x10unknown_varint11\x18\x0b \x01(\x03H\x01\x88\x01\x01\x12\x1d\n\x10unknown_varint12\x18\x0c \x01(\x03H\x02\x88\x01\x01\x42\x12\n\x10_unknown_varint4B\x13\n\x11_unknown_varint11B\x13\n\x11_unknown_varint12\"\xb6\x01\n\x14WlocCellularResponse\x12\x0b\n\x03mcc\x18\x01 \x01(\x05\x12\x0b\n\x03mnc\x18\x02 \x01(\x05\x12\x0f\n\x07\x63\x65ll_id\x18\x03 \x01(\x05\x12\x0b\n\x03lac\x18\x04 \x01(\x05\x12\x34\n\x0c\x63\x65ll_details\x18\x05 \x01(\x0b\x32\x1e.wloc.response.WlocCellDetails\x12\x17\n\x0funknown_varint6\x18\x06 \x01(\x05\x12\x17\n\x0funknown_varint7\x18\x07 \x01(\x05\"\x99\x01\n\x0fWlocCellDetails\x12\x10\n\x08latitude\x18\x01 \x01(\x03\x12\x11\n\tlongitude\x18\x02 \x01(\x03\x12\x1b\n\x13horizontal_accuracy\x18\x03 \x01(\x03\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x05\x12\x18\n\x10unknown_varint11\x18\x0b \x01(\x05\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_wloc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WLOCRESPONSE']._serialized_start=39
  _globals['_WLOCRESPONSE']._serialized_end=239
  _globals['_WLOCWIFIRESPONSE']._serialized_start=242
  _globals['_WLOCWIFIRESPONSE']._serialized_end=379
  _globals['_WLOCLOCATION']._serialized_start=382
  _globals['_WLOCLOCATION']._serialized_end=661
  _globals['_WLOCCELLULARRESPONSE']._serialized_start=664
  _globals['_WLOCCELLULARRESPONSE']._serialized_end=846
  _globals['_WLOCCELLDETAILS']._serialized_start=849
  _globals['_WLOCCELLDETAILS']._serialized_end=1002
# @@protoc_insertion_point(module_scope)