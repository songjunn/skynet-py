import os, sys, json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/../common'))
import skynet as skynet
import MongoDB as MongoDB

global mongo

def create(nid, handle, args):
	skynet.set_source(handle)

	global mongo
	mongo = MongoDB.MongoDB()
	mongo.connect('mongodb://127.0.0.1:27000')

def release():
	global mongo
	del mongo

def handle(handle, source, session, type, msg):
	message = msg.decode()
	if type == skynet.SERVICE_TEXT: 
		handleTextMsg(handle, source, session, message)
	else:
		skynet.logger_error('error handle message')

def handleTextMsg(handle, source, session, msg):
	args = msg.split('|')
	cmd = args[0]
	#print(args)

	if cmd == 'update':
		mongo.setDatabase(args[1])
		mongo.update(args[2], json.loads(args[3]), json.loads(args[4]))
	elif cmd == 'upsert':
		mongo.setDatabase(args[1])
		mongo.upsert(args[2], json.loads(args[3]), json.loads(args[4]))
	elif cmd == 'insert':
		mongo.setDatabase(args[1])
		mongo.insert(args[2], json.loads(args[3]))
	elif cmd == 'remove':
		mongo.setDatabase(args[1])
		mongo.remove(args[2], json.loads(args[3]))
	elif cmd == 'findone':
		mongo.setDatabase(args[1])
		value = mongo.findOne(args[2], json.loads(args[3]))
		skynet.service_send(source, session, skynet.SERVICE_RESPONSE, json.dumps(value))
	elif cmd == 'findall':
		mongo.setDatabase(args[1])
		value = mongo.findAll(args[2], json.loads(args[3]))
		skynet.service_send(source, session, skynet.SERVICE_RESPONSE, json.dumps(value))
	else:
		pass
