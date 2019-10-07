import importlib
import skynet
import hotfix

import AdminServer as AdminServer

import register as register
import userHandler as userHandler

import MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import MessageUser_pb2 as MessageUser_pb2

def reload():
	importlib.reload(skynet)
	importlib.reload(hotfix)

	importlib.reload(AdminServer)
	
	importlib.reload(register)
	importlib.reload(userHandler)

	importlib.reload(MessageTypeDefine_pb2)
	importlib.reload(MessageUser_pb2)

	skynet.logger_notice('[Game]reload ..')
