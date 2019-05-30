# -*- coding: utf-8 -*-

import json
import skynet
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
	#print("handleC2SUserLogin: " + j)
	#skynet.mongo_insert('tyjh_game_1', 'global', json.dumps(j))
