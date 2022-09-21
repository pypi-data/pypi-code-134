# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udsink.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0cudsink.proto\x12\x07sink.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto";\n\tEventTime\x12.\n\nevent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp":\n\tWatermark\x12-\n\twatermark\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"~\n\x05\x44\x61tum\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12&\n\nevent_time\x18\x03 \x01(\x0b\x32\x12.sink.v1.EventTime\x12%\n\twatermark\x18\x04 \x01(\x0b\x32\x12.sink.v1.Watermark\x12\n\n\x02id\x18\x05 \x01(\t"-\n\tDatumList\x12 \n\x08\x65lements\x18\x01 \x03(\x0b\x32\x0e.sink.v1.Datum"\x1e\n\rReadyResponse\x12\r\n\x05ready\x18\x01 \x01(\x08"8\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07\x65rr_msg\x18\x03 \x01(\t"4\n\x0cResponseList\x12$\n\tresponses\x18\x01 \x03(\x0b\x32\x11.sink.v1.Response2\x81\x01\n\x0fUserDefinedSink\x12\x33\n\x06SinkFn\x12\x12.sink.v1.DatumList\x1a\x15.sink.v1.ResponseList\x12\x39\n\x07IsReady\x12\x16.google.protobuf.Empty\x1a\x16.sink.v1.ReadyResponseB9Z7github.com/numaproj/numaflow-go/pkg/apis/protos/sink/v1b\x06proto3'
)


_EVENTTIME = DESCRIPTOR.message_types_by_name["EventTime"]
_WATERMARK = DESCRIPTOR.message_types_by_name["Watermark"]
_DATUM = DESCRIPTOR.message_types_by_name["Datum"]
_DATUMLIST = DESCRIPTOR.message_types_by_name["DatumList"]
_READYRESPONSE = DESCRIPTOR.message_types_by_name["ReadyResponse"]
_RESPONSE = DESCRIPTOR.message_types_by_name["Response"]
_RESPONSELIST = DESCRIPTOR.message_types_by_name["ResponseList"]
EventTime = _reflection.GeneratedProtocolMessageType(
    "EventTime",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTTIME,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.EventTime)
    },
)
_sym_db.RegisterMessage(EventTime)

Watermark = _reflection.GeneratedProtocolMessageType(
    "Watermark",
    (_message.Message,),
    {
        "DESCRIPTOR": _WATERMARK,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.Watermark)
    },
)
_sym_db.RegisterMessage(Watermark)

Datum = _reflection.GeneratedProtocolMessageType(
    "Datum",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATUM,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.Datum)
    },
)
_sym_db.RegisterMessage(Datum)

DatumList = _reflection.GeneratedProtocolMessageType(
    "DatumList",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATUMLIST,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.DatumList)
    },
)
_sym_db.RegisterMessage(DatumList)

ReadyResponse = _reflection.GeneratedProtocolMessageType(
    "ReadyResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _READYRESPONSE,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.ReadyResponse)
    },
)
_sym_db.RegisterMessage(ReadyResponse)

Response = _reflection.GeneratedProtocolMessageType(
    "Response",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPONSE,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.Response)
    },
)
_sym_db.RegisterMessage(Response)

ResponseList = _reflection.GeneratedProtocolMessageType(
    "ResponseList",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPONSELIST,
        "__module__": "udsink_pb2"
        # @@protoc_insertion_point(class_scope:sink.v1.ResponseList)
    },
)
_sym_db.RegisterMessage(ResponseList)

_USERDEFINEDSINK = DESCRIPTOR.services_by_name["UserDefinedSink"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z7github.com/numaproj/numaflow-go/pkg/apis/protos/sink/v1"
    _EVENTTIME._serialized_start = 87
    _EVENTTIME._serialized_end = 146
    _WATERMARK._serialized_start = 148
    _WATERMARK._serialized_end = 206
    _DATUM._serialized_start = 208
    _DATUM._serialized_end = 334
    _DATUMLIST._serialized_start = 336
    _DATUMLIST._serialized_end = 381
    _READYRESPONSE._serialized_start = 383
    _READYRESPONSE._serialized_end = 413
    _RESPONSE._serialized_start = 415
    _RESPONSE._serialized_end = 471
    _RESPONSELIST._serialized_start = 473
    _RESPONSELIST._serialized_end = 525
    _USERDEFINEDSINK._serialized_start = 528
    _USERDEFINEDSINK._serialized_end = 657
# @@protoc_insertion_point(module_scope)
