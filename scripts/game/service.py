import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import include
import skynet
import Coroutine as Coroutine
import GameServer as GameServer
import AdminServer as AdminServer

def create(nid, handle, args):
	skynet.set_source(handle)
	GameServer.GameServer().start(nid)
	skynet.set_timer(1000)

def release():
	pass

def handle(handle, source, session, type, msg):
	if type == skynet.SERVICE_TEXT:
		handleTextMsg(handle, source, session, msg)
	elif type == skynet.SERVICE_TIMER:
		handleTimerMsg(handle, source, session, msg)
	elif type == skynet.SERVICE_RESPONSE:
		handleResponseMsg(handle, source, session, msg)
	else:
		skynet.logger_error('[Game]error handle message')

def handleTextMsg(handle, source, fd, msg):
	args = msg.split(b'|')
	cmd = args[0].decode()
	size = int(args[1].decode())
	data = args[2]

	skynet.logger_debug('[Game]handle text msg: handle=%d source=%d fd=%d msg=%s' % (handle, source, fd, msg))

	if cmd == 'forward':
		GameServer.GameServer().recvClientMsg(fd, data, size)
	elif cmd == 'connect':
		skynet.logger_debug('[Game]game accept fd=%d addr=%s' % (fd, msg))
	elif cmd == 'disconnect':
		skynet.logger_debug('[Game]game disconnect fd=%d' % (fd))
	elif cmd == 'http':
		AdminServer.handleRequest(source, fd, data)
	else:
		pass

def handleTimerMsg(handle, source, session, msg):
	GameServer.GameServer().tick()
	skynet.set_timer(1000)

def handleResponseMsg(handle, source, session, msg):
	message = msg.decode()
	if (message == '""'): message = ''
	skynet.logger_debug('[Game]handle response msg: handle=%d source=%d session=%d msg=%s' % (handle, source, session, message))
	Coroutine.send(session, message)
