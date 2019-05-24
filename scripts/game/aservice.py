import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import skynet
from gamed.GameServerHandler import GameServerHandler

def create(nid, handle):
	skynet.set_source(handle)
	GameServerHandler().start(nid)
	skynet.logger_notice(b"Game service start")

def release():
	pass

def handle(handle, source, session, type, msg):
	print(type, source, msg, len(msg))
	skynet.logger_notice(b"test skynet logger...")
	if type == skynet.SERVICE_TEXT: 
		handleTextMsg(handle, source, session, msg)
	elif type == skynet.SERVICE_TIMER:
		handleTimerMsg(handle, source, session, msg)
	else:
		print('error handle message')


def handleTextMsg(handle, source, session, msg):
	cmd = msg.split('|')
	if cmd[0] == 'forward':
		GameServerHandler().handleClientEvent(session, cmd[2], int(cmd[1]))
	elif cmd[0] == 'connect':
		print('py accept fd=%d addr=%s' % (session, msg))
	elif cmd[0] == 'disconnect':
		print('py disconnect fd=%d' % (session))
	else:
		pass

def handleTimerMsg(handle, source, session, msg):
	pass
