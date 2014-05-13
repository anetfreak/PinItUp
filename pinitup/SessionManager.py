import sys
import os
import socket
import StringIO
import json
import time

from session_dao import DBConn
class SessionManager():
    def __init__(self):
        self.dbconn = DBConn("127.0.0.1",5984)
        self.sessionCache = []
        self.max_size = 100
        self.curr_size = 0
        
    def addSession(self, userId):
        if userId != None:
            self.addSessionCache(userId)
            return True
            #return self.dbconn.addSession(userId)
        return False
    
    def deleteSession(self, userId):
        if userId != None:
            self.removeSessionCache(userId)
            return True
            #return self.dbconn.deleteSession(userId)
        return False
    
    def isSessionExists(self, userId):
        if userId != None:
            return self.isSessionExistsInCache(userId)
            #return self.dbconn.isSessionExists(userId)
        return False
    
    def isSessionExistsInCache(self, userId):
        if userId in self.sessionCache:
            self.removeSessionCache(userId)
            self.addSessionCache(userId)
            return True
        return False
               
    def removeSessionCache(self, userId):
        if self.curr_size > 0:
            if self.isSessionExists(userId):
                self.sessionCache.remove(userId)
                self.curr_size = self.curr_size - 1
            
    def addSessionCache(self, userId):
        if self.curr_size < self.max_size:
            self.sessionCache.append(userId)
            self.curr_size = self.curr_size + 1
        else:
            self.sessionCache.remove()
            self.curr_size = self.curr_size - 1
            