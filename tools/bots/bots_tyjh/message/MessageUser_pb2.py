# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageUser.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MessageUser.proto',
  package='Message',
  serialized_pb=_b('\n\x11MessageUser.proto\x12\x07Message\"\x95\x01\n\x0c\x43\x32SUserLogin\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\r\n\x05\x61ppid\x18\x02 \x01(\t\x12\x0e\n\x06ticket\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x04 \x01(\t\x12\x0f\n\x07macaddr\x18\x05 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x06 \x01(\t\x12\r\n\x05model\x18\x07 \x01(\t\x12\x0e\n\x06system\x18\x08 \x01(\t\"\xbf\x01\n\x0cS2CUserLogin\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x12\n\nlastplayer\x18\x02 \x01(\t\x12\x34\n\nplayerlist\x18\x03 \x03(\x0b\x32 .Message.S2CUserLogin.PlayerInfo\x1aX\n\nPlayerInfo\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06gender\x18\x03 \x01(\x05\x12\x10\n\x08vocation\x18\x04 \x01(\x05\x12\r\n\x05level\x18\x05 \x01(\x05\"\x0f\n\rC2SUserLogout\"\x12\n\x10\x43\x32SUserHeartbeat\"!\n\x10S2CUserHeartbeat\x12\r\n\x05stime\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2SUSERLOGIN = _descriptor.Descriptor(
  name='C2SUserLogin',
  full_name='Message.C2SUserLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='Message.C2SUserLogin.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appid', full_name='Message.C2SUserLogin.appid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticket', full_name='Message.C2SUserLogin.ticket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='Message.C2SUserLogin.deviceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='macaddr', full_name='Message.C2SUserLogin.macaddr', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='Message.C2SUserLogin.manufacturer', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='Message.C2SUserLogin.model', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system', full_name='Message.C2SUserLogin.system', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=180,
)


_S2CUSERLOGIN_PLAYERINFO = _descriptor.Descriptor(
  name='PlayerInfo',
  full_name='Message.S2CUserLogin.PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Message.S2CUserLogin.PlayerInfo.pid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Message.S2CUserLogin.PlayerInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='Message.S2CUserLogin.PlayerInfo.gender', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocation', full_name='Message.S2CUserLogin.PlayerInfo.vocation', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Message.S2CUserLogin.PlayerInfo.level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=374,
)

_S2CUSERLOGIN = _descriptor.Descriptor(
  name='S2CUserLogin',
  full_name='Message.S2CUserLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='Message.S2CUserLogin.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastplayer', full_name='Message.S2CUserLogin.lastplayer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playerlist', full_name='Message.S2CUserLogin.playerlist', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_S2CUSERLOGIN_PLAYERINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=374,
)


_C2SUSERLOGOUT = _descriptor.Descriptor(
  name='C2SUserLogout',
  full_name='Message.C2SUserLogout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=391,
)


_C2SUSERHEARTBEAT = _descriptor.Descriptor(
  name='C2SUserHeartbeat',
  full_name='Message.C2SUserHeartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=411,
)


_S2CUSERHEARTBEAT = _descriptor.Descriptor(
  name='S2CUserHeartbeat',
  full_name='Message.S2CUserHeartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stime', full_name='Message.S2CUserHeartbeat.stime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=446,
)

_S2CUSERLOGIN_PLAYERINFO.containing_type = _S2CUSERLOGIN
_S2CUSERLOGIN.fields_by_name['playerlist'].message_type = _S2CUSERLOGIN_PLAYERINFO
DESCRIPTOR.message_types_by_name['C2SUserLogin'] = _C2SUSERLOGIN
DESCRIPTOR.message_types_by_name['S2CUserLogin'] = _S2CUSERLOGIN
DESCRIPTOR.message_types_by_name['C2SUserLogout'] = _C2SUSERLOGOUT
DESCRIPTOR.message_types_by_name['C2SUserHeartbeat'] = _C2SUSERHEARTBEAT
DESCRIPTOR.message_types_by_name['S2CUserHeartbeat'] = _S2CUSERHEARTBEAT

C2SUserLogin = _reflection.GeneratedProtocolMessageType('C2SUserLogin', (_message.Message,), dict(
  DESCRIPTOR = _C2SUSERLOGIN,
  __module__ = 'MessageUser_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SUserLogin)
  ))
_sym_db.RegisterMessage(C2SUserLogin)

S2CUserLogin = _reflection.GeneratedProtocolMessageType('S2CUserLogin', (_message.Message,), dict(

  PlayerInfo = _reflection.GeneratedProtocolMessageType('PlayerInfo', (_message.Message,), dict(
    DESCRIPTOR = _S2CUSERLOGIN_PLAYERINFO,
    __module__ = 'MessageUser_pb2'
    # @@protoc_insertion_point(class_scope:Message.S2CUserLogin.PlayerInfo)
    ))
  ,
  DESCRIPTOR = _S2CUSERLOGIN,
  __module__ = 'MessageUser_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CUserLogin)
  ))
_sym_db.RegisterMessage(S2CUserLogin)
_sym_db.RegisterMessage(S2CUserLogin.PlayerInfo)

C2SUserLogout = _reflection.GeneratedProtocolMessageType('C2SUserLogout', (_message.Message,), dict(
  DESCRIPTOR = _C2SUSERLOGOUT,
  __module__ = 'MessageUser_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SUserLogout)
  ))
_sym_db.RegisterMessage(C2SUserLogout)

C2SUserHeartbeat = _reflection.GeneratedProtocolMessageType('C2SUserHeartbeat', (_message.Message,), dict(
  DESCRIPTOR = _C2SUSERHEARTBEAT,
  __module__ = 'MessageUser_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SUserHeartbeat)
  ))
_sym_db.RegisterMessage(C2SUserHeartbeat)

S2CUserHeartbeat = _reflection.GeneratedProtocolMessageType('S2CUserHeartbeat', (_message.Message,), dict(
  DESCRIPTOR = _S2CUSERHEARTBEAT,
  __module__ = 'MessageUser_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CUserHeartbeat)
  ))
_sym_db.RegisterMessage(S2CUserHeartbeat)


# @@protoc_insertion_point(module_scope)
