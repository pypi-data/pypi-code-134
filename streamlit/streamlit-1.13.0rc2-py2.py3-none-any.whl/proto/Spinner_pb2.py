# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Spinner.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/Spinner.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dstreamlit/proto/Spinner.proto\"\x17\n\x07Spinner\x12\x0c\n\x04text\x18\x01 \x01(\tb\x06proto3'
)




_SPINNER = _descriptor.Descriptor(
  name='Spinner',
  full_name='Spinner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Spinner.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=56,
)

DESCRIPTOR.message_types_by_name['Spinner'] = _SPINNER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Spinner = _reflection.GeneratedProtocolMessageType('Spinner', (_message.Message,), {
  'DESCRIPTOR' : _SPINNER,
  '__module__' : 'streamlit.proto.Spinner_pb2'
  # @@protoc_insertion_point(class_scope:Spinner)
  })
_sym_db.RegisterMessage(Spinner)


# @@protoc_insertion_point(module_scope)
