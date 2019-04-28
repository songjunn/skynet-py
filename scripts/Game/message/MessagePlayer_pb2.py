# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessagePlayer.proto

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
  name='MessagePlayer.proto',
  package='Message',
  serialized_pb=_b('\n\x13MessagePlayer.proto\x12\x07Message\"A\n\x0f\x43\x32SPlayerCreate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06gender\x18\x02 \x01(\x05\x12\x10\n\x08vocation\x18\x03 \x01(\x05\"\x1d\n\x0e\x43\x32SPlayerLogin\x12\x0b\n\x03pid\x18\x01 \x01(\t\"\x11\n\x0f\x43\x32SPlayerLogout\"\x10\n\x0eS2CPlayerLogin\"\x94\x03\n\rS2CPlayerInfo\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08vocation\x18\x03 \x01(\x05\x12\x0e\n\x06gender\x18\x04 \x01(\x05\x12\r\n\x05level\x18\x05 \x01(\x05\x12\x10\n\x08goldcoin\x18\x06 \x01(\x05\x12\x12\n\nsilvercoin\x18\x07 \x01(\x05\x12\x12\n\ncoppercoin\x18\x08 \x01(\x05\x12\x0b\n\x03\x65xp\x18\t \x01(\x05\x12\x0f\n\x07readexp\x18\n \x01(\x05\x12\r\n\x05scene\x18\x0b \x01(\x05\x12\x0c\n\x04posx\x18\x0c \x01(\x05\x12\x0c\n\x04posy\x18\r \x01(\x05\x12\r\n\x05hpmax\x18\x0e \x01(\x05\x12\x12\n\nphysattack\x18\x0f \x01(\x05\x12\x13\n\x0bmagicattack\x18\x10 \x01(\x05\x12\x12\n\nphysdefend\x18\x11 \x01(\x05\x12\x13\n\x0bmagicdefend\x18\x12 \x01(\x05\x12\r\n\x05speed\x18\x13 \x01(\x05\x12\r\n\x05treat\x18\x14 \x01(\x05\x12\x0f\n\x07sealhit\x18\x15 \x01(\x05\x12\x12\n\nsealresist\x18\x16 \x01(\x05\x12\x10\n\x08\x66ighting\x18\x17 \x01(\x05\"\x9e\x01\n\x11S2CPlayerGetThing\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0f\n\x07tidlist\x18\x02 \x03(\x05\x12\x12\n\ntidnumlist\x18\x03 \x03(\x05\x12\x0b\n\x03\x65xp\x18\x04 \x01(\x05\x12\x10\n\x08goldcoin\x18\x05 \x01(\x05\x12\x12\n\nsilvercoin\x18\x06 \x01(\x05\x12\x12\n\ncoppercoin\x18\x07 \x01(\x05\x12\x0f\n\x07readexp\x18\x08 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2SPLAYERCREATE = _descriptor.Descriptor(
  name='C2SPlayerCreate',
  full_name='Message.C2SPlayerCreate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Message.C2SPlayerCreate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='Message.C2SPlayerCreate.gender', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocation', full_name='Message.C2SPlayerCreate.vocation', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=32,
  serialized_end=97,
)


_C2SPLAYERLOGIN = _descriptor.Descriptor(
  name='C2SPlayerLogin',
  full_name='Message.C2SPlayerLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Message.C2SPlayerLogin.pid', index=0,
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
  serialized_start=99,
  serialized_end=128,
)


_C2SPLAYERLOGOUT = _descriptor.Descriptor(
  name='C2SPlayerLogout',
  full_name='Message.C2SPlayerLogout',
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
  serialized_start=130,
  serialized_end=147,
)


_S2CPLAYERLOGIN = _descriptor.Descriptor(
  name='S2CPlayerLogin',
  full_name='Message.S2CPlayerLogin',
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
  serialized_start=149,
  serialized_end=165,
)


