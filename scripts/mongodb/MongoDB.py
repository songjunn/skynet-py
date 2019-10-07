import json
import pymongo
import skynet
from collections import Iterator

class MongoDB(object):
	conn = None
	database = None

	def __init__(self):
		pass

	def connect(self, uri):
		self.conn = pymongo.MongoClient(uri);
		if self.conn != None:
			skynet.logger_notice('[MongoDB]connect mongodb success, ' + uri)
		else:
			skynet.logger_error('[MongoDB]connect mongodb failed, ' + uri)

	def setDatabase(self, dbname):
		self.database = self.conn[dbname]

	def insert(self, collection, value):
		skynet.logger_debug('[MongoDB]insert '+collection+':'+json.dumps(value))
		self.database[collection].insert(value)

	def update(self, collection, query, value):
		skynet.logger_debug('[MongoDB]update '+collection+', query:'+json.dumps(query)+', value:'+json.dumps(value))
		self.database[collection].update(query, value)

	def upsert(self, collection, query, value):
		skynet.logger_debug('[MongoDB]upsert '+collection+', query:'+json.dumps(query)+', value:'+json.dumps(value))
		self.database[collection].update(query, value, upsert=True)

	def remove(self, collection, query):
		skynet.logger_debug('[MongoDB]remove '+collection+':'+json.dumps(query))
		self.database[collection].remove(query)

	def findAll(self, collection, query):
		value = self.database[collection].find(query, {'_id': 0})
		if value is None: return ''
		return value

	def findOne(self, collection, query):
		value = self.database[collection].find_one(query, {'_id': 0})
		if value is None: return ''
		return value

	def findBySort(self, collection, query, sort):
		value = self.database[collection].find(query, {'_id': 0}).sort(sort)
		if value is None: return ''
		return value

	def findBySkip(self, collection, query, skip):
		value = self.database[collection].find(query, {'_id': 0}).skip(skip)
		if value is None: return ''
		return value

	def findByLimit(self, collection, query, limit):
		value = self.database[collection].find(query, {'_id': 0}).limit(limit)
		if value is None: return ''
		return value

	def find(self, collection, query, sort=None, limit=0, skip=0):
		if sort != None and limit > 0 and skip > 0:
			value = self.database[collection].find(query, {'_id': 0}).sort(sort).skip(skip).limit(limit)
		elif sort != None and limit > 0:
			value = self.database[collection].find(query, {'_id': 0}).sort(sort).limit(limit)
		elif sort != None and skip > 0:
			value = self.database[collection].find(query, {'_id': 0}).sort(sort).skip(skip)
		elif skip > 0 and limit > 0:
			value = self.database[collection].find(query, {'_id': 0}).skip(skip).limit(limit)
		if value is None: return ''
		return value
