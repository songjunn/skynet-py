# -*- coding: utf-8 -*-
import Singleton as Singleton

class UserMgr(Singleton.Singleton):
	def __init__(self):
		super(UserMgr, self).__init__()
		self.userlist_ = {}

	def addUser(self, key, user):
		self.userlist_[key] = user

	def removeUser(self, userId):
		self.userlist_.pop(userId)

	def getUser(self, userId):
		return self.userlist_.get(userId)
