# -*- coding: utf-8 -*-

import json
import User as User
import UserMgr as UserMgr

def handleC2SUserLogin(sid, **kwargs):
	fd = kwargs['fd']
	data = kwargs['data']
	userId = data.userid
	
	user = UserMgr.UserMgr().getUser(userId)
	if (user == None):
		User.loadUser(sid, userId)
		user = yield
		
		if (len(user) == 0):
			user = User.createUser(userId)
		else:
			user = json.loads(user)

	User.loginUser(user, fd)
	User.sendUserInfo(user)
	User.saveUser(user)
	UserMgr.UserMgr().addUser(user['userid'], user)
