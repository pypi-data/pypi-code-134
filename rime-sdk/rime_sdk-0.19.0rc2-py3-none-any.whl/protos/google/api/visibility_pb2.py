# autogenerated
# mypy: ignore-errors
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/visibility.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgoogle/api/visibility.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto\"7\n\nVisibility\x12)\n\x05rules\x18\x01 \x03(\x0b\x32\x1a.google.api.VisibilityRule\"7\n\x0eVisibilityRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x13\n\x0brestriction\x18\x02 \x01(\t:T\n\x0f\x65num_visibility\x12\x1c.google.protobuf.EnumOptions\x18\xaf\xca\xbc\" \x01(\x0b\x32\x1a.google.api.VisibilityRule:Z\n\x10value_visibility\x12!.google.protobuf.EnumValueOptions\x18\xaf\xca\xbc\" \x01(\x0b\x32\x1a.google.api.VisibilityRule:V\n\x10\x66ield_visibility\x12\x1d.google.protobuf.FieldOptions\x18\xaf\xca\xbc\" \x01(\x0b\x32\x1a.google.api.VisibilityRule:Z\n\x12message_visibility\x12\x1f.google.protobuf.MessageOptions\x18\xaf\xca\xbc\" \x01(\x0b\x32\x1a.google.api.VisibilityRule:X\n\x11method_visibility\x12\x1e.google.protobuf.MethodOptions\x18\xaf\xca\xbc\" \x01(\x0b\x32\x1a.google.api.VisibilityRule:V\n\x0e\x61pi_visibility\x12\x1f.google.protobuf.ServiceOptions\x18\xaf\xca\xbc\" \x01(\x0b\x32\x1a.google.api.VisibilityRuleBn\n\x0e\x63om.google.apiB\x0fVisibilityProtoP\x01Z?google.golang.org/genproto/googleapis/api/visibility;visibility\xf8\x01\x01\xa2\x02\x04GAPIb\x06proto3')


ENUM_VISIBILITY_FIELD_NUMBER = 72295727
enum_visibility = DESCRIPTOR.extensions_by_name['enum_visibility']
VALUE_VISIBILITY_FIELD_NUMBER = 72295727
value_visibility = DESCRIPTOR.extensions_by_name['value_visibility']
FIELD_VISIBILITY_FIELD_NUMBER = 72295727
field_visibility = DESCRIPTOR.extensions_by_name['field_visibility']
MESSAGE_VISIBILITY_FIELD_NUMBER = 72295727
message_visibility = DESCRIPTOR.extensions_by_name['message_visibility']
METHOD_VISIBILITY_FIELD_NUMBER = 72295727
method_visibility = DESCRIPTOR.extensions_by_name['method_visibility']
API_VISIBILITY_FIELD_NUMBER = 72295727
api_visibility = DESCRIPTOR.extensions_by_name['api_visibility']

_VISIBILITY = DESCRIPTOR.message_types_by_name['Visibility']
_VISIBILITYRULE = DESCRIPTOR.message_types_by_name['VisibilityRule']
Visibility = _reflection.GeneratedProtocolMessageType('Visibility', (_message.Message,), {
  'DESCRIPTOR' : _VISIBILITY,
  '__module__' : 'rime_sdk.protos.google.api.visibility_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Visibility)
  })
_sym_db.RegisterMessage(Visibility)

VisibilityRule = _reflection.GeneratedProtocolMessageType('VisibilityRule', (_message.Message,), {
  'DESCRIPTOR' : _VISIBILITYRULE,
  '__module__' : 'rime_sdk.protos.google.api.visibility_pb2'
  # @@protoc_insertion_point(class_scope:google.api.VisibilityRule)
  })
_sym_db.RegisterMessage(VisibilityRule)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_visibility)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(value_visibility)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_visibility)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_visibility)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method_visibility)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(api_visibility)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.google.apiB\017VisibilityProtoP\001Z?google.golang.org/genproto/googleapis/api/visibility;visibility\370\001\001\242\002\004GAPI'
  _VISIBILITY._serialized_start=77
  _VISIBILITY._serialized_end=132
  _VISIBILITYRULE._serialized_start=134
  _VISIBILITYRULE._serialized_end=189
# @@protoc_insertion_point(module_scope)
