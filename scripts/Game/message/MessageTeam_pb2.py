# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageTeam.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MessageTeam.proto',
  package='',
  serialized_pb=_b('\n\x11MessageTeam.proto\"\x1d\n\rC2SCreateTeam\x12\x0c\n\x04type\x18\x01 \x02(\x05\"\x1b\n\x0c\x43\x32SApplyTeam\x12\x0b\n\x03pid\x18\x01 \x02(\t\",\n\x0cS2CApplyTeam\x12\x1c\n\x07\x61pplyer\x18\x01 \x02(\x0b\x32\x0b.MemberInfo\"*\n\x0e\x43\x32SApplyResult\x12\x0b\n\x03pid\x18\x01 \x02(\t\x12\x0b\n\x03ret\x18\x02 \x02(\x08\"\x1c\n\rC2SInviteTeam\x12\x0b\n\x03pid\x18\x01 \x02(\t\".\n\rS2CInviteTeam\x12\x0f\n\x07team_id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\"/\n\x0f\x43\x32SInviteResult\x12\x0f\n\x07team_id\x18\x01 \x02(\x05\x12\x0b\n\x03ret\x18\x02 \x02(\x08\"\r\n\x0b\x43\x32SQuitTeam\"\x1a\n\x0b\x43\x32SKickTeam\x12\x0b\n\x03pid\x18\x01 \x02(\t\"\x1c\n\x0cS2CLeaveTeam\x12\x0c\n\x04type\x18\x01 \x02(\x05\"\x11\n\x0f\x43\x32SDissolveTeam\"\x1a\n\x0b\x43\x32SGiveTeam\x12\x0b\n\x03pid\x18\x01 \x02(\t\"F\n\x0bS2CGiveTeam\x12\x0f\n\x07team_id\x18\x01 \x02(\x05\x12\x11\n\tleader_id\x18\x02 \x02(\t\x12\x13\n\x0bleader_name\x18\x03 \x02(\t\"D\n\x11\x43\x32SGiveTeamResult\x12\x0f\n\x07team_id\x18\x01 \x02(\x05\x12\x11\n\tleader_id\x18\x02 \x02(\t\x12\x0b\n\x03ret\x18\x03 \x02(\x08\"\x10\n\x0e\x43\x32SReplaceTeam\"/\n\x11\x43\x32SChangeTeamInfo\x12\x0b\n\x03\x66id\x18\x01 \x02(\x05\x12\r\n\x05\x61pply\x18\x02 \x02(\x05\"\x96\x01\n\nMemberInfo\x12\x0b\n\x03pid\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x10\n\x08vocation\x18\x03 \x02(\x05\x12\x0e\n\x06vlevel\x18\x04 \x02(\x05\x12\x0e\n\x06gender\x18\x05 \x02(\x05\x12\r\n\x05level\x18\x06 \x02(\x05\x12\r\n\x05power\x18\x07 \x02(\x05\x12\x0e\n\x06status\x18\x08 \x02(\x05\x12\r\n\x05title\x18\t \x02(\x05\"\x96\x01\n\x0bS2CTeamInfo\x12 \n\x0bmember_list\x18\x01 \x03(\x0b\x32\x0b.MemberInfo\x12\x11\n\tformation\x18\x02 \x02(\x05\x12\r\n\x05\x61pply\x18\x03 \x02(\x08\x12\r\n\x05isnew\x18\x04 \x01(\x08\x12\x10\n\x08join_pid\x18\x05 \x01(\t\x12\x10\n\x08quit_pid\x18\x06 \x01(\t\x12\x10\n\x08kick_pid\x18\x07 \x01(\t\")\n\x0bS2CTeamMove\x12\x0c\n\x04posx\x18\x01 \x02(\x05\x12\x0c\n\x04posy\x18\x02 \x02(\x05*>\n\tLeaveType\x12\r\n\tQuit_Team\x10\x01\x12\x0f\n\x0bKicked_Team\x10\x02\x12\x11\n\rDissolve_Team\x10\x03*L\n\x0cMemberStatus\x12\x0b\n\x07NO_TEAM\x10\x00\x12\x0f\n\x0b\x46OLLOW_TEAM\x10\x01\x12\x11\n\rWAIT_COMEBACK\x10\x02\x12\x0b\n\x07OFFLINE\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LEAVETYPE = _descriptor.EnumDescriptor(
  name='LeaveType',
  full_name='LeaveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Quit_Team', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Kicked_Team', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Dissolve_Team', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=976,
  serialized_end=1038,
)
_sym_db.RegisterEnumDescriptor(_LEAVETYPE)

