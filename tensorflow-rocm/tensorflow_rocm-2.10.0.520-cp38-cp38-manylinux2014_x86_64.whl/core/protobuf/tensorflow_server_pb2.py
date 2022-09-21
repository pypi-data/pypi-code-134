# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/tensorflow_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.protobuf import cluster_pb2 as tensorflow_dot_core_dot_protobuf_dot_cluster__pb2
from tensorflow.core.protobuf import config_pb2 as tensorflow_dot_core_dot_protobuf_dot_config__pb2
from tensorflow.core.protobuf import device_filters_pb2 as tensorflow_dot_core_dot_protobuf_dot_device__filters__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/tensorflow_server.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\032org.tensorflow.distruntimeB\014ServerProtosP\001ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\370\001\001'),
  serialized_pb=_b('\n0tensorflow/core/protobuf/tensorflow_server.proto\x12\ntensorflow\x1a&tensorflow/core/protobuf/cluster.proto\x1a%tensorflow/core/protobuf/config.proto\x1a-tensorflow/core/protobuf/device_filters.proto\"\xf5\x01\n\tServerDef\x12\'\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x16.tensorflow.ClusterDef\x12\x10\n\x08job_name\x18\x02 \x01(\t\x12\x12\n\ntask_index\x18\x03 \x01(\x05\x12\x37\n\x16\x64\x65\x66\x61ult_session_config\x18\x04 \x01(\x0b\x32\x17.tensorflow.ConfigProto\x12\x10\n\x08protocol\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05\x12@\n\x16\x63luster_device_filters\x18\x07 \x01(\x0b\x32 .tensorflow.ClusterDeviceFiltersB\x86\x01\n\x1aorg.tensorflow.distruntimeB\x0cServerProtosP\x01ZUgithub.com/tensorflow/tensorflow/tensorflow/go/core/protobuf/for_core_protos_go_proto\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_protobuf_dot_cluster__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_config__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_device__filters__pb2.DESCRIPTOR,])




_SERVERDEF = _descriptor.Descriptor(
  name='ServerDef',
  full_name='tensorflow.ServerDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='tensorflow.ServerDef.cluster', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_name', full_name='tensorflow.ServerDef.job_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_index', full_name='tensorflow.ServerDef.task_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_session_config', full_name='tensorflow.ServerDef.default_session_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='tensorflow.ServerDef.protocol', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='tensorflow.ServerDef.port', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_device_filters', full_name='tensorflow.ServerDef.cluster_device_filters', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=191,
  serialized_end=436,
)

_SERVERDEF.fields_by_name['cluster'].message_type = tensorflow_dot_core_dot_protobuf_dot_cluster__pb2._CLUSTERDEF
_SERVERDEF.fields_by_name['default_session_config'].message_type = tensorflow_dot_core_dot_protobuf_dot_config__pb2._CONFIGPROTO
_SERVERDEF.fields_by_name['cluster_device_filters'].message_type = tensorflow_dot_core_dot_protobuf_dot_device__filters__pb2._CLUSTERDEVICEFILTERS
DESCRIPTOR.message_types_by_name['ServerDef'] = _SERVERDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerDef = _reflection.GeneratedProtocolMessageType('ServerDef', (_message.Message,), {
  'DESCRIPTOR' : _SERVERDEF,
  '__module__' : 'tensorflow.core.protobuf.tensorflow_server_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ServerDef)
  })
_sym_db.RegisterMessage(ServerDef)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
