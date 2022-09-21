# autogenerated
# mypy: ignore-errors
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rime_info/rime_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rime_sdk.protos.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19rime_info/rime_info.proto\x12\x04rime\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x14\n\x12GetRIMEInfoRequest\"\xec\x01\n\x13GetRIMEInfoResponse\x12\x1c\n\x14\x63luster_info_version\x18\x01 \x01(\t\x12\x15\n\rcustomer_name\x18\x02 \x01(\t\x12\x33\n\x0f\x65xpiration_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x15grace_period_end_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tis_hosted\x18\x05 \x01(\x08\x12\x1d\n\x07ri_plan\x18\x06 \x01(\x0e\x32\x0c.rime.RIPlan*g\n\x06RIPlan\x12\x17\n\x13RI_PLAN_UNSPECIFIED\x10\x00\x12\x13\n\x0fRI_PLAN_DEFAULT\x10\x01\x12\x16\n\x12RI_PLAN_SELF_SERVE\x10\x02\x12\x17\n\x13RI_PLAN_LOCAL_TRIAL\x10\x03\x32\x65\n\x08RIMEInfo\x12Y\n\x0bGetRIMEInfo\x12\x18.rime.GetRIMEInfoRequest\x1a\x19.rime.GetRIMEInfoResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/rime-infoB\x19Z\x17ri/_gen/protos/rimeinfob\x06proto3')

_RIPLAN = DESCRIPTOR.enum_types_by_name['RIPlan']
RIPlan = enum_type_wrapper.EnumTypeWrapper(_RIPLAN)
RI_PLAN_UNSPECIFIED = 0
RI_PLAN_DEFAULT = 1
RI_PLAN_SELF_SERVE = 2
RI_PLAN_LOCAL_TRIAL = 3


_GETRIMEINFOREQUEST = DESCRIPTOR.message_types_by_name['GetRIMEInfoRequest']
_GETRIMEINFORESPONSE = DESCRIPTOR.message_types_by_name['GetRIMEInfoResponse']
GetRIMEInfoRequest = _reflection.GeneratedProtocolMessageType('GetRIMEInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRIMEINFOREQUEST,
  '__module__' : 'rime_sdk.protos.rime_info.rime_info_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetRIMEInfoRequest)
  })
_sym_db.RegisterMessage(GetRIMEInfoRequest)

GetRIMEInfoResponse = _reflection.GeneratedProtocolMessageType('GetRIMEInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRIMEINFORESPONSE,
  '__module__' : 'rime_sdk.protos.rime_info.rime_info_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetRIMEInfoResponse)
  })
_sym_db.RegisterMessage(GetRIMEInfoResponse)

_RIMEINFO = DESCRIPTOR.services_by_name['RIMEInfo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\027ri/_gen/protos/rimeinfo'
  _RIMEINFO.methods_by_name['GetRIMEInfo']._options = None
  _RIMEINFO.methods_by_name['GetRIMEInfo']._serialized_options = b'\202\323\344\223\002\017\022\r/v1/rime-info'
  _RIPLAN._serialized_start=359
  _RIPLAN._serialized_end=462
  _GETRIMEINFOREQUEST._serialized_start=98
  _GETRIMEINFOREQUEST._serialized_end=118
  _GETRIMEINFORESPONSE._serialized_start=121
  _GETRIMEINFORESPONSE._serialized_end=357
  _RIMEINFO._serialized_start=464
  _RIMEINFO._serialized_end=565
# @@protoc_insertion_point(module_scope)
