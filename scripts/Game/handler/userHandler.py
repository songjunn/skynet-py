# -*- coding: utf-8 -*-

import json
import skynet
import gamed.GameServerHandler as GameServerHandler
from google.protobuf import text_format

import message.MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import message.MessageUser_pb2 as MessageUser_pb2

def handleC2SGuestLogin(data):
	print("handleC2SGuestLogin:" + data.name)
	pass

def handleC2SUserLogin(data):
	#j = text_format.MessageToString(data, True, True)
	j = {}
	j['appid'] = data.appid
	j['userid'] = data.userid
	j['ticket'] = data.ticket
	
	res = GameServerHandler.GameServerHandler().findOne('user', {'userid': j['userid']})
	if res == None:
		GameServerHandler.GameServerHandler().insertDb('user', j)
	else:
		GameServerHandler.GameServerHandler().updateDb('user', {'userid': j['userid']}, j)
