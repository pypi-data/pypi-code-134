# autogenerated
# mypy: ignore-errors
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from rime_sdk.protos.common import common_pb2 as common_dot_common__pb2
from rime_sdk.protos.result_synthesizer import result_message_pb2 as result__synthesizer_dot_result__message__pb2
from rime_sdk.protos.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from rime_sdk.protos.grpc_gateway.openapi import annotations_pb2 as grpc__gateway_dot_openapi_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15project/project.proto\x12\x04rime\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13\x63ommon/common.proto\x1a\'result_synthesizer/result_message.proto\x1a\x1cgoogle/api/annotations.proto\x1a&grpc_gateway/openapi/annotations.proto\"O\n\x14\x43reateProjectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x03 \x01(\t\"7\n\x15\x43reateProjectResponse\x12\x1e\n\x07project\x18\x01 \x01(\x0b\x32\r.rime.Project\"\'\n\x11GetProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"=\n\x12GetProjectResponse\x12\'\n\x07project\x18\x01 \x01(\x0b\x32\x16.rime.AnnotatedProject\"\\\n\x14UpdateProjectRequest\x12\x1e\n\x07project\x18\x01 \x01(\x0b\x32\r.rime.Project\x12$\n\x04mask\x18\x02 \x01(\x0b\x32\x16.rime.ProjectWriteMask\"7\n\x15UpdateProjectResponse\x12\x1e\n\x07project\x18\x01 \x01(\x0b\x32\r.rime.Project\"*\n\x14\x44\x65leteProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"\x17\n\x15\x44\x65leteProjectResponse\"<\n\x13ListProjectsRequest\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\"k\n\x14ListProjectsResponse\x12(\n\x08projects\x18\x01 \x03(\x0b\x32\x16.rime.AnnotatedProject\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x10\n\x08has_more\x18\x03 \x01(\x08\"f\n\x13MoveTestRunsRequest\x12\x19\n\x11source_project_id\x18\x01 \x01(\t\x12\x1e\n\x16\x64\x65stination_project_id\x18\x02 \x01(\t\x12\x14\n\x0ctest_run_ids\x18\x03 \x03(\t\"\x16\n\x14MoveTestRunsResponse\"<\n&ServeAvailableColumnsForProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"X\n\'ServeAvailableColumnsForProjectResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x19\n\x11\x61vailable_columns\x18\x02 \x03(\t\"\x86\x01\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x30\n\x0c\x63reated_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cworkspace_id\x18\x06 \x01(\tJ\x04\x08\x05\x10\x06\"\xe1\x01\n\x10\x41nnotatedProject\x12\x1e\n\x07project\x18\x01 \x01(\x0b\x32\r.rime.Project\x12\x36\n\x12last_test_run_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0etest_run_count\x18\x03 \x01(\x04\x12\x39\n\x16test_run_count_mapping\x18\x04 \x03(\x0b\x32\x19.rime.TestRunCountMapping\x12\"\n\x0bweb_app_url\x18\x05 \x01(\x0b\x32\r.rime.SafeURL\"P\n\x13TestRunCountMapping\x12!\n\ttest_type\x18\x01 \x01(\x0e\x32\x0e.rime.TestType\x12\x16\n\x0etest_run_count\x18\x02 \x01(\x04\";\n\x10ProjectWriteMask\x12\x0c\n\x04name\x18\x02 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\x08J\x04\x08\x05\x10\x06\x32\xe5\x05\n\x0eProjectManager\x12\x61\n\rCreateProject\x12\x1a.rime.CreateProjectRequest\x1a\x1b.rime.CreateProjectResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/projects:\x01*\x12\x62\n\nGetProject\x12\x17.rime.GetProjectRequest\x1a\x18.rime.GetProjectResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/projects/{project_id}\x12H\n\rUpdateProject\x12\x1a.rime.UpdateProjectRequest\x1a\x1b.rime.UpdateProjectResponse\x12H\n\rDeleteProject\x12\x1a.rime.DeleteProjectRequest\x1a\x1b.rime.DeleteProjectResponse\x12[\n\x0cListProjects\x12\x19.rime.ListProjectsRequest\x1a\x1a.rime.ListProjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/projects\x12\x9a\x01\n\x0cMoveTestRuns\x12\x19.rime.MoveTestRunsRequest\x1a\x1a.rime.MoveTestRunsResponse\"S\x82\xd3\xe4\x93\x02M\"H/v1/projects/move-test-runs/{source_project_id}/{destination_project_id}:\x01*\x12~\n\x1fServeAvailableColumnsForProject\x12,.rime.ServeAvailableColumnsForProjectRequest\x1a-.rime.ServeAvailableColumnsForProjectResponseB\xfa\x01Z\x16ri/_gen/protos/project\x92\x41\xde\x01\x12\xb3\x01\n\x08Projects\x12KAPI methods for projects. Must be authenticated with \'rime-api-key\' header.\"U\n\x13Robust Intelligence\x12\"https://www.robustintelligence.com\x1a\x1a\x64\x65v@robustintelligence.com2\x03\x31.0*\x02\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonb\x06proto3')



_CREATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectRequest']
_CREATEPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['CreateProjectResponse']
_GETPROJECTREQUEST = DESCRIPTOR.message_types_by_name['GetProjectRequest']
_GETPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['GetProjectResponse']
_UPDATEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['UpdateProjectRequest']
_UPDATEPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateProjectResponse']
_DELETEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['DeleteProjectRequest']
_DELETEPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteProjectResponse']
_LISTPROJECTSREQUEST = DESCRIPTOR.message_types_by_name['ListProjectsRequest']
_LISTPROJECTSRESPONSE = DESCRIPTOR.message_types_by_name['ListProjectsResponse']
_MOVETESTRUNSREQUEST = DESCRIPTOR.message_types_by_name['MoveTestRunsRequest']
_MOVETESTRUNSRESPONSE = DESCRIPTOR.message_types_by_name['MoveTestRunsResponse']
_SERVEAVAILABLECOLUMNSFORPROJECTREQUEST = DESCRIPTOR.message_types_by_name['ServeAvailableColumnsForProjectRequest']
_SERVEAVAILABLECOLUMNSFORPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['ServeAvailableColumnsForProjectResponse']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
_ANNOTATEDPROJECT = DESCRIPTOR.message_types_by_name['AnnotatedProject']
_TESTRUNCOUNTMAPPING = DESCRIPTOR.message_types_by_name['TestRunCountMapping']
_PROJECTWRITEMASK = DESCRIPTOR.message_types_by_name['ProjectWriteMask']
CreateProjectRequest = _reflection.GeneratedProtocolMessageType('CreateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.CreateProjectRequest)
  })
_sym_db.RegisterMessage(CreateProjectRequest)

CreateProjectResponse = _reflection.GeneratedProtocolMessageType('CreateProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.CreateProjectResponse)
  })
_sym_db.RegisterMessage(CreateProjectResponse)

GetProjectRequest = _reflection.GeneratedProtocolMessageType('GetProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetProjectRequest)
  })
_sym_db.RegisterMessage(GetProjectRequest)

GetProjectResponse = _reflection.GeneratedProtocolMessageType('GetProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.GetProjectResponse)
  })
_sym_db.RegisterMessage(GetProjectResponse)

UpdateProjectRequest = _reflection.GeneratedProtocolMessageType('UpdateProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.UpdateProjectRequest)
  })
_sym_db.RegisterMessage(UpdateProjectRequest)

UpdateProjectResponse = _reflection.GeneratedProtocolMessageType('UpdateProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROJECTRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.UpdateProjectResponse)
  })
_sym_db.RegisterMessage(UpdateProjectResponse)

DeleteProjectRequest = _reflection.GeneratedProtocolMessageType('DeleteProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPROJECTREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.DeleteProjectRequest)
  })
_sym_db.RegisterMessage(DeleteProjectRequest)

DeleteProjectResponse = _reflection.GeneratedProtocolMessageType('DeleteProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPROJECTRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.DeleteProjectResponse)
  })
_sym_db.RegisterMessage(DeleteProjectResponse)

ListProjectsRequest = _reflection.GeneratedProtocolMessageType('ListProjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTSREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.ListProjectsRequest)
  })
_sym_db.RegisterMessage(ListProjectsRequest)

ListProjectsResponse = _reflection.GeneratedProtocolMessageType('ListProjectsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTSRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.ListProjectsResponse)
  })
_sym_db.RegisterMessage(ListProjectsResponse)

MoveTestRunsRequest = _reflection.GeneratedProtocolMessageType('MoveTestRunsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVETESTRUNSREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.MoveTestRunsRequest)
  })
_sym_db.RegisterMessage(MoveTestRunsRequest)

MoveTestRunsResponse = _reflection.GeneratedProtocolMessageType('MoveTestRunsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOVETESTRUNSRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.MoveTestRunsResponse)
  })
_sym_db.RegisterMessage(MoveTestRunsResponse)

ServeAvailableColumnsForProjectRequest = _reflection.GeneratedProtocolMessageType('ServeAvailableColumnsForProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVEAVAILABLECOLUMNSFORPROJECTREQUEST,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.ServeAvailableColumnsForProjectRequest)
  })
_sym_db.RegisterMessage(ServeAvailableColumnsForProjectRequest)

ServeAvailableColumnsForProjectResponse = _reflection.GeneratedProtocolMessageType('ServeAvailableColumnsForProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVEAVAILABLECOLUMNSFORPROJECTRESPONSE,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.ServeAvailableColumnsForProjectResponse)
  })
