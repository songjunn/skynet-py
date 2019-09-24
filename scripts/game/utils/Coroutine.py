# -*- coding: utf-8 -*-
from collections import Iterator

global sessions
global session_generate_id

sessions = {}
session_generate_id = 0

def create(generator, **kwargs):
	global sessions
	global session_generate_id
	session_generate_id += 1
	sid = session_generate_id
	co = generator(sid, **kwargs)
	if isinstance(co, Iterator):
		sessions[sid] = co
		next(co)

def resume(sid):
	global sessions
	co = sessions[sid]
	try:
		next(co)
	except StopIteration:
		pass

def send(sid, msg):
	global sessions
	co = sessions[sid]
	try:
		co.send(msg)
	except StopIteration:
		pass
