# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_wloc.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12request_wloc.proto\x12\x0cwloc.request\"\xed\x02\n\x0bWlocRequest\x12<\n\x11\x63\x65llular_request1\x18\x01 \x03(\x0b\x32!.wloc.request.WlocCellularRequest\x12\x33\n\x0cwifi_request\x18\x02 \x03(\x0b\x32\x1d.wloc.request.WlocWifiRequest\x12<\n\x11\x63\x65llular_request2\x18\x19 \x03(\x0b\x32!.wloc.request.WlocCellularRequest\x12\x16\n\tinfo_mask\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07\x63hannel\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x18\n\x10unknown_varint31\x18\x1f \x01(\x05\x12\x18\n\x10unknown_varint32\x18  \x01(\x05\x12\x31\n\x0b\x63lient_info\x18! \x01(\x0b\x32\x1c.wloc.request.WlocClientInfoB\x0c\n\n_info_maskB\n\n\x08_channel\" \n\x0fWlocWifiRequest\x12\r\n\x05\x62ssid\x18\x01 \x01(\t\"M\n\x13WlocCellularRequest\x12\x0b\n\x03mcc\x18\x01 \x01(\x05\x12\x0b\n\x03mnc\x18\x02 \x01(\x05\x12\x0f\n\x07\x63\x65ll_id\x18\x03 \x01(\x05\x12\x0b\n\x03lac\x18\x04 \x01(\x05\":\n\x0eWlocClientInfo\x12\x12\n\nos_version\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x02 \x01(\t\"\xe9\x01\n\x12StrangeWlocRequest\x12\x10\n\x08latitude\x18\x01 \x01(\x03\x12\x11\n\tlongitude\x18\x02 \x01(\x03\x12\x16\n\tinfo_mask\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07\x63hannel\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x18\n\x10unknown_varint31\x18\x1f \x01(\x05\x12\x18\n\x10unknown_varint32\x18  \x01(\x05\x12\x18\n\x10unknown_varint33\x18! \x01(\x05\x12\x18\n\x10unknown_varint34\x18\" \x01(\x05\x42\x0c\n\n_info_maskB\n\n\x08_channelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_wloc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WLOCREQUEST']._serialized_start=37
  _globals['_WLOCREQUEST']._serialized_end=402
  _globals['_WLOCWIFIREQUEST']._serialized_start=404
  _globals['_WLOCWIFIREQUEST']._serialized_end=436
  _globals['_WLOCCELLULARREQUEST']._serialized_start=438
  _globals['_WLOCCELLULARREQUEST']._serialized_end=515
  _globals['_WLOCCLIENTINFO']._serialized_start=517
  _globals['_WLOCCLIENTINFO']._serialized_end=575
  _globals['_STRANGEWLOCREQUEST']._serialized_start=578
  _globals['_STRANGEWLOCREQUEST']._serialized_end=811
# @@protoc_insertion_point(module_scope)