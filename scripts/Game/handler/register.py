# -*- coding: utf-8 -*-

from message import MessageTypeDefine_pb2
from message import MessageUser_pb2
from message import MessagePlayer_pb2
from message import MessageProp_pb2
from message import MessageMail_pb2
from message import MessageFriend_pb2

from handler import userHandler
from handler import propHandler
from handler import mailHandler
from handler import friendHandler

protocols = {
    MessageTypeDefine_pb2.C2S_GUEST_LOGIN: MessageUser_pb2.C2SGuestLogin(),
    MessageTypeDefine_pb2.C2S_USER_LOGIN: MessageUser_pb2.C2SUserLogin(),
}

handlers = {
	MessageTypeDefine_pb2.C2S_GUEST_LOGIN: userHandler.handleC2SGuestLogin,
	MessageTypeDefine_pb2.C2S_USER_LOGIN: userHandler.handleC2SUserLogin,
}