import importlib
import handler.userHandler as userHandler

def reload(name):
	if name == 'userHandler':
		importlib.reload(userHandler)
