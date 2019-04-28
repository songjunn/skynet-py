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

	def handleClientEvent(self, message):
		fd, addr_size = struct.unpack_from('=ih', message, 0)
		data_size = len(message) - addr_size- 8
		addr, type, req = struct.unpack_from('='+str(addr_size)+'sH'+str(data_size)+'s', message, 6)

		guest = register.protocols.get(type)
		guest.ParseFromString(req)
		print("Recv message %d size %d: {%s}" % (type, data_size, text_format.MessageToString(guest, True, True)))
		
		register.handlers.get(type)(guest)

