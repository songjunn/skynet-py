import os, sys, importlib
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import skynet
import hotfix
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
	elif cmd[0] == 'http':
		handleHttpMsg(cmd[2])
	else:
		pass

def handleHttpMsg(msg):
	print('http msg:'+msg)
	args = {}
	p = msg.split('?', 1)
	route = p[0]
	t = p[1].split('&')
	for item in t:
		pos = item.index('=')
		k = item[0:pos]
		v = item[pos+1:]
		args[k] = v
	print('route='+route)
	print(args)

	if route == '/gm/reload':
		hotfix.reload(args['module'])

def handleTimerMsg(handle, source, session, msg):
	pass
