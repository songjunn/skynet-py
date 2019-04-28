# -*- coding: utf-8 -*-

sessions = {}
session_generate_id = 0;

def create(generator, **kwargs):
    sid = session_generate_id++
    co = generator(sid, kwargs)
    sessions[sid] = co
    next(co)

def resume():
    pass

def delete():
    pass
