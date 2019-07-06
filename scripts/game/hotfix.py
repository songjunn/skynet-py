import importlib
import skynet
import hotfix
import command

import handler.register as register
import handler.userHandler as userHandler

import message.MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import message.MessageUser_pb2 as MessageUser_pb2

def reload():
	importlib.reload(skynet)
	importlib.reload(hotfix)
	importlib.reload(command)
	
	importlib.reload(register)
	importlib.reload(userHandler)

	importlib.reload(MessageTypeDefine_pb2)
	importlib.reload(MessageUser_pb2)

	skynet.logger_notice('reload ..')