LeaveType = enum_type_wrapper.EnumTypeWrapper(_LEAVETYPE)
_MEMBERSTATUS = _descriptor.EnumDescriptor(
  name='MemberStatus',
  full_name='MemberStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_TEAM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW_TEAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAIT_COMEBACK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1040,
  serialized_end=1116,
)
_sym_db.RegisterEnumDescriptor(_MEMBERSTATUS)

MemberStatus = enum_type_wrapper.EnumTypeWrapper(_MEMBERSTATUS)
Quit_Team = 1
Kicked_Team = 2
Dissolve_Team = 3
NO_TEAM = 0
FOLLOW_TEAM = 1
WAIT_COMEBACK = 2
OFFLINE = 3



_C2SCREATETEAM = _descriptor.Descriptor(
  name='C2SCreateTeam',
  full_name='C2SCreateTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='C2SCreateTeam.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=21,
  serialized_end=50,
)


_C2SAPPLYTEAM = _descriptor.Descriptor(
  name='C2SApplyTeam',
  full_name='C2SApplyTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='C2SApplyTeam.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=52,
  serialized_end=79,
)


_S2CAPPLYTEAM = _descriptor.Descriptor(
  name='S2CApplyTeam',
  full_name='S2CApplyTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='applyer', full_name='S2CApplyTeam.applyer', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=81,
  serialized_end=125,
)


_C2SAPPLYRESULT = _descriptor.Descriptor(
  name='C2SApplyResult',
  full_name='C2SApplyResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='C2SApplyResult.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='C2SApplyResult.ret', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=127,
  serialized_end=169,
)


_C2SINVITETEAM = _descriptor.Descriptor(
  name='C2SInviteTeam',
  full_name='C2SInviteTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='C2SInviteTeam.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=171,
  serialized_end=199,
)


_S2CINVITETEAM = _descriptor.Descriptor(
  name='S2CInviteTeam',
  full_name='S2CInviteTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_id', full_name='S2CInviteTeam.team_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='S2CInviteTeam.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=201,
  serialized_end=247,
)


_C2SINVITERESULT = _descriptor.Descriptor(
  name='C2SInviteResult',
  full_name='C2SInviteResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_id', full_name='C2SInviteResult.team_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='C2SInviteResult.ret', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=249,
  serialized_end=296,
)


_C2SQUITTEAM = _descriptor.Descriptor(
  name='C2SQuitTeam',
  full_name='C2SQuitTeam',
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
  serialized_start=298,
  serialized_end=311,
)


_C2SKICKTEAM = _descriptor.Descriptor(
  name='C2SKickTeam',
  full_name='C2SKickTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='C2SKickTeam.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=313,
  serialized_end=339,
)


_S2CLEAVETEAM = _descriptor.Descriptor(
  name='S2CLeaveTeam',
  full_name='S2CLeaveTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='S2CLeaveTeam.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=341,
  serialized_end=369,
)


_C2SDISSOLVETEAM = _descriptor.Descriptor(
  name='C2SDissolveTeam',
  full_name='C2SDissolveTeam',
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
  serialized_start=371,
  serialized_end=388,
)


_C2SGIVETEAM = _descriptor.Descriptor(
  name='C2SGiveTeam',
  full_name='C2SGiveTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='C2SGiveTeam.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=390,
  serialized_end=416,
)


_S2CGIVETEAM = _descriptor.Descriptor(
  name='S2CGiveTeam',
  full_name='S2CGiveTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_id', full_name='S2CGiveTeam.team_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leader_id', full_name='S2CGiveTeam.leader_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leader_name', full_name='S2CGiveTeam.leader_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=418,
  serialized_end=488,
)


_C2SGIVETEAMRESULT = _descriptor.Descriptor(
  name='C2SGiveTeamResult',
  full_name='C2SGiveTeamResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_id', full_name='C2SGiveTeamResult.team_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leader_id', full_name='C2SGiveTeamResult.leader_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='C2SGiveTeamResult.ret', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=490,
  serialized_end=558,
)


_C2SREPLACETEAM = _descriptor.Descriptor(
  name='C2SReplaceTeam',
  full_name='C2SReplaceTeam',
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
  serialized_start=560,
  serialized_end=576,
)


_C2SCHANGETEAMINFO = _descriptor.Descriptor(
  name='C2SChangeTeamInfo',
  full_name='C2SChangeTeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fid', full_name='C2SChangeTeamInfo.fid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply', full_name='C2SChangeTeamInfo.apply', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=578,
  serialized_end=625,
)


