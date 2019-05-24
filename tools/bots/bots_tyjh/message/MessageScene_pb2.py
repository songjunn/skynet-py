# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageScene.proto

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
  name='MessageScene.proto',
  package='Message',
  serialized_pb=_b('\n\x12MessageScene.proto\x12\x07Message\"5\n\x08SceneNpc\x12\r\n\x05mapid\x18\x01 \x01(\x05\x12\x0c\n\x04posx\x18\x02 \x01(\x05\x12\x0c\n\x04posy\x18\x03 \x01(\x05\"D\n\x0bScenePlayer\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04posx\x18\x03 \x01(\x05\x12\x0c\n\x04posy\x18\x04 \x01(\x05\"P\n\tSceneMove\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\x0c\n\x04srcx\x18\x02 \x01(\x05\x12\x0c\n\x04srcy\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x65sx\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x65sy\x18\x05 \x01(\x05\"*\n\x0c\x43\x32SSceneMove\x12\x0c\n\x04\x64\x65sx\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sy\x18\x02 \x01(\x05\";\n\x0e\x43\x32SSceneSwitch\x12\r\n\x05scene\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sx\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x65sy\x18\x03 \x01(\x05\"4\n\x0cS2CSceneMove\x12$\n\x08movement\x18\x01 \x01(\x0b\x32\x12.Message.SceneMove\"1\n\x0bS2CSceneNpc\x12\"\n\x07npclist\x18\x01 \x03(\x0b\x32\x11.Message.SceneNpc\":\n\x0eS2CScenePlayer\x12(\n\nplayerlist\x18\x01 \x03(\x0b\x32\x14.Message.ScenePlayer\"\xd3\x01\n\rS2CSceneEvent\x12)\n\x0b\x65nterplayer\x18\x01 \x03(\x0b\x32\x14.Message.ScenePlayer\x12(\n\nquitplayer\x18\x02 \x03(\x0b\x32\x14.Message.ScenePlayer\x12#\n\x08\x65nternpc\x18\x03 \x03(\x0b\x32\x11.Message.SceneNpc\x12\"\n\x07quitnpc\x18\x04 \x03(\x0b\x32\x11.Message.SceneNpc\x12$\n\x08movement\x18\x05 \x03(\x0b\x32\x12.Message.SceneMove\":\n\rS2CSceneEnter\x12\r\n\x05scene\x18\x01 \x01(\x05\x12\x0c\n\x04posx\x18\x02 \x01(\x05\x12\x0c\n\x04posy\x18\x03 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SCENENPC = _descriptor.Descriptor(
  name='SceneNpc',
  full_name='Message.SceneNpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mapid', full_name='Message.SceneNpc.mapid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posx', full_name='Message.SceneNpc.posx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posy', full_name='Message.SceneNpc.posy', index=2,
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
  serialized_start=31,
  serialized_end=84,
)


_SCENEPLAYER = _descriptor.Descriptor(
  name='ScenePlayer',
  full_name='Message.ScenePlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Message.ScenePlayer.pid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Message.ScenePlayer.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posx', full_name='Message.ScenePlayer.posx', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posy', full_name='Message.ScenePlayer.posy', index=3,
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
  serialized_start=86,
  serialized_end=154,
)


_SCENEMOVE = _descriptor.Descriptor(
  name='SceneMove',
  full_name='Message.SceneMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='Message.SceneMove.pid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='srcx', full_name='Message.SceneMove.srcx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='srcy', full_name='Message.SceneMove.srcy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desx', full_name='Message.SceneMove.desx', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desy', full_name='Message.SceneMove.desy', index=4,
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
  serialized_start=156,
  serialized_end=236,
)


_C2SSCENEMOVE = _descriptor.Descriptor(
  name='C2SSceneMove',
  full_name='Message.C2SSceneMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desx', full_name='Message.C2SSceneMove.desx', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desy', full_name='Message.C2SSceneMove.desy', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=238,
  serialized_end=280,
)


_C2SSCENESWITCH = _descriptor.Descriptor(
  name='C2SSceneSwitch',
  full_name='Message.C2SSceneSwitch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene', full_name='Message.C2SSceneSwitch.scene', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desx', full_name='Message.C2SSceneSwitch.desx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desy', full_name='Message.C2SSceneSwitch.desy', index=2,
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
  serialized_start=282,
  serialized_end=341,
)


_S2CSCENEMOVE = _descriptor.Descriptor(
  name='S2CSceneMove',
  full_name='Message.S2CSceneMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='movement', full_name='Message.S2CSceneMove.movement', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=343,
  serialized_end=395,
)


_S2CSCENENPC = _descriptor.Descriptor(
  name='S2CSceneNpc',
  full_name='Message.S2CSceneNpc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='npclist', full_name='Message.S2CSceneNpc.npclist', index=0,
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
  serialized_start=397,
  serialized_end=446,
)


_S2CSCENEPLAYER = _descriptor.Descriptor(
  name='S2CScenePlayer',
  full_name='Message.S2CScenePlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerlist', full_name='Message.S2CScenePlayer.playerlist', index=0,
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
  serialized_start=448,
  serialized_end=506,
)


