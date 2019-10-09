# -*- coding: utf-8 -*-
import struct, socket
import skynet
import Coroutine as Coroutine
import Singleton as Singleton
import google.protobuf.text_format as text_format
import register as register

class GameServer(Singleton.Singleton):
	def __init__(self):
		super(GameServer, self).__init__()
		self.nid_ = 0

	def start(self, id):
		self.nid_ = id
		skynet.logger_debug('[Game]service start, id={}'.format(self.nid_))

	def quit(self):
		skynet.logger_debug('[Game]service quit, id={}'.format(self.nid_))

	def tick(self):
		pass
		#skynet.logger_debug('[Game]server handler tick...')

	def sendClientMsg(self, fd, type, proto):
		message = proto.SerializeToString()
		size = 4 + len(message)
		s = struct.Struct('ii' + str(size-4) + 's')
		v = (size, type, message)
		data = s.pack(*v)
		skynet.gate_forward_send(fd, data) 
		skynet.logger_debug('[Game]Send message {} to {} size {}: {{{}}}'.format(type, fd, size, text_format.MessageToString(proto, True, True)))

	def recvClientMsg(self, fd, message, sz):
		type, req = struct.unpack('i'+str(sz-4)+'s', message)
		type = socket.ntohl(type)

		proto = register.protocols.get(type)
		proto.ParseFromString(req)
		skynet.logger_debug("[Game]Recv message {} from {} size {}: {{{}}}".format(type, fd, sz, text_format.MessageToString(proto, True, True)))
		
		handler = register.handlers.get(type)
		try:
			Coroutine.create(handler, fd=fd, data=proto)
		except StopIteration as e:
			pass
