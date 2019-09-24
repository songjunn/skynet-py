# -*- coding: utf-8 -*-
import struct
import skynet
import utils.Coroutine as Coroutine
import utils.Singleton as Singleton
import google.protobuf.text_format as text_format
import handler.register as register

class GameServerHandler(Singleton.Singleton):
	def __init__(self):
		super(GameServerHandler, self).__init__()
		self.nid_ = 0

	def start(self, id):
		self.nid_ = id
		skynet.logger_debug('Game service start, id={}'.format(self.nid_))

	def quit(self):
		skynet.logger_debug('Game service quit, id={}'.format(self.nid_))

	def tick(self):
		pass

	def handleClientEvent(self, fd, message, sz):
		print("fd=%d sz=%d message={%s}" % (fd, sz, message))
		message = message.encode()
		type, req = struct.unpack('i'+str(sz-4)+'s', message)

		guest = register.protocols.get(type)
		guest.ParseFromString(req)
		skynet.logger_debug("Recv message {} size {}: {}".format(type, sz, text_format.MessageToString(guest, True, True)))
		
		handler = register.handlers.get(type)
		Coroutine.create(handler, data=guest)
