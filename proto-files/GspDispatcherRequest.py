# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_gsp_dispatcher.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1crequest_gsp_dispatcher.proto\x12\x16gsp.dispatcher.request\"\xea\x02\n\x14GspDispatcherRequest\x12\x46\n\x0cservice_data\x18\x01 \x01(\x0b\x32\x30.gsp.dispatcher.request.GspDispatcherServiceData\x12\x46\n\x0c\x63ountry_data\x18\x02 \x01(\x0b\x32\x30.gsp.dispatcher.request.GspDispatcherCountryData\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12=\n\x07subdata\x18\x05 \x03(\x0b\x32,.gsp.dispatcher.request.GspDispatcherSubdata\x12\x17\n\x0funknown_varint7\x18\x07 \x01(\x05\x12\x43\n\nsubstring1\x18\x08 \x01(\x0b\x32/.gsp.dispatcher.request.GspDispatcherSubstring1\x12\x0f\n\x07\x63ountry\x18\t \x01(\t\"\x9b\x01\n\x14GspDispatcherSubdata\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint3\x18\x03 \x01(\x05\x12\x44\n\x08subdata6\x18\x05 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata6H\x00\x88\x01\x01\x42\x0b\n\t_subdata6\"\xe2\n\n\x15GspDispatcherSubdata6\x12\x46\n\nsubdata8_4\x18\x07 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata8H\x00\x88\x01\x01\x12\x46\n\nsubdata8_5\x18\x0b \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata8H\x01\x88\x01\x01\x12\x46\n\nsubdata7_1\x18\x0f \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata7H\x02\x88\x01\x01\x12\x46\n\nsubdata7_4\x18\x17 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata7H\x03\x88\x01\x01\x12\x46\n\nsubdata8_1\x18\x1a \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata8H\x04\x88\x01\x01\x12\x1d\n\x10unknown_string30\x18\x1e \x01(\tH\x05\x88\x01\x01\x12\x46\n\tsubdata10\x18\x1f \x01(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata10H\x06\x88\x01\x01\x12\x46\n\nsubdata8_3\x18$ \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata8H\x07\x88\x01\x01\x12\x46\n\nsubdata7_3\x18( \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata7H\x08\x88\x01\x01\x12\x1d\n\x10unknown_string42\x18* \x01(\tH\t\x88\x01\x01\x12\x1d\n\x10unknown_string55\x18\x37 \x01(\tH\n\x88\x01\x01\x12\x46\n\nsubdata8_2\x18\x39 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata8H\x0b\x88\x01\x01\x12\x1d\n\x10unknown_string59\x18; \x01(\tH\x0c\x88\x01\x01\x12\x46\n\nsubdata7_2\x18\x41 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata7H\r\x88\x01\x01\x12\x46\n\nsubdata7_6\x18\x42 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata7H\x0e\x88\x01\x01\x12\x1d\n\x10unknown_string71\x18G \x01(\tH\x0f\x88\x01\x01\x12\x46\n\nsubdata7_5\x18T \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata7H\x10\x88\x01\x01\x12\x1d\n\x10unknown_string44\x18, \x01(\tH\x11\x88\x01\x01\x42\r\n\x0b_subdata8_4B\r\n\x0b_subdata8_5B\r\n\x0b_subdata7_1B\r\n\x0b_subdata7_4B\r\n\x0b_subdata8_1B\x13\n\x11_unknown_string30B\x0c\n\n_subdata10B\r\n\x0b_subdata8_3B\r\n\x0b_subdata7_3B\x13\n\x11_unknown_string42B\x13\n\x11_unknown_string55B\r\n\x0b_subdata8_2B\x13\n\x11_unknown_string59B\r\n\x0b_subdata7_2B\r\n\x0b_subdata7_6B\x13\n\x11_unknown_string71B\r\n\x0b_subdata7_5B\x13\n\x11_unknown_string44\"\xdf\x01\n\x15GspDispatcherSubdata7\x12\x1c\n\x0funknown_varint1\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0funknown_varint2\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x1c\n\x0funknown_varint3\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x1c\n\x0funknown_varint4\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x12\n\x10_unknown_varint1B\x12\n\x10_unknown_varint2B\x12\n\x10_unknown_varint3B\x12\n\x10_unknown_varint4\"\xcc\x03\n\x15GspDispatcherSubdata8\x12\x41\n\tsubdata12\x18\x01 \x03(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata12\x12\x1c\n\x0funknown_varint2\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12H\n\x0bsubdata13_1\x18\x05 \x01(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata13H\x01\x88\x01\x01\x12H\n\x0bsubdata13_2\x18\x06 \x01(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata13H\x02\x88\x01\x01\x12H\n\x0bsubdata13_3\x18\x07 \x01(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata13H\x03\x88\x01\x01\x12\x1c\n\x0funknown_varint8\x18\x08 \x01(\x05H\x04\x88\x01\x01\x42\x12\n\x10_unknown_varint2B\x0e\n\x0c_subdata13_1B\x0e\n\x0c_subdata13_2B\x0e\n\x0c_subdata13_3B\x12\n\x10_unknown_varint8\")\n\x16GspDispatcherSubdata10\x12\x0f\n\x07version\x18\x01 \x01(\t\"1\n\x16GspDispatcherSubdata11\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\"J\n\x16GspDispatcherSubdata12\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"\xa0\x01\n\x16GspDispatcherSubdata13\x12\x46\n\tsubdata14\x18\x01 \x01(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata14H\x00\x88\x01\x01\x12\x1c\n\x0funknown_varint2\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_subdata14B\x12\n\x10_unknown_varint2\"J\n\x16GspDispatcherSubdata14\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x03\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"\xb0\x03\n\x18GspDispatcherServiceData\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x0funknown_string3\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x13\n\x0bios_version\x18\x05 \x01(\t\x12\x17\n\x0funknown_varint7\x18\x07 \x01(\x05\x12?\n\x08subdata1\x18\x08 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata1\x12\x17\n\x0funknown_varint9\x18\t \x01(\x05\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\x12?\n\x08subdata2\x18\r \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata2\x12\n\n\x02os\x18\x0e \x01(\t\x12\x41\n\tsubdata17\x18\x11 \x01(\x0b\x32..gsp.dispatcher.request.GspDispatcherSubdata15\x12\x18\n\x10unknown_double18\x18\x12 \x01(\x01\"I\n\x15GspDispatcherSubdata1\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x03\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x03\">\n\x15GspDispatcherSubdata2\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\xc7\x03\n\x18GspDispatcherCountryData\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x18\n\x10\x63ountry_language\x18\x03 \x01(\t\x12\x17\n\x0funknown_string9\x18\t \x01(\t\x12\x18\n\x10unknown_varint10\x18\n \x01(\x05\x12\x18\n\x10unknown_varint11\x18\x0b \x01(\x05\x12\x18\n\x10unknown_varint12\x18\x0c \x01(\x05\x12\x18\n\x10unknown_varint16\x18\x10 \x01(\x05\x12\x18\n\x10unknown_varint19\x18\x13 \x01(\x05\x12?\n\x08subdata3\x18\x17 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata3\x12\x18\n\x10unknown_varint26\x18\x1a \x01(\x05\x12\x18\n\x10unknown_string28\x18\x1c \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x1e \x01(\t\x12\x18\n\x10unknown_varint31\x18\x1f \x01(\x05\x12?\n\x08subdata4\x18\x64 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata4\"I\n\x15GspDispatcherSubdata3\x12\x17\n\x0funknown_varint1\x18\x01 \x03(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"X\n\x15GspDispatcherSubdata4\x12?\n\x08subdata5\x18\x05 \x01(\x0b\x32-.gsp.dispatcher.request.GspDispatcherSubdata5\"I\n\x15GspDispatcherSubdata5\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\"^\n\x17GspDispatcherSubstring1\x12\x43\n\nsubstring2\x18\x02 \x01(\x0b\x32/.gsp.dispatcher.request.GspDispatcherSubstring2\"q\n\x17GspDispatcherSubstring2\x12\x17\n\x0funknown_varint2\x18\x02 \x01(\x05\x12=\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32,.gsp.dispatcher.request.GspDispatcherAddress\"s\n\x14GspDispatcherAddress\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x06 \x01(\t\x12\x13\n\x0bpostal_code\x18\x07 \x01(\t\x12\x15\n\rstreet_number\x18\n \x01(\t\"I\n\x16GspDispatcherSubdata15\x12\x17\n\x0funknown_varint1\x18\x01 \x01(\x05\x12\x16\n\x0eunknown_float2\x18\x02 \x01(\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_gsp_dispatcher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GSPDISPATCHERREQUEST']._serialized_start=57
  _globals['_GSPDISPATCHERREQUEST']._serialized_end=419
  _globals['_GSPDISPATCHERSUBDATA']._serialized_start=422
  _globals['_GSPDISPATCHERSUBDATA']._serialized_end=577
  _globals['_GSPDISPATCHERSUBDATA6']._serialized_start=580
  _globals['_GSPDISPATCHERSUBDATA6']._serialized_end=1958
  _globals['_GSPDISPATCHERSUBDATA7']._serialized_start=1961
  _globals['_GSPDISPATCHERSUBDATA7']._serialized_end=2184
  _globals['_GSPDISPATCHERSUBDATA8']._serialized_start=2187
  _globals['_GSPDISPATCHERSUBDATA8']._serialized_end=2647
  _globals['_GSPDISPATCHERSUBDATA10']._serialized_start=2649
  _globals['_GSPDISPATCHERSUBDATA10']._serialized_end=2690
  _globals['_GSPDISPATCHERSUBDATA11']._serialized_start=2692
  _globals['_GSPDISPATCHERSUBDATA11']._serialized_end=2741
  _globals['_GSPDISPATCHERSUBDATA12']._serialized_start=2743
  _globals['_GSPDISPATCHERSUBDATA12']._serialized_end=2817
  _globals['_GSPDISPATCHERSUBDATA13']._serialized_start=2820
  _globals['_GSPDISPATCHERSUBDATA13']._serialized_end=2980
  _globals['_GSPDISPATCHERSUBDATA14']._serialized_start=2982
  _globals['_GSPDISPATCHERSUBDATA14']._serialized_end=3056
  _globals['_GSPDISPATCHERSERVICEDATA']._serialized_start=3059
  _globals['_GSPDISPATCHERSERVICEDATA']._serialized_end=3491
  _globals['_GSPDISPATCHERSUBDATA1']._serialized_start=3493
  _globals['_GSPDISPATCHERSUBDATA1']._serialized_end=3566
  _globals['_GSPDISPATCHERSUBDATA2']._serialized_start=3568
  _globals['_GSPDISPATCHERSUBDATA2']._serialized_end=3630
  _globals['_GSPDISPATCHERCOUNTRYDATA']._serialized_start=3633
  _globals['_GSPDISPATCHERCOUNTRYDATA']._serialized_end=4088
  _globals['_GSPDISPATCHERSUBDATA3']._serialized_start=4090
  _globals['_GSPDISPATCHERSUBDATA3']._serialized_end=4163
  _globals['_GSPDISPATCHERSUBDATA4']._serialized_start=4165
  _globals['_GSPDISPATCHERSUBDATA4']._serialized_end=4253
  _globals['_GSPDISPATCHERSUBDATA5']._serialized_start=4255
  _globals['_GSPDISPATCHERSUBDATA5']._serialized_end=4328
  _globals['_GSPDISPATCHERSUBSTRING1']._serialized_start=4330
  _globals['_GSPDISPATCHERSUBSTRING1']._serialized_end=4424
  _globals['_GSPDISPATCHERSUBSTRING2']._serialized_start=4426
  _globals['_GSPDISPATCHERSUBSTRING2']._serialized_end=4539
  _globals['_GSPDISPATCHERADDRESS']._serialized_start=4541
  _globals['_GSPDISPATCHERADDRESS']._serialized_end=4656
  _globals['_GSPDISPATCHERSUBDATA15']._serialized_start=4658
  _globals['_GSPDISPATCHERSUBDATA15']._serialized_end=4731
# @@protoc_insertion_point(module_scope)
