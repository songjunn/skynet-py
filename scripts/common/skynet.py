import os, ctypes, platform, struct, json

if platform.system() == 'Windows':
    skynet = ctypes.cdll.LoadLibrary(os.path.abspath(os.path.dirname(__file__))+'/../../skynet.dll')
elif platform.system() =='Linux':
    skynet = ctypes.cdll.LoadLibrary(os.path.abspath(os.path.dirname(__file__))+'/../../libskynet.so')

#logger type
LOGGER_DEBUG = 0
LOGGER_WARN = 1
LOGGER_NOTICE = 2
LOGGER_ERROR = 3

#service message type
SERVICE_TEXT = 0
SERVICE_SOCKET = 1
SERVICE_TIMER = 2
SERVICE_REMOTE = 3
SERVICE_RESPONSE = 4

def set_source(value):
	global source
	source = value

def logger_debug(text):
	#print(text.encode('utf-8'))
	skynet.skynet_logger_print(source, LOGGER_DEBUG, ctypes.c_char_p(text.encode('utf-8')))

def logger_warn(text):
	skynet.skynet_logger_print(source, LOGGER_WARN, ctypes.c_char_p(text.encode('utf-8')))

def logger_notice(text):
	skynet.skynet_logger_print(source, LOGGER_NOTICE, ctypes.c_char_p(text.encode('utf-8')))

def logger_error(text):
	skynet.skynet_logger_print(source, LOGGER_ERROR, ctypes.c_char_p(text.encode('utf-8')))

def service_send(target, session, type, msg):
	#print('target=%d session=%d type=%d msg=%s len=%d' % (target, session, type, msg, len(msg)))
	skynet.skynet_sendhandle(target, source, session, type, ctypes.c_char_p(msg.encode('utf-8')), len(msg))

def set_timer(time):
	skynet.skynet_timer_register(source, 0, 0, time)

def http_response_send(target, fd, msg):
	data = 'response|' + str(fd) + '|' + msg
	service_send(target, fd, SERVICE_TEXT, data)

def gate_forward_send(fd, msg):
	data = b'forward|' + msg
	skynet.skynet_sendname(b'gatews', source, fd, SERVICE_TEXT, ctypes.c_char_p(data), len(data))

def gate_kick_send(target, fd):
	data = 'kick'
	service_send(target, fd, SERVICE_TEXT, data)

def mongo_findone(sid, dbname, collec, query):
	s = 'findone|{}|{}|{}'.format(dbname, collec, query)
	skynet.skynet_sendname(b'mongo', source, sid, SERVICE_TEXT, ctypes.c_char_p(s.encode('utf-8')), len(s))

def mongo_upsert(dbname, dbcollec, query, value):
	s = 'upsert|{}|{}|{}|{}'.format(dbname, dbcollec, query, value)
	skynet.skynet_sendname(b'mongo', source, 0, SERVICE_TEXT, ctypes.c_char_p(s.encode('utf-8')), len(s))
