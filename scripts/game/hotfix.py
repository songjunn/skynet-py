import importlib
import skynet
import gamed.GameServerHandler as GameServerHandler

import handler.register as register
import handler.userHandler as userHandler

import message.MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import message.MessageUser_pb2 as MessageUser_pb2

def reload(name):
	skynet.logger_notice('reload {}'.format(name))

	if name == 'skynet':
		importlib.reload(skynet)
	elif name == 'GameServerHandler':
		importlib.reload(GameServerHandler)

	elif name == 'register':
		importlib.reload(register)
	elif name == 'userHandler':
		importlib.reload(userHandler)

	elif name == 'MessageTypeDefine':
		importlib.reload(MessageTypeDefine_pb2)
	elif name == 'MessageUser':
		importlib.reload(MessageUser_pb2)
