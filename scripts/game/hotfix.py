import importlib
import skynet
import hotfix
import command

import handler.register as register
import handler.userHandler as userHandler

import message.MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import message.MessageUser_pb2 as MessageUser_pb2

def reload(name):
	skynet.logger_notice('reload {}'.format(name))

	if name == 'skynet':
		importlib.reload(skynet)
	elif name == 'hotfix':
		importlib.reload(hotfix)
	elif name == 'command':
		importlib.reload(command)

	elif name == 'register':
		importlib.reload(register)
	elif name == 'userHandler':
		importlib.reload(userHandler)

	elif name == 'MessageTypeDefine':
		importlib.reload(MessageTypeDefine_pb2)
	elif name == 'MessageUser':
		importlib.reload(MessageUser_pb2)