_S2CSCENEEVENT = _descriptor.Descriptor(
  name='S2CSceneEvent',
  full_name='Message.S2CSceneEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enterplayer', full_name='Message.S2CSceneEvent.enterplayer', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quitplayer', full_name='Message.S2CSceneEvent.quitplayer', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enternpc', full_name='Message.S2CSceneEvent.enternpc', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quitnpc', full_name='Message.S2CSceneEvent.quitnpc', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='movement', full_name='Message.S2CSceneEvent.movement', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=509,
  serialized_end=720,
)


_S2CSCENEENTER = _descriptor.Descriptor(
  name='S2CSceneEnter',
  full_name='Message.S2CSceneEnter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene', full_name='Message.S2CSceneEnter.scene', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posx', full_name='Message.S2CSceneEnter.posx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posy', full_name='Message.S2CSceneEnter.posy', index=2,
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
  serialized_start=722,
  serialized_end=780,
)

_S2CSCENEMOVE.fields_by_name['movement'].message_type = _SCENEMOVE
_S2CSCENENPC.fields_by_name['npclist'].message_type = _SCENENPC
_S2CSCENEPLAYER.fields_by_name['playerlist'].message_type = _SCENEPLAYER
_S2CSCENEEVENT.fields_by_name['enterplayer'].message_type = _SCENEPLAYER
_S2CSCENEEVENT.fields_by_name['quitplayer'].message_type = _SCENEPLAYER
_S2CSCENEEVENT.fields_by_name['enternpc'].message_type = _SCENENPC
_S2CSCENEEVENT.fields_by_name['quitnpc'].message_type = _SCENENPC
_S2CSCENEEVENT.fields_by_name['movement'].message_type = _SCENEMOVE
DESCRIPTOR.message_types_by_name['SceneNpc'] = _SCENENPC
DESCRIPTOR.message_types_by_name['ScenePlayer'] = _SCENEPLAYER
DESCRIPTOR.message_types_by_name['SceneMove'] = _SCENEMOVE
DESCRIPTOR.message_types_by_name['C2SSceneMove'] = _C2SSCENEMOVE
DESCRIPTOR.message_types_by_name['C2SSceneSwitch'] = _C2SSCENESWITCH
DESCRIPTOR.message_types_by_name['S2CSceneMove'] = _S2CSCENEMOVE
DESCRIPTOR.message_types_by_name['S2CSceneNpc'] = _S2CSCENENPC
DESCRIPTOR.message_types_by_name['S2CScenePlayer'] = _S2CSCENEPLAYER
DESCRIPTOR.message_types_by_name['S2CSceneEvent'] = _S2CSCENEEVENT
DESCRIPTOR.message_types_by_name['S2CSceneEnter'] = _S2CSCENEENTER

SceneNpc = _reflection.GeneratedProtocolMessageType('SceneNpc', (_message.Message,), dict(
  DESCRIPTOR = _SCENENPC,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.SceneNpc)
  ))
_sym_db.RegisterMessage(SceneNpc)

ScenePlayer = _reflection.GeneratedProtocolMessageType('ScenePlayer', (_message.Message,), dict(
  DESCRIPTOR = _SCENEPLAYER,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.ScenePlayer)
  ))
_sym_db.RegisterMessage(ScenePlayer)

SceneMove = _reflection.GeneratedProtocolMessageType('SceneMove', (_message.Message,), dict(
  DESCRIPTOR = _SCENEMOVE,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.SceneMove)
  ))
_sym_db.RegisterMessage(SceneMove)

C2SSceneMove = _reflection.GeneratedProtocolMessageType('C2SSceneMove', (_message.Message,), dict(
  DESCRIPTOR = _C2SSCENEMOVE,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SSceneMove)
  ))
_sym_db.RegisterMessage(C2SSceneMove)

C2SSceneSwitch = _reflection.GeneratedProtocolMessageType('C2SSceneSwitch', (_message.Message,), dict(
  DESCRIPTOR = _C2SSCENESWITCH,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.C2SSceneSwitch)
  ))
_sym_db.RegisterMessage(C2SSceneSwitch)

S2CSceneMove = _reflection.GeneratedProtocolMessageType('S2CSceneMove', (_message.Message,), dict(
  DESCRIPTOR = _S2CSCENEMOVE,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CSceneMove)
  ))
_sym_db.RegisterMessage(S2CSceneMove)

S2CSceneNpc = _reflection.GeneratedProtocolMessageType('S2CSceneNpc', (_message.Message,), dict(
  DESCRIPTOR = _S2CSCENENPC,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CSceneNpc)
  ))
_sym_db.RegisterMessage(S2CSceneNpc)

S2CScenePlayer = _reflection.GeneratedProtocolMessageType('S2CScenePlayer', (_message.Message,), dict(
  DESCRIPTOR = _S2CSCENEPLAYER,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CScenePlayer)
  ))
_sym_db.RegisterMessage(S2CScenePlayer)

S2CSceneEvent = _reflection.GeneratedProtocolMessageType('S2CSceneEvent', (_message.Message,), dict(
  DESCRIPTOR = _S2CSCENEEVENT,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CSceneEvent)
  ))
_sym_db.RegisterMessage(S2CSceneEvent)

S2CSceneEnter = _reflection.GeneratedProtocolMessageType('S2CSceneEnter', (_message.Message,), dict(
  DESCRIPTOR = _S2CSCENEENTER,
  __module__ = 'MessageScene_pb2'
  # @@protoc_insertion_point(class_scope:Message.S2CSceneEnter)
  ))
_sym_db.RegisterMessage(S2CSceneEnter)


# @@protoc_insertion_point(module_scope)
