# -*- coding: utf-8 -*-

from message import MessageTypeDefine_pb2
from message import MessageUser_pb2

#from handler import userHandler
import handler.userHandler as userHandler

protocols = {
    MessageTypeDefine_pb2.C2S_USER_LOGIN: MessageUser_pb2.C2SUserLogin(),
}

handlers = {
	MessageTypeDefine_pb2.C2S_USER_LOGIN: userHandler.handleC2SUserLogin,
}