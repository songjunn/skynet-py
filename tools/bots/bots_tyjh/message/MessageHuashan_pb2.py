# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageHuashan.proto

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
  name='MessageHuashan.proto',
  package='Message',
  serialized_pb=_b('\n\x14MessageHuashan.proto\x12\x07Message\"I\n\x0bHuashanTeam\x12\x0c\n\x04rank\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05point\x18\x03 \x01(\x05\x12\x0f\n\x07\x63onwins\x18\x04 \x01(\x05\"^\n\rHuashanRecord\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\x05\x12\x0f\n\x07\x63onwins\x18\x04 \x01(\x05\x12\r\n\x05point\x18\x05 \x01(\x05\" \n\x0f\x43\x32SHuashanEnter\x12\r\n\x05level\x18\x01 \x01(\x05\"\x10\n\x0e\x43\x32SHuashanQuit\"\x11\n\x0f\x43\x32SHuashanMatch\"\x13\n\x11\x43\x32SHuashanToplist\";\n\x11S2CHuashanToplist\x12&\n\x08teamlist\x18\x01 \x03(\x0b\x32\x14.Message.HuashanTeam\"\xae\x01\n\x12S2CHuashanTeamInfo\x12\x0e\n\x06teamid\x18\x01 \x01(\x05\x12\x10\n\x08teamname\x18\x02 \x01(\t\x12\r\n\x05point\x18\x03 \x01(\x05\x12\r\n\x05\x66ight\x18\x04 \x01(\x05\x12\x0f\n\x07victory\x18\x05 \x01(\x05\x12\x0f\n\x07\x63onwins\x18\x06 \x01(\x05\x12\r\n\x05level\x18\x07 \x01(\x05\x12\'\n\x07records\x18\x08 \x03(\x0b\x32\x16.Message.HuashanRecord')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HUASHANTEAM = _descriptor.Descriptor(
  name='HuashanTeam',
  full_name='Message.HuashanTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank', full_name='Message.HuashanTeam.rank', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Message.HuashanTeam.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='Message.HuashanTeam.point', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conwins', full_name='Message.HuashanTeam.conwins', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=33,
  serialized_end=106,
)


_HUASHANRECORD = _descriptor.Descriptor(
  name='HuashanRecord',
  full_name='Message.HuashanRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='Message.HuashanRecord.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='Message.HuashanRecord.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='Message.HuashanRecord.result', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conwins', full_name='Message.HuashanRecord.conwins', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='Message.HuashanRecord.point', index=4,
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
  serialized_start=108,
  serialized_end=202,
)


_C2SHUASHANENTER = _descriptor.Descriptor(
  name='C2SHuashanEnter',
  full_name='Message.C2SHuashanEnter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='Message.C2SHuashanEnter.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=204,
  serialized_end=236,
)


_C2SHUASHANQUIT = _descriptor.Descriptor(
  name='C2SHuashanQuit',
  full_name='Message.C2SHuashanQuit',
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
  serialized_start=238,
  serialized_end=254,
)


_C2SHUASHANMATCH = _descriptor.Descriptor(
  name='C2SHuashanMatch',
  full_name='Message.C2SHuashanMatch',
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
  serialized_start=256,
  serialized_end=273,
)


_C2SHUASHANTOPLIST = _descriptor.Descriptor(
  name='C2SHuashanToplist',
  full_name='Message.C2SHuashanToplist',
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
  serialized_start=275,
  serialized_end=294,
)


_S2CHUASHANTOPLIST = _descriptor.Descriptor(
  name='S2CHuashanToplist',
  full_name='Message.S2CHuashanToplist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamlist', full_name='Message.S2CHuashanToplist.teamlist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=296,
  serialized_end=355,
)


