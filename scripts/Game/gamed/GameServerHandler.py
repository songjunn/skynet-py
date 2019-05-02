# -*- coding: utf-8 -*-
import struct
from utils.Singleton import Singleton
from google.protobuf import text_format
from handler import register

class GameServerHandler(Singleton):

	def __init__(self):
		super(GameServerHandler, self).__init__()
		self.nid_ = 0

	def start(self, id):
		self.nid_ = id

	def quit(self):
		pass

	def tick(self):
		pass

	def handleClientEvent(self, fd, message, sz):
		print("fd=%d sz=%d message={%s}" % (fd, sz, message))
		type, req = struct.unpack_from('i'+str(sz)+'s', message, 0)

		guest = register.protocols.get(type)
		guest.ParseFromString(req)
		print("Recv message %d size %d: {%s}" % (type, data_size, text_format.MessageToString(guest, True, True)))
		
		register.handlers.get(type)(guest)

