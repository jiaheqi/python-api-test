# -*- coding: UTF-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commons.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commons.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\033com.hualala.app.equity.grpcB\006Common'),
  serialized_pb=_b('\n\rcommons.proto\" \n\rRequestHeader\x12\x0f\n\x07traceID\x18\x01 \x01(\t\">\n\x0cResultHeader\x12\x0f\n\x07traceID\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"5\n\x11RequestPageHeader\x12\x0e\n\x06pageNo\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\"Z\n\x10ResultPageHeader\x12\x0e\n\x06pageNo\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x11\n\tpageCount\x18\x03 \x01(\x05\x12\x11\n\ttotalSize\x18\x04 \x01(\x05\x42%\n\x1b\x63om.hualala.app.equity.grpcB\x06\x43ommonb\x06proto3')
)




_REQUESTHEADER = _descriptor.Descriptor(
  name='RequestHeader',
  full_name='RequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='RequestHeader.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=17,
  serialized_end=49,
)


_RESULTHEADER = _descriptor.Descriptor(
  name='ResultHeader',
  full_name='ResultHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='traceID', full_name='ResultHeader.traceID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='ResultHeader.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ResultHeader.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=51,
  serialized_end=113,
)


_REQUESTPAGEHEADER = _descriptor.Descriptor(
  name='RequestPageHeader',
  full_name='RequestPageHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageNo', full_name='RequestPageHeader.pageNo', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='RequestPageHeader.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=115,
  serialized_end=168,
)


_RESULTPAGEHEADER = _descriptor.Descriptor(
  name='ResultPageHeader',
  full_name='ResultPageHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageNo', full_name='ResultPageHeader.pageNo', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='ResultPageHeader.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageCount', full_name='ResultPageHeader.pageCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalSize', full_name='ResultPageHeader.totalSize', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=170,
  serialized_end=260,
)

DESCRIPTOR.message_types_by_name['RequestHeader'] = _REQUESTHEADER
DESCRIPTOR.message_types_by_name['ResultHeader'] = _RESULTHEADER
DESCRIPTOR.message_types_by_name['RequestPageHeader'] = _REQUESTPAGEHEADER
DESCRIPTOR.message_types_by_name['ResultPageHeader'] = _RESULTPAGEHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestHeader = _reflection.GeneratedProtocolMessageType('RequestHeader', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTHEADER,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:RequestHeader)
  ))
_sym_db.RegisterMessage(RequestHeader)

ResultHeader = _reflection.GeneratedProtocolMessageType('ResultHeader', (_message.Message,), dict(
  DESCRIPTOR = _RESULTHEADER,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:ResultHeader)
  ))
_sym_db.RegisterMessage(ResultHeader)

RequestPageHeader = _reflection.GeneratedProtocolMessageType('RequestPageHeader', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTPAGEHEADER,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:RequestPageHeader)
  ))
_sym_db.RegisterMessage(RequestPageHeader)

ResultPageHeader = _reflection.GeneratedProtocolMessageType('ResultPageHeader', (_message.Message,), dict(
  DESCRIPTOR = _RESULTPAGEHEADER,
  __module__ = 'commons_pb2'
  # @@protoc_insertion_point(class_scope:ResultPageHeader)
  ))
_sym_db.RegisterMessage(ResultPageHeader)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
