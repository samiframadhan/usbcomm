# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='protoblog',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\x12\tprotoblog\"K\n\x19TestMessageWithoutOptions\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x05\x12\r\n\x05whatf\x18\x03 \x01(\x05\x62\x06proto3'
)




_TESTMESSAGEWITHOUTOPTIONS = _descriptor.Descriptor(
  name='TestMessageWithoutOptions',
  full_name='protoblog.TestMessageWithoutOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='protoblog.TestMessageWithoutOptions.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='protoblog.TestMessageWithoutOptions.address', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='whatf', full_name='protoblog.TestMessageWithoutOptions.whatf', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=25,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['TestMessageWithoutOptions'] = _TESTMESSAGEWITHOUTOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessageWithoutOptions = _reflection.GeneratedProtocolMessageType('TestMessageWithoutOptions', (_message.Message,), {
  'DESCRIPTOR' : _TESTMESSAGEWITHOUTOPTIONS,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:protoblog.TestMessageWithoutOptions)
  })
_sym_db.RegisterMessage(TestMessageWithoutOptions)


# @@protoc_insertion_point(module_scope)