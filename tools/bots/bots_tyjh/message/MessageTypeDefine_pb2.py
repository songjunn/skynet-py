# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageTypeDefine.proto

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
  name='MessageTypeDefine.proto',
  package='Message',
  serialized_pb=_b('\n\x17MessageTypeDefine.proto\x12\x07Message*\xe3\x18\n\tMsgDefine\x12\x11\n\rS2C_MSG_BEGIN\x10\x00\x12\x14\n\x10S2C_COMMON_ERROR\x10\x32\x12\x0f\n\x0bS2C_PAY_REQ\x10\x63\x12\x12\n\x0eS2C_USER_LOGIN\x10\x64\x12\x13\n\x0fS2C_USER_LOGOUT\x10\x65\x12\x16\n\x12S2C_USER_HEARTBEAT\x10\x66\x12\x14\n\x10S2C_PLAYER_LOGIN\x10g\x12\x13\n\x0fS2C_PLAYER_INFO\x10h\x12\x17\n\x13S2C_PLAYER_GETTHING\x10i\x12\x12\n\rS2C_PROP_LIST\x10\xc8\x01\x12\x13\n\x0eS2C_EQUIP_LIST\x10\xc9\x01\x12\x15\n\x10S2C_UNEQUIP_LIST\x10\xca\x01\x12\x15\n\x10S2C_PROP_COMPOSE\x10\xcb\x01\x12\x15\n\x10S2C_PROP_ENHANCE\x10\xcc\x01\x12\x15\n\x10S2C_ENHANCE_INFO\x10\xcd\x01\x12\x16\n\x11S2C_SHOPPING_INFO\x10\xce\x01\x12\r\n\x08S2C_CHAT\x10\xac\x02\x12\x14\n\x0fS2C_FRIEND_LIST\x10\xad\x02\x12\x12\n\rS2C_TASK_LIST\x10\xae\x02\x12\x18\n\x13S2C_SUITFRIEND_LIST\x10\xaf\x02\x12\x19\n\x14S2C_FRIENDAPPLY_LIST\x10\xb0\x02\x12\x16\n\x11S2C_ADDFRIEND_SUC\x10\xb1\x02\x12\x16\n\x11S2C_FRIEND_STATUS\x10\xb2\x02\x12\x17\n\x12S2C_TASK_SYNCSTORY\x10\xb3\x02\x12\x13\n\x0eS2C_SKILL_LIST\x10\xc0\x02\x12\x12\n\rS2C_BASE_GONG\x10\xc1\x02\x12\x13\n\x0eS2C_HEART_GONG\x10\xc2\x02\x12\x17\n\x12S2C_FIGHT_UNITLIST\x10\xca\x02\x12\x16\n\x11S2C_FIGHT_PROCESS\x10\xcb\x02\x12\x15\n\x10S2C_FIGHT_RESULT\x10\xcc\x02\x12\x13\n\x0eS2C_FIGHT_AUTO\x10\xcd\x02\x12\x12\n\rS2C_TEAM_INFO\x10\xde\x02\x12\x13\n\x0eS2C_TEAM_APPLY\x10\xdf\x02\x12\x14\n\x0fS2C_TEAM_INVITE\x10\xe0\x02\x12\x13\n\x0eS2C_TEAM_LEAVE\x10\xe1\x02\x12\x12\n\rS2C_TEAM_GIVE\x10\xe2\x02\x12\x12\n\rS2C_TEAM_MOVE\x10\xe3\x02\x12\x1a\n\x15S2C_TEAM_MEMBERSTATUS\x10\xe4\x02\x12\x12\n\rS2C_MAIL_LIST\x10\x90\x03\x12\x13\n\x0eS2C_SCENE_MOVE\x10\xf4\x03\x12\x12\n\rS2C_SCENE_NPC\x10\xf5\x03\x12\x15\n\x10S2C_SCENE_PLAYER\x10\xf6\x03\x12\x14\n\x0fS2C_SCENE_EVENT\x10\xf7\x03\x12\x14\n\x0fS2C_SCENE_ENTER\x10\xf8\x03\x12\x14\n\x0fS2C_PALACE_INFO\x10\xd8\x04\x12\x1a\n\x15S2C_PALACE_PLAYERINFO\x10\xd9\x04\x12\x17\n\x12S2C_TRAINROOM_INFO\x10\xe2\x04\x12\x11\n\x0cS2C_PET_INFO\x10\xbd\x05\x12\x11\n\x0cS2C_PET_LIST\x10\xbe\x05\x12\x19\n\x14S2C_ARENA_PLAYERINFO\x10\xa0\x06\x12\x19\n\x14S2C_ARENA_TARGETLIST\x10\xa1\x06\x12\x16\n\x11S2C_ARENA_TOPLIST\x10\xa2\x06\x12\x1a\n\x15S2C_ARENA_FIGHTRESULT\x10\xa3\x06\x12\x19\n\x14S2C_HUASHAN_TEAMINFO\x10\x84\x07\x12\x18\n\x13S2C_HUASHAN_TOPLIST\x10\x85\x07\x12\x13\n\x0eS2C_TOWER_INFO\x10\xe8\x07\x12\x16\n\x11S2C_RANKLIST_INFO\x10\xe9\x07\x12\x10\n\x0bS2C_MSG_END\x10\x8fN\x12\x12\n\rC2S_MSG_BEGIN\x10\x90N\x12\x14\n\x0f\x43\x32S_GUEST_LOGIN\x10\x91N\x12\x13\n\x0e\x43\x32S_USER_LOGIN\x10\x92N\x12\x14\n\x0f\x43\x32S_USER_LOGOUT\x10\x93N\x12\x17\n\x12\x43\x32S_USER_HEARTBEAT\x10\x94N\x12\x16\n\x11\x43\x32S_PLAYER_CREATE\x10\x95N\x12\x15\n\x10\x43\x32S_PLAYER_LOGIN\x10\x96N\x12\x16\n\x11\x43\x32S_PLAYER_LOGOUT\x10\x97N\x12\x15\n\x10\x43\x32S_PLAYER_GUIDE\x10\x98N\x12\x11\n\x0c\x43\x32S_PROP_USE\x10\xf4N\x12\x11\n\x0c\x43\x32S_PROP_BUY\x10\xf5N\x12\x12\n\rC2S_PROP_SELL\x10\xf6N\x12\x15\n\x10\x43\x32S_PROP_COMPOSE\x10\xf7N\x12\x17\n\x12\x43\x32S_PROP_DECOMPOSE\x10\xf8N\x12\x13\n\x0e\x43\x32S_PROP_EQUIP\x10\xf9N\x12\x15\n\x10\x43\x32S_PROP_UNEQUIP\x10\xfaN\x12\x14\n\x0f\x43\x32S_PROP_SETGEM\x10\xfbN\x12\x16\n\x11\x43\x32S_PROP_UNSETGEM\x10\xfcN\x12\x18\n\x13\x43\x32S_PROP_COMPOSEGEM\x10\xfdN\x12\x1d\n\x18\x43\x32S_PROP_COMPOSEEQUIPGEM\x10\xfeN\x12\x15\n\x10\x43\x32S_PROP_ENHANCE\x10\xffN\x12\x12\n\rC2S_MAIL_SEND\x10\xd8O\x12\x12\n\rC2S_MAIL_READ\x10\xd9O\x12\x14\n\x0f\x43\x32S_MAIL_DELETE\x10\xdaO\x12\x15\n\x10\x43\x32S_MAIL_EXTRACT\x10\xdbO\x12\r\n\x08\x43\x32S_CHAT\x10\xbcP\x12\x13\n\x0e\x43\x32S_FRIEND_ADD\x10\xbdP\x12\x16\n\x11\x43\x32S_FRIEND_DELETE\x10\xbeP\x12\x16\n\x11\x43\x32S_FRIEND_RESULT\x10\xbfP\x12\x14\n\x0f\x43\x32S_TASK_ACCEPT\x10\xc6P\x12\x14\n\x0f\x43\x32S_TASK_FINISH\x10\xc7P\x12\x14\n\x0f\x43\x32S_TASK_CANCEL\x10\xc8P\x12\x13\n\x0e\x43\x32S_TASK_FIGHT\x10\xc9P\x12\x17\n\x12\x43\x32S_TASK_SYNCSTORY\x10\xcaP\x12\x17\n\x12\x43\x32S_FIGHT_USESKILL\x10\xdaP\x12\x19\n\x14\x43\x32S_FIGHT_ROUNDREADY\x10\xdbP\x12\x16\n\x11\x43\x32S_SKILL_UPGRADE\x10\xdcP\x12\x1a\n\x15\x43\x32S_BASEGONG_ADDPOINT\x10\xddP\x12\x18\n\x13\x43\x32S_HEARTGONG_RESET\x10\xdeP\x12\x1a\n\x15\x43\x32S_HEARTGONG_UPGRADE\x10\xdfP\x12\x13\n\x0e\x43\x32S_FIGHT_AUTO\x10\xe0P\x12\x16\n\x11\x43\x32S_FIGHT_CALLPET\x10\xe1P\x12\x14\n\x0f\x43\x32S_TEAM_CREATE\x10\xe4P\x12\x13\n\x0e\x43\x32S_TEAM_APPLY\x10\xe5P\x12\x19\n\x14\x43\x32S_TEAM_APPLYRESULT\x10\xe6P\x12\x14\n\x0f\x43\x32S_TEAM_INVITE\x10\xe7P\x12\x1a\n\x15\x43\x32S_TEAM_INVITERESULT\x10\xe8P\x12\x12\n\rC2S_TEAM_QUIT\x10\xe9P\x12\x12\n\rC2S_TEAM_KICK\x10\xeaP\x12\x16\n\x11\x43\x32S_TEAM_DISSOLVE\x10\xebP\x12\x12\n\rC2S_TEAM_GIVE\x10\xecP\x12\x18\n\x13\x43\x32S_TEAM_GIVERESULT\x10\xedP\x12\x15\n\x10\x43\x32S_TEAM_REPLACE\x10\xeeP\x12\x17\n\x12\x43\x32S_TEAM_FORMATION\x10\xefP\x12\x19\n\x14\x43\x32S_TEAM_PLAYERMATCH\x10\xf0P\x12\x17\n\x12\x43\x32S_TEAM_TEAMMATCH\x10\xf1P\x12\x13\n\x0e\x43\x32S_SCENE_MOVE\x10\xa0Q\x12\x15\n\x10\x43\x32S_SCENE_SWITCH\x10\xa1Q\x12\x15\n\x10\x43\x32S_PALACE_ENTER\x10\xa2Q\x12\x14\n\x0f\x43\x32S_PALACE_QUIT\x10\xa3Q\x12\x16\n\x11\x43\x32S_PALACE_FINISH\x10\xa4Q\x12\x18\n\x13\x43\x32S_TRAINROOM_FIGHT\x10\xaaQ\x12\x18\n\x13\x43\x32S_TRAINROOM_ENTER\x10\xabQ\x12\x17\n\x12\x43\x32S_PET_UPGRADEQUA\x10\xf0Q\x12\x15\n\x10\x43\x32S_PET_SETFIGHT\x10\xf1Q\x12\x15\n\x10\x43\x32S_PET_EXCHANGE\x10\xf2Q\x12\x18\n\x13\x43\x32S_PET_UPGRADESTAR\x10\xf3Q\x12\x14\n\x0f\x43\x32S_ARENA_ENTER\x10\x84R\x12\x14\n\x0f\x43\x32S_ARENA_FIGHT\x10\x85R\x12\x16\n\x11\x43\x32S_ARENA_TOPLIST\x10\x86R\x12\x18\n\x13\x43\x32S_ARENA_RANKPRIZE\x10\x87R\x12\x16\n\x11\x43\x32S_HUASHAN_ENTER\x10\xe8R\x12\x15\n\x10\x43\x32S_HUASHAN_QUIT\x10\xe9R\x12\x18\n\x13\x43\x32S_HUASHAN_TOPLIST\x10\xeaR\x12\x16\n\x11\x43\x32S_HUASHAN_MATCH\x10\xebR\x12\x14\n\x0f\x43\x32S_TOWER_FIGHT\x10\x9aS\x12\x14\n\x0f\x43\x32S_TOWER_RESET\x10\x9bS\x12\x16\n\x11\x43\x32S_RANKLIST_INFO\x10\xccS\x12\x17\n\x11\x43\x32S_MSG_GMCOMMOND\x10\xaf\xea\x01\x12\x11\n\x0b\x43\x32S_MSG_END\x10\xb0\xea\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSGDEFINE = _descriptor.EnumDescriptor(
  name='MsgDefine',
  full_name='Message.MsgDefine',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='S2C_MSG_BEGIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_COMMON_ERROR', index=1, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PAY_REQ', index=2, number=99,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_USER_LOGIN', index=3, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_USER_LOGOUT', index=4, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_USER_HEARTBEAT', index=5, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PLAYER_LOGIN', index=6, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PLAYER_INFO', index=7, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PLAYER_GETTHING', index=8, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PROP_LIST', index=9, number=200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_EQUIP_LIST', index=10, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_UNEQUIP_LIST', index=11, number=202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PROP_COMPOSE', index=12, number=203,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PROP_ENHANCE', index=13, number=204,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_ENHANCE_INFO', index=14, number=205,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SHOPPING_INFO', index=15, number=206,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_CHAT', index=16, number=300,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FRIEND_LIST', index=17, number=301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TASK_LIST', index=18, number=302,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SUITFRIEND_LIST', index=19, number=303,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FRIENDAPPLY_LIST', index=20, number=304,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_ADDFRIEND_SUC', index=21, number=305,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FRIEND_STATUS', index=22, number=306,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TASK_SYNCSTORY', index=23, number=307,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SKILL_LIST', index=24, number=320,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_BASE_GONG', index=25, number=321,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_HEART_GONG', index=26, number=322,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FIGHT_UNITLIST', index=27, number=330,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FIGHT_PROCESS', index=28, number=331,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FIGHT_RESULT', index=29, number=332,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_FIGHT_AUTO', index=30, number=333,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_INFO', index=31, number=350,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_APPLY', index=32, number=351,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_INVITE', index=33, number=352,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_LEAVE', index=34, number=353,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_GIVE', index=35, number=354,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_MOVE', index=36, number=355,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TEAM_MEMBERSTATUS', index=37, number=356,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_MAIL_LIST', index=38, number=400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SCENE_MOVE', index=39, number=500,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SCENE_NPC', index=40, number=501,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SCENE_PLAYER', index=41, number=502,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SCENE_EVENT', index=42, number=503,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_SCENE_ENTER', index=43, number=504,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PALACE_INFO', index=44, number=600,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PALACE_PLAYERINFO', index=45, number=601,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TRAINROOM_INFO', index=46, number=610,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PET_INFO', index=47, number=701,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_PET_LIST', index=48, number=702,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_ARENA_PLAYERINFO', index=49, number=800,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_ARENA_TARGETLIST', index=50, number=801,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_ARENA_TOPLIST', index=51, number=802,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_ARENA_FIGHTRESULT', index=52, number=803,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_HUASHAN_TEAMINFO', index=53, number=900,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_HUASHAN_TOPLIST', index=54, number=901,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_TOWER_INFO', index=55, number=1000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_RANKLIST_INFO', index=56, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S2C_MSG_END', index=57, number=9999,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MSG_BEGIN', index=58, number=10000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_GUEST_LOGIN', index=59, number=10001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_USER_LOGIN', index=60, number=10002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_USER_LOGOUT', index=61, number=10003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_USER_HEARTBEAT', index=62, number=10004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PLAYER_CREATE', index=63, number=10005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PLAYER_LOGIN', index=64, number=10006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PLAYER_LOGOUT', index=65, number=10007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PLAYER_GUIDE', index=66, number=10008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_USE', index=67, number=10100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_BUY', index=68, number=10101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_SELL', index=69, number=10102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_COMPOSE', index=70, number=10103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_DECOMPOSE', index=71, number=10104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_EQUIP', index=72, number=10105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_UNEQUIP', index=73, number=10106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_SETGEM', index=74, number=10107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_UNSETGEM', index=75, number=10108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_COMPOSEGEM', index=76, number=10109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_COMPOSEEQUIPGEM', index=77, number=10110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PROP_ENHANCE', index=78, number=10111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MAIL_SEND', index=79, number=10200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MAIL_READ', index=80, number=10201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MAIL_DELETE', index=81, number=10202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MAIL_EXTRACT', index=82, number=10203,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_CHAT', index=83, number=10300,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FRIEND_ADD', index=84, number=10301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FRIEND_DELETE', index=85, number=10302,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FRIEND_RESULT', index=86, number=10303,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TASK_ACCEPT', index=87, number=10310,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TASK_FINISH', index=88, number=10311,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TASK_CANCEL', index=89, number=10312,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TASK_FIGHT', index=90, number=10313,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TASK_SYNCSTORY', index=91, number=10314,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FIGHT_USESKILL', index=92, number=10330,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FIGHT_ROUNDREADY', index=93, number=10331,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_SKILL_UPGRADE', index=94, number=10332,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_BASEGONG_ADDPOINT', index=95, number=10333,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_HEARTGONG_RESET', index=96, number=10334,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_HEARTGONG_UPGRADE', index=97, number=10335,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FIGHT_AUTO', index=98, number=10336,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_FIGHT_CALLPET', index=99, number=10337,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_CREATE', index=100, number=10340,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_APPLY', index=101, number=10341,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_APPLYRESULT', index=102, number=10342,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_INVITE', index=103, number=10343,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_INVITERESULT', index=104, number=10344,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_QUIT', index=105, number=10345,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_KICK', index=106, number=10346,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_DISSOLVE', index=107, number=10347,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_GIVE', index=108, number=10348,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_GIVERESULT', index=109, number=10349,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_REPLACE', index=110, number=10350,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_FORMATION', index=111, number=10351,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_PLAYERMATCH', index=112, number=10352,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TEAM_TEAMMATCH', index=113, number=10353,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_SCENE_MOVE', index=114, number=10400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_SCENE_SWITCH', index=115, number=10401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PALACE_ENTER', index=116, number=10402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PALACE_QUIT', index=117, number=10403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PALACE_FINISH', index=118, number=10404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TRAINROOM_FIGHT', index=119, number=10410,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TRAINROOM_ENTER', index=120, number=10411,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PET_UPGRADEQUA', index=121, number=10480,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PET_SETFIGHT', index=122, number=10481,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PET_EXCHANGE', index=123, number=10482,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_PET_UPGRADESTAR', index=124, number=10483,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_ARENA_ENTER', index=125, number=10500,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_ARENA_FIGHT', index=126, number=10501,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_ARENA_TOPLIST', index=127, number=10502,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_ARENA_RANKPRIZE', index=128, number=10503,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_HUASHAN_ENTER', index=129, number=10600,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_HUASHAN_QUIT', index=130, number=10601,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_HUASHAN_TOPLIST', index=131, number=10602,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_HUASHAN_MATCH', index=132, number=10603,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TOWER_FIGHT', index=133, number=10650,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_TOWER_RESET', index=134, number=10651,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_RANKLIST_INFO', index=135, number=10700,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MSG_GMCOMMOND', index=136, number=29999,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C2S_MSG_END', index=137, number=30000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=37,
  serialized_end=3208,
)
_sym_db.RegisterEnumDescriptor(_MSGDEFINE)