_MEMBERINFO = _descriptor.Descriptor(
  name='MemberInfo',
  full_name='MemberInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='MemberInfo.pid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='MemberInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vocation', full_name='MemberInfo.vocation', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vlevel', full_name='MemberInfo.vlevel', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='MemberInfo.gender', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='MemberInfo.level', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='MemberInfo.power', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='MemberInfo.status', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='MemberInfo.title', index=8,
      number=9, type=5, cpp_type=1, label=2,
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
  serialized_start=628,
  serialized_end=778,
)


_S2CTEAMINFO = _descriptor.Descriptor(
  name='S2CTeamInfo',
  full_name='S2CTeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member_list', full_name='S2CTeamInfo.member_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='formation', full_name='S2CTeamInfo.formation', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply', full_name='S2CTeamInfo.apply', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isnew', full_name='S2CTeamInfo.isnew', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='join_pid', full_name='S2CTeamInfo.join_pid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quit_pid', full_name='S2CTeamInfo.quit_pid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kick_pid', full_name='S2CTeamInfo.kick_pid', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=781,
  serialized_end=931,
)


_S2CTEAMMOVE = _descriptor.Descriptor(
  name='S2CTeamMove',
  full_name='S2CTeamMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='posx', full_name='S2CTeamMove.posx', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posy', full_name='S2CTeamMove.posy', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=933,
  serialized_end=974,
)

_S2CAPPLYTEAM.fields_by_name['applyer'].message_type = _MEMBERINFO
_S2CTEAMINFO.fields_by_name['member_list'].message_type = _MEMBERINFO
DESCRIPTOR.message_types_by_name['C2SCreateTeam'] = _C2SCREATETEAM
DESCRIPTOR.message_types_by_name['C2SApplyTeam'] = _C2SAPPLYTEAM
DESCRIPTOR.message_types_by_name['S2CApplyTeam'] = _S2CAPPLYTEAM
DESCRIPTOR.message_types_by_name['C2SApplyResult'] = _C2SAPPLYRESULT
DESCRIPTOR.message_types_by_name['C2SInviteTeam'] = _C2SINVITETEAM
DESCRIPTOR.message_types_by_name['S2CInviteTeam'] = _S2CINVITETEAM
DESCRIPTOR.message_types_by_name['C2SInviteResult'] = _C2SINVITERESULT
DESCRIPTOR.message_types_by_name['C2SQuitTeam'] = _C2SQUITTEAM
DESCRIPTOR.message_types_by_name['C2SKickTeam'] = _C2SKICKTEAM
DESCRIPTOR.message_types_by_name['S2CLeaveTeam'] = _S2CLEAVETEAM
DESCRIPTOR.message_types_by_name['C2SDissolveTeam'] = _C2SDISSOLVETEAM
DESCRIPTOR.message_types_by_name['C2SGiveTeam'] = _C2SGIVETEAM
DESCRIPTOR.message_types_by_name['S2CGiveTeam'] = _S2CGIVETEAM
DESCRIPTOR.message_types_by_name['C2SGiveTeamResult'] = _C2SGIVETEAMRESULT
DESCRIPTOR.message_types_by_name['C2SReplaceTeam'] = _C2SREPLACETEAM
DESCRIPTOR.message_types_by_name['C2SChangeTeamInfo'] = _C2SCHANGETEAMINFO
DESCRIPTOR.message_types_by_name['MemberInfo'] = _MEMBERINFO
DESCRIPTOR.message_types_by_name['S2CTeamInfo'] = _S2CTEAMINFO
DESCRIPTOR.message_types_by_name['S2CTeamMove'] = _S2CTEAMMOVE
DESCRIPTOR.enum_types_by_name['LeaveType'] = _LEAVETYPE
DESCRIPTOR.enum_types_by_name['MemberStatus'] = _MEMBERSTATUS

C2SCreateTeam = _reflection.GeneratedProtocolMessageType('C2SCreateTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SCREATETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SCreateTeam)
  ))
_sym_db.RegisterMessage(C2SCreateTeam)

C2SApplyTeam = _reflection.GeneratedProtocolMessageType('C2SApplyTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SAPPLYTEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SApplyTeam)
  ))
_sym_db.RegisterMessage(C2SApplyTeam)

