import sys 
sys.path.append("../lib")
import pySkynet
import Coroutine

sessions = {}
session_generate_id = 0;

def send(service, type, msg):
	pySkynet.skynet_send(service, 0, 0, type, msg, len(msg))

def ret(service, type, msg):
	def generator(sid, **kwargs):
        pySkynet.skynet_send(kwargs['service'], 0, sid, kwargs['type'], kwargs['msg'], kwargs['len'])
        return yield
    Coroutine.create(generator, service=service, type=type, msg=msg, len=len(msg))
