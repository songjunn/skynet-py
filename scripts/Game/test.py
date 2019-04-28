import sys 
sys.path.append("../lib") 
import json
#import pySkynet
import pyMongodb

class Game:

	def __init__(self):
		print "python service construct..."
		#init_logging()

	def create(self, harbor, handle):
		#fpa=open("pylog.txt","w")
		#testStr="Hello World!"
		#print >> fpa, testStr
		#fpa.close()
		#logging.info("python service start...")
		data = { 'name' : 'test1', 'age' : 20}
		pyMongodb.insertDb(0, 'testpy', 'pycollection', json.dumps(data))
		print "python service start..."
		#pySkynet.skynet_send('game', 0, 101, 'testtest', 8)

		pyMongodb.selectOne()

	def release(self):
		pass

	def handle(self):
		print(self.name)
