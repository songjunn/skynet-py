import skynet, time, json
import pbjson as pbjson
import GameServer as GameServer
import DBObject_pb2 as DBObject
import MessageTypeDefine_pb2 as MessageTypeDefine
import MessageUser_pb2 as MessageUser

def createUser(uid):
	p = DBObject.DBPlayer()
	p.userid = uid
	p.base.createtime = int(time.time())
	user = pbjson.pb2dict(p)

	skynet.logger_notice('[Game]User create, userId=' + str(user['userid']))

	return user

def loginUser(user, fd):
	user['fd'] = fd
	user['base']['logintime'] = int(time.time())

	skynet.logger_notice('[Game]User login, userId=' + str(user['userid']))

def logoutUser(user):
	user['base']['logouttime'] = int(time.time())

	skynet.logger_notice('[Game]User logout, userId=' + str(user['userid']))

def loadUser(session, userId):
	q = {'userid': userId}
	query = json.dumps(q)
	skynet.mongo_findone(session, 'honorwar', 'user', query)

def saveUser(user):
	query = {'userid': user['userid']}
	query = json.dumps(query)
	value = pbjson.dict2pb(user, DBObject.DBPlayer)
	value = pbjson.pb2json(value)
	skynet.mongo_upsert('honorwar', 'user', query, value)

def sendMessage(user, type, message):
	fd = user['fd']
	GameServer.GameServer().sendClientMsg(fd, type, message)

def sendUserInfo(user):
	message = MessageUser.S2CUserInfo()
	message.userid = user['userid']
	message.ranks = user['base']['ranks']
	message.level = user['base']['level']
	message.honor = user['base']['honor']
	message.action = user['base']['action']
	message.golden = user['base']['golden']
	
	sendMessage(user, MessageTypeDefine.S2C_USER_LOGIN, message)
