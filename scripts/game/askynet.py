import os, ctypes, platform

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

def set_source(value):
	global source
	source = value

def logger_debug(text):
	skynet.skynet_logger_print(source, LOGGER_DEBUG, text)

def logger_warn(text):
	skynet.skynet_logger_print(source, LOGGER_WARN, text)

def logger_notice(text):
	skynet.skynet_logger_print(source, LOGGER_NOTICE, text)

def logger_error(text):
	skynet.skynet_logger_print(source, LOGGER_ERROR, text)

def service_send(target, session, type, msg):
	skynet.skynet_sendhandle(target, source, session, type, msg, len(msg))

def service_return(target, session, type, msg):
	pass
