# -*- coding: utf-8 -*-
import struct
import skynet
import utils.MongoDB as MongoDB
from utils.Singleton import Singleton
from google.protobuf import text_format
from handler import register

class GameServerHandler(Singleton):
	mongoDb = None

	def __init__(self):
		super(GameServerHandler, self).__init__()
		self.nid_ = 0

	def start(self, id):
		self.nid_ = id

		self.mongoDb = MongoDB.MongoDB()
		self.mongoDb.connect('mongodb://127.0.0.1:27017')
		self.mongoDb.setDatabase('tyjh2-game3')

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
		
		register.handlers.get(type)(guest)

	def insertDb(self, collection, value):
		self.mongoDb.insert(collection, value)

	def updateDb(self, collection, query, value):
		self.mongoDb.update(collection, query, value)

	def upsertDb(self, collection, query, value):
		self.mongoDb.upsert(collection, query, value)

	def removeDb(self, collection, query):
		self.mongoDb.remove(collection, query)

	def findOne(self, collection, query):
		self.mongoDb.findOne(collection, query)

	def findAll(self, collection, query):
		self.mongoDb.findAll(collection, query)
