# -*- coding: utf-8 -*-

import message.MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import message.MessageUser_pb2 as MessageUser_pb2

import handler.userHandler as userHandler

protocols = {
    MessageTypeDefine_pb2.C2S_USER_LOGIN: MessageUser_pb2.C2SUserLogin(),
}

handlers = {
	MessageTypeDefine_pb2.C2S_USER_LOGIN: userHandler.handleC2SUserLogin,
}