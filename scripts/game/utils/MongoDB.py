import json
import pymongo
import skynet

class MongoDB(object):
	conn = None
	database = None

	def __init__(self):
		pass

	def connect(self, uri):
		self.conn = pymongo.MongoClient(uri);
		if self.conn != None:
			skynet.logger_notice('connect mongodb success, ' + uri)
		else:
			skynet.logger_error('connect mongodb failed, ' + uri)

	def setDatabase(self, dbname):
		self.database = self.conn[dbname]

	def insert(self, collection, value):
		skynet.logger_debug('[MongoDB] insert '+collection+':'+json.dumps(value))
		self.database[collection].insert(value)

	def update(self, collection, query, value):
		skynet.logger_debug('[MongoDB] update '+collection+', query:'+json.dumps(query)+', value:'+json.dumps(value))
		self.database[collection].update(query, value, {upsert:False, multi:True})

	def upsert(self, collection, query, value):
		skynet.logger_debug('[MongoDB] upsert '+collection+', query:'+json.dumps(query)+', value:'+json.dumps(value))
		self.database[collection].upsert(query, value, {upsert:True, multi:True})

	def remove(self, collection, query):
		skynet.logger_debug('[MongoDB] remove '+collection+':'+json.dumps(query))
		self.database[collection].remove(query)

	def findAll(self, collection, query):
		return self.database[collection].find(query)

	def findOne(self, collection, query):
		return self.database[collection].find_one(query)

	def findBySort(self, collection, query, sort):
		return self.database[collection].find(query).sort(sort)

	def findBySkip(self, collection, query, skip):
		return self.database[collection].find(query).skip(skip)

	def findByLimit(self, collection, query, limit):
		return self.database[collection].find(query).limit(limit)

	def find(self, collection, query, sort=None, limit=0, skip=0):
		if sort != None and limit > 0 and skip > 0:
			return self.database[collection].find(query).sort(sort).skip(skip).limit(limit)
		elif sort != None and limit > 0:
			return self.database[collection].find(query).sort(sort).limit(limit)
		elif sort != None and skip > 0:
			return self.database[collection].find(query).sort(sort).skip(skip)
		elif skip > 0 and limit > 0:
			return self.database[collection].find(query).skip(skip).limit(limit)
