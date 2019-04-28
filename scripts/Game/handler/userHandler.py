# -*- coding: utf-8 -*-

from message import MessageTypeDefine_pb2
from message import MessageUser_pb2

def handleC2SGuestLogin(data):
	print("handleC2SGuestLogin:" + data.name)
	pass
	
def handleC2SUserLogin(data):
	print("handleC2SUserLogin")
	pass