_S2CPLAYERINFO = _descriptor.Descriptor(
  name='S2CPlayerInfo',
  full_name='Message.S2CPlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Message.S2CPlayerInfo.pid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Message.S2CPlayerInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocation', full_name='Message.S2CPlayerInfo.vocation', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='Message.S2CPlayerInfo.gender', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Message.S2CPlayerInfo.level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goldcoin', full_name='Message.S2CPlayerInfo.goldcoin', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='silvercoin', full_name='Message.S2CPlayerInfo.silvercoin', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coppercoin', full_name='Message.S2CPlayerInfo.coppercoin', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='Message.S2CPlayerInfo.exp', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readexp', full_name='Message.S2CPlayerInfo.readexp', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scene', full_name='Message.S2CPlayerInfo.scene', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posx', full_name='Message.S2CPlayerInfo.posx', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posy', full_name='Message.S2CPlayerInfo.posy', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hpmax', full_name='Message.S2CPlayerInfo.hpmax', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physattack', full_name='Message.S2CPlayerInfo.physattack', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magicattack', full_name='Message.S2CPlayerInfo.magicattack', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physdefend', full_name='Message.S2CPlayerInfo.physdefend', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magicdefend', full_name='Message.S2CPlayerInfo.magicdefend', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='Message.S2CPlayerInfo.speed', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='treat', full_name='Message.S2CPlayerInfo.treat', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sealhit', full_name='Message.S2CPlayerInfo.sealhit', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sealresist', full_name='Message.S2CPlayerInfo.sealresist', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fighting', full_name='Message.S2CPlayerInfo.fighting', index=22,
      number=23, type=5, cpp_type=1, label=1,
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
  serialized_start=168,
  serialized_end=572,
)


_S2CPLAYERGETTHING = _descriptor.Descriptor(
  name='S2CPlayerGetThing',
  full_name='Message.S2CPlayerGetThing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.S2CPlayerGetThing.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tidlist', full_name='Message.S2CPlayerGetThing.tidlist', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tidnumlist', full_name='Message.S2CPlayerGetThing.tidnumlist', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='Message.S2CPlayerGetThing.exp', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goldcoin', full_name='Message.S2CPlayerGetThing.goldcoin', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='silvercoin', full_name='Message.S2CPlayerGetThing.silvercoin', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coppercoin', full_name='Message.S2CPlayerGetThing.coppercoin', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readexp', full_name='Message.S2CPlayerGetThing.readexp', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=575,
  serialized_end=733,
)

DESCRIPTOR.message_types_by_name['C2SPlayerCreate'] = _C2SPLAYERCREATE
DESCRIPTOR.message_types_by_name['C2SPlayerLogin'] = _C2SPLAYERLOGIN
DESCRIPTOR.message_types_by_name['C2SPlayerLogout'] = _C2SPLAYERLOGOUT
DESCRIPTOR.message_types_by_name['S2CPlayerLogin'] = _S2CPLAYERLOGIN
DESCRIPTOR.message_types_by_name['S2CPlayerInfo'] = _S2CPLAYERINFO
DESCRIPTOR.message_types_by_name['S2CPlayerGetThing'] = _S2CPLAYERGETTHING

C2SPlayerCreate = _reflection.GeneratedProtocolMessageType('C2SPlayerCreate', (_message.Message,), dict(
  DESCRIPTOR = _C2SPLAYERCREATE,
  __module__ = 'MessagePlayer_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SPlayerCreate)
  ))
_sym_db.RegisterMessage(C2SPlayerCreate)

C2SPlayerLogin = _reflection.GeneratedProtocolMessageType('C2SPlayerLogin', (_message.Message,), dict(
  DESCRIPTOR = _C2SPLAYERLOGIN,
  __module__ = 'MessagePlayer_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SPlayerLogin)
  ))
_sym_db.RegisterMessage(C2SPlayerLogin)

C2SPlayerLogout = _reflection.GeneratedProtocolMessageType('C2SPlayerLogout', (_message.Message,), dict(
  DESCRIPTOR = _C2SPLAYERLOGOUT,
  __module__ = 'MessagePlayer_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SPlayerLogout)
  ))
_sym_db.RegisterMessage(C2SPlayerLogout)

S2CPlayerLogin = _reflection.GeneratedProtocolMessageType('S2CPlayerLogin', (_message.Message,), dict(
  DESCRIPTOR = _S2CPLAYERLOGIN,
  __module__ = 'MessagePlayer_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CPlayerLogin)
  ))
_sym_db.RegisterMessage(S2CPlayerLogin)

S2CPlayerInfo = _reflection.GeneratedProtocolMessageType('S2CPlayerInfo', (_message.Message,), dict(
  DESCRIPTOR = _S2CPLAYERINFO,
  __module__ = 'MessagePlayer_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CPlayerInfo)
  ))
_sym_db.RegisterMessage(S2CPlayerInfo)

S2CPlayerGetThing = _reflection.GeneratedProtocolMessageType('S2CPlayerGetThing', (_message.Message,), dict(
  DESCRIPTOR = _S2CPLAYERGETTHING,
  __module__ = 'MessagePlayer_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CPlayerGetThing)
  ))
_sym_db.RegisterMessage(S2CPlayerGetThing)


# @@protoc_insertion_point(module_scope)
