import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import skynet
import command
import utils.Coroutine as Coroutine
import gamed.GameServerHandler as GameServerHandler

def create(nid, handle):
	skynet.set_source(handle)
	GameServerHandler.GameServerHandler().start(nid)

def release():
	pass

def handle(handle, source, session, type, msg):
	print(type, source, msg, len(msg))
	if type == skynet.SERVICE_TEXT: 
		handleTextMsg(handle, source, session, msg)
	elif type == skynet.SERVICE_TIMER:
		handleTimerMsg(handle, source, session, msg)
	elif type == skynet.SERVICE_RESPONSE:
		handleResponseMsg(handle, source, session, msg)
	else:
		skynet.logger_error('error handle message')

def handleTextMsg(handle, source, session, msg):
	args = msg.split('|')
	cmd = args[0]
	size = int(args[1])
	data = args[2]

	if cmd == 'forward':
		GameServerHandler.GameServerHandler().handleClientEvent(session, data, size)
	elif cmd == 'connect':
		print('py accept fd=%d addr=%s' % (session, msg))
	elif cmd == 'disconnect':
		print('py disconnect fd=%d' % (session))
	elif cmd == 'http':
		command.handleRequest(source, session, data)
	else:
		pass

def handleTimerMsg(handle, source, session, msg):
	pass

def handleResponseMsg(handle, source, session, msg):
	Coroutine.send(session, msg)
