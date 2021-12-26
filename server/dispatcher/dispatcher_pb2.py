# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dispatcher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dispatcher.proto',
  package='dispatcher',
  syntax='proto3',
  serialized_options=b'\n\022io.grpc.dispatcherB\nDispatcherP\001\242\002\003DBR',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x64ispatcher.proto\x12\ndispatcher\"\"\n\x04User\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"U\n\x04Game\x12\x1f\n\x05owner\x18\x01 \x01(\x0b\x32\x10.dispatcher.User\x12\r\n\x05state\x18\x02 \x01(\x03\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\t\"M\n\x0bJoinRequest\x12\x1e\n\x04user\x18\x01 \x01(\x0b\x32\x10.dispatcher.User\x12\x1e\n\x04game\x18\x02 \x01(\x0b\x32\x10.dispatcher.Game\"\x16\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x32\xa7\x02\n\nDispatcher\x12\x35\n\x0bGetGameList\x12\x10.dispatcher.User\x1a\x10.dispatcher.Game\"\x00\x30\x01\x12\x32\n\nCreateGame\x12\x10.dispatcher.User\x1a\x10.dispatcher.Game\"\x00\x12\x33\n\tCloseGame\x12\x10.dispatcher.Game\x1a\x12.dispatcher.Status\"\x00\x12;\n\nJoinPlayer\x12\x17.dispatcher.JoinRequest\x1a\x12.dispatcher.Status\"\x00\x12<\n\x0bJoinVisitor\x12\x17.dispatcher.JoinRequest\x1a\x12.dispatcher.Status\"\x00\x42(\n\x12io.grpc.dispatcherB\nDispatcherP\x01\xa2\x02\x03\x44\x42Rb\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='dispatcher.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='dispatcher.User.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='dispatcher.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=66,
)


_GAME = _descriptor.Descriptor(
  name='Game',
  full_name='dispatcher.Game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='dispatcher.Game.owner', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='dispatcher.Game.state', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='dispatcher.Game.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='dispatcher.Game.port', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=68,
  serialized_end=153,
)


_JOINREQUEST = _descriptor.Descriptor(
  name='JoinRequest',
  full_name='dispatcher.JoinRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='dispatcher.JoinRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game', full_name='dispatcher.JoinRequest.game', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=155,
  serialized_end=232,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='dispatcher.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dispatcher.Status.code', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=234,
  serialized_end=256,
)

_GAME.fields_by_name['owner'].message_type = _USER
_JOINREQUEST.fields_by_name['user'].message_type = _USER
_JOINREQUEST.fields_by_name['game'].message_type = _GAME
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Game'] = _GAME
DESCRIPTOR.message_types_by_name['JoinRequest'] = _JOINREQUEST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:dispatcher.User)
  })
_sym_db.RegisterMessage(User)

Game = _reflection.GeneratedProtocolMessageType('Game', (_message.Message,), {
  'DESCRIPTOR' : _GAME,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:dispatcher.Game)
  })
_sym_db.RegisterMessage(Game)

JoinRequest = _reflection.GeneratedProtocolMessageType('JoinRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINREQUEST,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:dispatcher.JoinRequest)
  })
_sym_db.RegisterMessage(JoinRequest)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:dispatcher.Status)
  })
_sym_db.RegisterMessage(Status)


DESCRIPTOR._options = None

_DISPATCHER = _descriptor.ServiceDescriptor(
  name='Dispatcher',
  full_name='dispatcher.Dispatcher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=259,
  serialized_end=554,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGameList',
    full_name='dispatcher.Dispatcher.GetGameList',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_GAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateGame',
    full_name='dispatcher.Dispatcher.CreateGame',
    index=1,
    containing_service=None,
    input_type=_USER,
    output_type=_GAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseGame',
    full_name='dispatcher.Dispatcher.CloseGame',
    index=2,
    containing_service=None,
    input_type=_GAME,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='JoinPlayer',
    full_name='dispatcher.Dispatcher.JoinPlayer',
    index=3,
    containing_service=None,
    input_type=_JOINREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='JoinVisitor',
    full_name='dispatcher.Dispatcher.JoinVisitor',
    index=4,
    containing_service=None,
    input_type=_JOINREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISPATCHER)

DESCRIPTOR.services_by_name['Dispatcher'] = _DISPATCHER

# @@protoc_insertion_point(module_scope)
