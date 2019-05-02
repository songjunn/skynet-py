import os, sys 
sys.path.append("../lib")
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from gamed.GameServerHandler import GameServerHandler

SERVICE_TEXT = 0
SERVICE_SOCKET = 1
SERVICE_TIMER = 2
SERVICE_REMOTE = 3


def create(nid, handle):
	GameServerHandler().start(nid)

def release():
	pass

def handle(handle, source, session, type, msg):
	print(type, source, msg, len(msg))
	if type == SERVICE_TEXT: 
		handleTextMsg(handle, source, session, msg)
	elif type == SERVICE_TIMER:
		handleTimerMsg(handle, source, session, msg)
	else:
		print('error handle message')


def handleTextMsg(handle, source, session, msg):
	cmd = msg.split('|')
	if cmd[0] == 'forward':
		GameServerHandler().handleClientEvent(session, cmd[2], int(cmd[1]))
	elif cmd[0] == 'accept':
		pass
	elif cmd[0] == 'disconnect':
		pass
	else:
		pass

def handleTimerMsg(handle, source, session, msg):
	pass