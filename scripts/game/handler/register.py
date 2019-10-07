# -*- coding: utf-8 -*-

import MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import MessageUser_pb2 as MessageUser_pb2

import userHandler as userHandler

protocols = {}
handlers = {}

def regist(type, proto, func):
	protocols[type] = proto
	handlers[type] = func

regist(MessageTypeDefine_pb2.C2S_USER_LOGIN, MessageUser_pb2.C2SUserLogin(), userHandler.handleC2SUserLogin)
