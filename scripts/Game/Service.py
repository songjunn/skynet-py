import os, sys
import ctypes
import platform
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from gamed.GameServerHandler import GameServerHandler

if platform.system() == 'Windows':
    lib = ctypes.cdll.LoadLibrary(os.path.abspath(os.path.dirname(__file__))+'/../../skynet.dll')
elif platform.system() =='Linux':
    lib = ctypes.cdll.LoadLibrary(os.path.abspath(os.path.dirname(__file__))+'/../../libskynet.so')

SERVICE_TEXT = 0
SERVICE_SOCKET = 1
SERVICE_TIMER = 2
SERVICE_REMOTE = 3


def create(nid, handle):
	GameServerHandler().start(nid)
	lib.skynet_logger_print(0, 0, b"Game service start...")

def release():
	pass

def handle(handle, source, session, type, msg):
	print(type, source, msg, len(msg))
	lib.skynet_logger_print(0, 0, b"test skynet logger...")
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
	elif cmd[0] == 'connect':
		print('py accept fd=%d addr=%s' % (session, msg))
	elif cmd[0] == 'disconnect':
		print('py disconnect fd=%d' % (session))
	else:
		pass

def handleTimerMsg(handle, source, session, msg):
	pass