S2CApplyTeam = _reflection.GeneratedProtocolMessageType('S2CApplyTeam', (_message.Message,), dict(
  DESCRIPTOR = _S2CAPPLYTEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:S2CApplyTeam)
  ))
_sym_db.RegisterMessage(S2CApplyTeam)

C2SApplyResult = _reflection.GeneratedProtocolMessageType('C2SApplyResult', (_message.Message,), dict(
  DESCRIPTOR = _C2SAPPLYRESULT,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SApplyResult)
  ))
_sym_db.RegisterMessage(C2SApplyResult)

C2SInviteTeam = _reflection.GeneratedProtocolMessageType('C2SInviteTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SINVITETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SInviteTeam)
  ))
_sym_db.RegisterMessage(C2SInviteTeam)

S2CInviteTeam = _reflection.GeneratedProtocolMessageType('S2CInviteTeam', (_message.Message,), dict(
  DESCRIPTOR = _S2CINVITETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:S2CInviteTeam)
  ))
_sym_db.RegisterMessage(S2CInviteTeam)

C2SInviteResult = _reflection.GeneratedProtocolMessageType('C2SInviteResult', (_message.Message,), dict(
  DESCRIPTOR = _C2SINVITERESULT,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SInviteResult)
  ))
_sym_db.RegisterMessage(C2SInviteResult)

C2SQuitTeam = _reflection.GeneratedProtocolMessageType('C2SQuitTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SQUITTEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SQuitTeam)
  ))
_sym_db.RegisterMessage(C2SQuitTeam)

C2SKickTeam = _reflection.GeneratedProtocolMessageType('C2SKickTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SKICKTEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SKickTeam)
  ))
_sym_db.RegisterMessage(C2SKickTeam)

S2CLeaveTeam = _reflection.GeneratedProtocolMessageType('S2CLeaveTeam', (_message.Message,), dict(
  DESCRIPTOR = _S2CLEAVETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:S2CLeaveTeam)
  ))
_sym_db.RegisterMessage(S2CLeaveTeam)

C2SDissolveTeam = _reflection.GeneratedProtocolMessageType('C2SDissolveTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SDISSOLVETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SDissolveTeam)
  ))
_sym_db.RegisterMessage(C2SDissolveTeam)

C2SGiveTeam = _reflection.GeneratedProtocolMessageType('C2SGiveTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SGIVETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SGiveTeam)
  ))
_sym_db.RegisterMessage(C2SGiveTeam)

S2CGiveTeam = _reflection.GeneratedProtocolMessageType('S2CGiveTeam', (_message.Message,), dict(
  DESCRIPTOR = _S2CGIVETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:S2CGiveTeam)
  ))
_sym_db.RegisterMessage(S2CGiveTeam)

C2SGiveTeamResult = _reflection.GeneratedProtocolMessageType('C2SGiveTeamResult', (_message.Message,), dict(
  DESCRIPTOR = _C2SGIVETEAMRESULT,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SGiveTeamResult)
  ))
_sym_db.RegisterMessage(C2SGiveTeamResult)

C2SReplaceTeam = _reflection.GeneratedProtocolMessageType('C2SReplaceTeam', (_message.Message,), dict(
  DESCRIPTOR = _C2SREPLACETEAM,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SReplaceTeam)
  ))
_sym_db.RegisterMessage(C2SReplaceTeam)

C2SChangeTeamInfo = _reflection.GeneratedProtocolMessageType('C2SChangeTeamInfo', (_message.Message,), dict(
  DESCRIPTOR = _C2SCHANGETEAMINFO,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:C2SChangeTeamInfo)
  ))
_sym_db.RegisterMessage(C2SChangeTeamInfo)

MemberInfo = _reflection.GeneratedProtocolMessageType('MemberInfo', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERINFO,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:MemberInfo)
  ))
_sym_db.RegisterMessage(MemberInfo)

S2CTeamInfo = _reflection.GeneratedProtocolMessageType('S2CTeamInfo', (_message.Message,), dict(
  DESCRIPTOR = _S2CTEAMINFO,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:S2CTeamInfo)
  ))
_sym_db.RegisterMessage(S2CTeamInfo)

S2CTeamMove = _reflection.GeneratedProtocolMessageType('S2CTeamMove', (_message.Message,), dict(
  DESCRIPTOR = _S2CTEAMMOVE,
  __module__ = 'MessageTeam_pb2'
  # @@protoc_insertion_point(class_scope:S2CTeamMove)
  ))
_sym_db.RegisterMessage(S2CTeamMove)


# @@protoc_insertion_point(module_scope)