MsgDefine = enum_type_wrapper.EnumTypeWrapper(_MSGDEFINE)
S2C_MSG_BEGIN = 0
S2C_COMMON_ERROR = 50
S2C_PAY_REQ = 99
S2C_USER_LOGIN = 100
S2C_USER_LOGOUT = 101
S2C_USER_HEARTBEAT = 102
S2C_PLAYER_LOGIN = 103
S2C_PLAYER_INFO = 104
S2C_PLAYER_GETTHING = 105
S2C_PROP_LIST = 200
S2C_EQUIP_LIST = 201
S2C_UNEQUIP_LIST = 202
S2C_PROP_COMPOSE = 203
S2C_PROP_ENHANCE = 204
S2C_ENHANCE_INFO = 205
S2C_SHOPPING_INFO = 206
S2C_CHAT = 300
S2C_FRIEND_LIST = 301
S2C_TASK_LIST = 302
S2C_SUITFRIEND_LIST = 303
S2C_FRIENDAPPLY_LIST = 304
S2C_ADDFRIEND_SUC = 305
S2C_FRIEND_STATUS = 306
S2C_TASK_SYNCSTORY = 307
S2C_SKILL_LIST = 320
S2C_BASE_GONG = 321
S2C_HEART_GONG = 322
S2C_FIGHT_UNITLIST = 330
S2C_FIGHT_PROCESS = 331
S2C_FIGHT_RESULT = 332
S2C_FIGHT_AUTO = 333
S2C_TEAM_INFO = 350
S2C_TEAM_APPLY = 351
S2C_TEAM_INVITE = 352
S2C_TEAM_LEAVE = 353
S2C_TEAM_GIVE = 354
S2C_TEAM_MOVE = 355
S2C_TEAM_MEMBERSTATUS = 356
S2C_MAIL_LIST = 400
S2C_SCENE_MOVE = 500
S2C_SCENE_NPC = 501
S2C_SCENE_PLAYER = 502
S2C_SCENE_EVENT = 503
S2C_SCENE_ENTER = 504
S2C_PALACE_INFO = 600
S2C_PALACE_PLAYERINFO = 601
S2C_TRAINROOM_INFO = 610
S2C_PET_INFO = 701
S2C_PET_LIST = 702
S2C_ARENA_PLAYERINFO = 800
S2C_ARENA_TARGETLIST = 801
S2C_ARENA_TOPLIST = 802
S2C_ARENA_FIGHTRESULT = 803
S2C_HUASHAN_TEAMINFO = 900
S2C_HUASHAN_TOPLIST = 901
S2C_TOWER_INFO = 1000
S2C_RANKLIST_INFO = 1001
S2C_MSG_END = 9999
C2S_MSG_BEGIN = 10000
C2S_GUEST_LOGIN = 10001
C2S_USER_LOGIN = 10002
C2S_USER_LOGOUT = 10003
C2S_USER_HEARTBEAT = 10004
C2S_PLAYER_CREATE = 10005
C2S_PLAYER_LOGIN = 10006
C2S_PLAYER_LOGOUT = 10007
C2S_PLAYER_GUIDE = 10008
C2S_PROP_USE = 10100
C2S_PROP_BUY = 10101
C2S_PROP_SELL = 10102
C2S_PROP_COMPOSE = 10103
C2S_PROP_DECOMPOSE = 10104
C2S_PROP_EQUIP = 10105
C2S_PROP_UNEQUIP = 10106
C2S_PROP_SETGEM = 10107
C2S_PROP_UNSETGEM = 10108
C2S_PROP_COMPOSEGEM = 10109
C2S_PROP_COMPOSEEQUIPGEM = 10110
C2S_PROP_ENHANCE = 10111
C2S_MAIL_SEND = 10200
C2S_MAIL_READ = 10201
C2S_MAIL_DELETE = 10202
C2S_MAIL_EXTRACT = 10203
C2S_CHAT = 10300
C2S_FRIEND_ADD = 10301
C2S_FRIEND_DELETE = 10302
C2S_FRIEND_RESULT = 10303
C2S_TASK_ACCEPT = 10310
C2S_TASK_FINISH = 10311
C2S_TASK_CANCEL = 10312
C2S_TASK_FIGHT = 10313
C2S_TASK_SYNCSTORY = 10314
C2S_FIGHT_USESKILL = 10330
C2S_FIGHT_ROUNDREADY = 10331
C2S_SKILL_UPGRADE = 10332
C2S_BASEGONG_ADDPOINT = 10333
C2S_HEARTGONG_RESET = 10334
C2S_HEARTGONG_UPGRADE = 10335
C2S_FIGHT_AUTO = 10336
C2S_FIGHT_CALLPET = 10337
C2S_TEAM_CREATE = 10340
C2S_TEAM_APPLY = 10341
C2S_TEAM_APPLYRESULT = 10342
C2S_TEAM_INVITE = 10343
C2S_TEAM_INVITERESULT = 10344
C2S_TEAM_QUIT = 10345
C2S_TEAM_KICK = 10346
C2S_TEAM_DISSOLVE = 10347
C2S_TEAM_GIVE = 10348
C2S_TEAM_GIVERESULT = 10349
C2S_TEAM_REPLACE = 10350
C2S_TEAM_FORMATION = 10351
C2S_TEAM_PLAYERMATCH = 10352
C2S_TEAM_TEAMMATCH = 10353
C2S_SCENE_MOVE = 10400
C2S_SCENE_SWITCH = 10401
C2S_PALACE_ENTER = 10402
C2S_PALACE_QUIT = 10403
C2S_PALACE_FINISH = 10404
C2S_TRAINROOM_FIGHT = 10410
C2S_TRAINROOM_ENTER = 10411
C2S_PET_UPGRADEQUA = 10480
C2S_PET_SETFIGHT = 10481
C2S_PET_EXCHANGE = 10482
C2S_PET_UPGRADESTAR = 10483
C2S_ARENA_ENTER = 10500
C2S_ARENA_FIGHT = 10501
C2S_ARENA_TOPLIST = 10502
C2S_ARENA_RANKPRIZE = 10503
C2S_HUASHAN_ENTER = 10600
C2S_HUASHAN_QUIT = 10601
C2S_HUASHAN_TOPLIST = 10602
C2S_HUASHAN_MATCH = 10603
C2S_TOWER_FIGHT = 10650
C2S_TOWER_RESET = 10651
C2S_RANKLIST_INFO = 10700
C2S_MSG_GMCOMMOND = 29999
C2S_MSG_END = 30000


DESCRIPTOR.enum_types_by_name['MsgDefine'] = _MSGDEFINE


# @@protoc_insertion_point(module_scope)
