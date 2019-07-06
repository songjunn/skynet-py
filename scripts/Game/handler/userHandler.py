# -*- coding: utf-8 -*-

import json
import skynet
import utils.Coroutine as Coroutine
import gamed.GameServerHandler as GameServerHandler
import google.protobuf.text_format as text_format

import message.MessageTypeDefine_pb2 as MessageTypeDefine_pb2
import message.MessageUser_pb2 as MessageUser_pb2

def handleC2SGuestLogin(data):
	print("handleC2SGuestLogin:" + data.name)
	pass

def handleC2SUserLogin(sid, **kwargs):
	data = kwargs['data']
	j = {}
	j['appid'] = data.appid
	j['userid'] = data.userid
	j['ticket'] = data.ticket

	q = {}
	q['userid'] = data.userid

	skynet.mongo_findone(sid, 'user', 'user', json.dumps(q))
	userData = yield
	print('userData: %s' % (userData))

	if userData == '':
		skynet.mongo_insert('user', 'user', json.dumps(j))