_sym_db.RegisterMessage(ServeAvailableColumnsForProjectResponse)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.Project)
  })
_sym_db.RegisterMessage(Project)

AnnotatedProject = _reflection.GeneratedProtocolMessageType('AnnotatedProject', (_message.Message,), {
  'DESCRIPTOR' : _ANNOTATEDPROJECT,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.AnnotatedProject)
  })
_sym_db.RegisterMessage(AnnotatedProject)

TestRunCountMapping = _reflection.GeneratedProtocolMessageType('TestRunCountMapping', (_message.Message,), {
  'DESCRIPTOR' : _TESTRUNCOUNTMAPPING,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.TestRunCountMapping)
  })
_sym_db.RegisterMessage(TestRunCountMapping)

ProjectWriteMask = _reflection.GeneratedProtocolMessageType('ProjectWriteMask', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTWRITEMASK,
  '__module__' : 'rime_sdk.protos.project.project_pb2'
  # @@protoc_insertion_point(class_scope:rime.ProjectWriteMask)
  })
_sym_db.RegisterMessage(ProjectWriteMask)

_PROJECTMANAGER = DESCRIPTOR.services_by_name['ProjectManager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\026ri/_gen/protos/project\222A\336\001\022\263\001\n\010Projects\022KAPI methods for projects. Must be authenticated with \'rime-api-key\' header.\"U\n\023Robust Intelligence\022\"https://www.robustintelligence.com\032\032dev@robustintelligence.com2\0031.0*\002\001\0022\020application/json:\020application/json'
  _PROJECTMANAGER.methods_by_name['CreateProject']._options = None
  _PROJECTMANAGER.methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/projects:\001*'
  _PROJECTMANAGER.methods_by_name['GetProject']._options = None
  _PROJECTMANAGER.methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/projects/{project_id}'
  _PROJECTMANAGER.methods_by_name['ListProjects']._options = None
  _PROJECTMANAGER.methods_by_name['ListProjects']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/projects'
  _PROJECTMANAGER.methods_by_name['MoveTestRuns']._options = None
  _PROJECTMANAGER.methods_by_name['MoveTestRuns']._serialized_options = b'\202\323\344\223\002M\"H/v1/projects/move-test-runs/{source_project_id}/{destination_project_id}:\001*'
  _CREATEPROJECTREQUEST._serialized_start=196
  _CREATEPROJECTREQUEST._serialized_end=275
  _CREATEPROJECTRESPONSE._serialized_start=277
  _CREATEPROJECTRESPONSE._serialized_end=332
  _GETPROJECTREQUEST._serialized_start=334
  _GETPROJECTREQUEST._serialized_end=373
  _GETPROJECTRESPONSE._serialized_start=375
  _GETPROJECTRESPONSE._serialized_end=436
  _UPDATEPROJECTREQUEST._serialized_start=438
  _UPDATEPROJECTREQUEST._serialized_end=530
  _UPDATEPROJECTRESPONSE._serialized_start=532
  _UPDATEPROJECTRESPONSE._serialized_end=587
  _DELETEPROJECTREQUEST._serialized_start=589
  _DELETEPROJECTREQUEST._serialized_end=631
  _DELETEPROJECTRESPONSE._serialized_start=633
  _DELETEPROJECTRESPONSE._serialized_end=656
  _LISTPROJECTSREQUEST._serialized_start=658
  _LISTPROJECTSREQUEST._serialized_end=718
  _LISTPROJECTSRESPONSE._serialized_start=720
  _LISTPROJECTSRESPONSE._serialized_end=827
  _MOVETESTRUNSREQUEST._serialized_start=829
  _MOVETESTRUNSREQUEST._serialized_end=931
  _MOVETESTRUNSRESPONSE._serialized_start=933
  _MOVETESTRUNSRESPONSE._serialized_end=955
  _SERVEAVAILABLECOLUMNSFORPROJECTREQUEST._serialized_start=957
  _SERVEAVAILABLECOLUMNSFORPROJECTREQUEST._serialized_end=1017
  _SERVEAVAILABLECOLUMNSFORPROJECTRESPONSE._serialized_start=1019
  _SERVEAVAILABLECOLUMNSFORPROJECTRESPONSE._serialized_end=1107
  _PROJECT._serialized_start=1110
  _PROJECT._serialized_end=1244
  _ANNOTATEDPROJECT._serialized_start=1247
  _ANNOTATEDPROJECT._serialized_end=1472
  _TESTRUNCOUNTMAPPING._serialized_start=1474
  _TESTRUNCOUNTMAPPING._serialized_end=1554
  _PROJECTWRITEMASK._serialized_start=1556
  _PROJECTWRITEMASK._serialized_end=1615
  _PROJECTMANAGER._serialized_start=1618
  _PROJECTMANAGER._serialized_end=2359
# @@protoc_insertion_point(module_scope)