_S2CHUASHANTEAMINFO = _descriptor.Descriptor(
  name='S2CHuashanTeamInfo',
  full_name='Message.S2CHuashanTeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamid', full_name='Message.S2CHuashanTeamInfo.teamid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='teamname', full_name='Message.S2CHuashanTeamInfo.teamname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='Message.S2CHuashanTeamInfo.point', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight', full_name='Message.S2CHuashanTeamInfo.fight', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='victory', full_name='Message.S2CHuashanTeamInfo.victory', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conwins', full_name='Message.S2CHuashanTeamInfo.conwins', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Message.S2CHuashanTeamInfo.level', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='records', full_name='Message.S2CHuashanTeamInfo.records', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=358,
  serialized_end=532,
)

_S2CHUASHANTOPLIST.fields_by_name['teamlist'].message_type = _HUASHANTEAM
_S2CHUASHANTEAMINFO.fields_by_name['records'].message_type = _HUASHANRECORD
DESCRIPTOR.message_types_by_name['HuashanTeam'] = _HUASHANTEAM
DESCRIPTOR.message_types_by_name['HuashanRecord'] = _HUASHANRECORD
DESCRIPTOR.message_types_by_name['C2SHuashanEnter'] = _C2SHUASHANENTER
DESCRIPTOR.message_types_by_name['C2SHuashanQuit'] = _C2SHUASHANQUIT
DESCRIPTOR.message_types_by_name['C2SHuashanMatch'] = _C2SHUASHANMATCH
DESCRIPTOR.message_types_by_name['C2SHuashanToplist'] = _C2SHUASHANTOPLIST
DESCRIPTOR.message_types_by_name['S2CHuashanToplist'] = _S2CHUASHANTOPLIST
DESCRIPTOR.message_types_by_name['S2CHuashanTeamInfo'] = _S2CHUASHANTEAMINFO

HuashanTeam = _reflection.GeneratedProtocolMessageType('HuashanTeam', (_message.Message,), dict(
  DESCRIPTOR = _HUASHANTEAM,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.HuashanTeam)
  ))
_sym_db.RegisterMessage(HuashanTeam)

HuashanRecord = _reflection.GeneratedProtocolMessageType('HuashanRecord', (_message.Message,), dict(
  DESCRIPTOR = _HUASHANRECORD,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.HuashanRecord)
  ))
_sym_db.RegisterMessage(HuashanRecord)

C2SHuashanEnter = _reflection.GeneratedProtocolMessageType('C2SHuashanEnter', (_message.Message,), dict(
  DESCRIPTOR = _C2SHUASHANENTER,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SHuashanEnter)
  ))
_sym_db.RegisterMessage(C2SHuashanEnter)

C2SHuashanQuit = _reflection.GeneratedProtocolMessageType('C2SHuashanQuit', (_message.Message,), dict(
  DESCRIPTOR = _C2SHUASHANQUIT,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SHuashanQuit)
  ))
_sym_db.RegisterMessage(C2SHuashanQuit)

C2SHuashanMatch = _reflection.GeneratedProtocolMessageType('C2SHuashanMatch', (_message.Message,), dict(
  DESCRIPTOR = _C2SHUASHANMATCH,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SHuashanMatch)
  ))
_sym_db.RegisterMessage(C2SHuashanMatch)

C2SHuashanToplist = _reflection.GeneratedProtocolMessageType('C2SHuashanToplist', (_message.Message,), dict(
  DESCRIPTOR = _C2SHUASHANTOPLIST,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SHuashanToplist)
  ))
_sym_db.RegisterMessage(C2SHuashanToplist)

S2CHuashanToplist = _reflection.GeneratedProtocolMessageType('S2CHuashanToplist', (_message.Message,), dict(
  DESCRIPTOR = _S2CHUASHANTOPLIST,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CHuashanToplist)
  ))
_sym_db.RegisterMessage(S2CHuashanToplist)

S2CHuashanTeamInfo = _reflection.GeneratedProtocolMessageType('S2CHuashanTeamInfo', (_message.Message,), dict(
  DESCRIPTOR = _S2CHUASHANTEAMINFO,
  __module__ = 'MessageHuashan_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CHuashanTeamInfo)
  ))
_sym_db.RegisterMessage(S2CHuashanTeamInfo)


# @@protoc_insertion_point(module_scope)