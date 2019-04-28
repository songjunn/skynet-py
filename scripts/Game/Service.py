import os, sys 
sys.path.append("../lib")
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from gamed.GameServerHandler import GameServerHandler

def create(nid, handle):
	GameServerHandler().start(nid)

def release():
	pass

def handle(handle, source, session, type, msg):
	#print(type, source, msg, len(msg))
	GameServerHandler().handleClientEvent(msg)
