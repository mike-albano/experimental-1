# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='gnoi.common',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x63ommon.proto\x12\x0bgnoi.common\x1a\x0btypes.proto\"\xc5\x01\n\x0eRemoteDownload\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x36\n\x08protocol\x18\x02 \x01(\x0e\x32$.gnoi.common.RemoteDownload.Protocol\x12,\n\x0b\x63redentials\x18\x03 \x01(\x0b\x32\x17.gnoi.types.Credentials\"?\n\x08Protocol\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04SFTP\x10\x01\x12\x08\n\x04HTTP\x10\x02\x12\t\n\x05HTTPS\x10\x03\x12\x07\n\x03SCP\x10\x04\x62\x06proto3'
  ,
  dependencies=[types__pb2.DESCRIPTOR,])



_REMOTEDOWNLOAD_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='gnoi.common.RemoteDownload.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFTP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTPS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCP', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=177,
  serialized_end=240,
)
_sym_db.RegisterEnumDescriptor(_REMOTEDOWNLOAD_PROTOCOL)


_REMOTEDOWNLOAD = _descriptor.Descriptor(
  name='RemoteDownload',
  full_name='gnoi.common.RemoteDownload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='gnoi.common.RemoteDownload.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='gnoi.common.RemoteDownload.protocol', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credentials', full_name='gnoi.common.RemoteDownload.credentials', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REMOTEDOWNLOAD_PROTOCOL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=240,
)

_REMOTEDOWNLOAD.fields_by_name['protocol'].enum_type = _REMOTEDOWNLOAD_PROTOCOL
_REMOTEDOWNLOAD.fields_by_name['credentials'].message_type = types__pb2._CREDENTIALS
_REMOTEDOWNLOAD_PROTOCOL.containing_type = _REMOTEDOWNLOAD
DESCRIPTOR.message_types_by_name['RemoteDownload'] = _REMOTEDOWNLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoteDownload = _reflection.GeneratedProtocolMessageType('RemoteDownload', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEDOWNLOAD,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:gnoi.common.RemoteDownload)
  })
_sym_db.RegisterMessage(RemoteDownload)


# @@protoc_insertion_point(module_scope)
