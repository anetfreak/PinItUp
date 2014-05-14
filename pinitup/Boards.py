import sys
import os
import socket
import StringIO
import json

from board_dao import DBConn
from SessionManager import SessionManager
class Board(object):
   json, xml, html, text = range(1, 5)

   # setup the configuration for our service
   def __init__(self, base, conf_fn, session):
      self.host = socket.gethostname()
      self.base = base
      self.conf = {}
      
      # should emit a failure (file not found) message
      if os.path.exists(conf_fn):
         with open(conf_fn) as cf:
            for line in cf:
               name, var = line.partition("=")[::2]
               self.conf[name.strip()] = var.strip()
      else:
         raise Exception("configuration file not found.")

      self.dbconn = DBConn("127.0.0.1",5984)
      self.session = session


   def createBoard(self, userId, boardName, boardDesc, category, isPrivate):
      if not self.session.isSessionExists(userId):
           return "Login First!!"  
      print '---> board.add: boardName:', boardName, ' boardDesc:', boardDesc, ' category:', category, ' isPrivate:', isPrivate
      try:
         # Insert userId and Board mapping in DB (key = User Id)
           result = self.dbconn.createBoard(userId, boardName, boardDesc, category, isPrivate)
#          bin_name = ["userId", "boardName"]
#          values = [userId, boardName]
#          types = ["string", "string"]
#          keyObj = self.dbconn.createKey_Obj(userId)
#          bins = self.dbconn.createBins_general(bin_name, values, types, 2)
#          self.dbconn.writeToDB("UserBoards", keyObj, bins, 2)
# 
#          # Insert Board Details in DB (Key = Board Name)
#          bin_name = ["userId", "boardName", "boardDesc", "category", "isPrivate"]
#          values = [userId, boardName, boardDesc, category, isPrivate]
#          types = ["string", "string", "string", "string", "string"]
#          keyObj = self.dbconn.createKey_Obj(boardName)
#          bins = self.dbconn.createBins_general(bin_name, values, types, 5)
#          self.dbconn.writeToDB("AllBoards", keyObj, bins, 5)
           if result == True:
               print '------------------------------------------------------------------------------------------'
               print 'Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board'
               print '------------------------------------------------------------------------------------------'
               # Create response to Client
               url = '/users/'+ userId+ '/boards/'+ boardName+ '/'
               urlgetBoards = {}
               urlgetBoards['url'] = url
               urlgetBoards['method'] = 'GET'
         
               updateBoard = {}
               updateBoard['url'] = url
               updateBoard['method'] = 'PUT'
            
               deleteBoard = {}
               deleteBoard['url'] = url
               deleteBoard['method'] = 'DELETE'
         
               createPin = {}
               createPin['url'] = url + 'pins/'
               createPin['method'] = 'POST'
            
               list = [urlgetBoards, updateBoard, deleteBoard, createPin]
               # print 'DEBUG: reading from DB'
               # self.dbconn.readFromDB("AllBoards",keyObj)
               # Return result to Client
               links = {}
               links["links"] = list
               return str(links)
           else:
               return '** BoardName '+boardName+ ' already exists for user '+userId
      except:
         return 'Failed.!'

#
# Return All the boards for a UserId
   def getBoards(self, userId):
      if not self.session.isSessionExists(userId):
         return "Login First!!"  
      print '--> getBoards for user', userId
      try:
         if True == True:
             boardlist = self.dbconn.getUserBoards(userId)
             if boardlist == None:
                 return '** No Boards exist for the user '+userId
             else:
                 boardDetails = []
                 for item in boardlist:
                     if item != None:
                         res = self.dbconn.getBoardDetails(userId, item)
                         if res != None:
                             boardDetails.append(res)
                 boards = {}
                 boards["Boards"] = boardDetails
                 return str(boards)
      except:
          return 'Failed.!'


#
# Return a single board value for a UserID
   def getABoard(self, userid, boardname):
        if not self.session.isSessionExists(userid):
           return "Login First!!"  
        print '--> Get a single Board'
        try:
            board_keyvalue = self.dbconn.getBoardDetails(userid, boardname)
            if board_keyvalue == None:
                return '** No Board Details for '+boardname + 'for user '+userid
            else :
                print '------------------------------------------------------------------------------------------------'
                print '** Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board **'
                print '------------------------------------------------------------------------------------------------'
                url = '/users/'+ userid+ '/boards/'+ boardname+ '/'
                updateBoard = {}
                updateBoard['url'] = url
                updateBoard['method'] = 'PUT'
            
                deleteBoard = {}
                deleteBoard['url'] = url
                deleteBoard['method'] = 'DELETE'
            
                createPin = {}
                createPin['url'] = url + 'pins/'
                createPin['method'] = 'POST'
            
                listlinks = [updateBoard, deleteBoard, createPin]
                
                board_keyvalue["links"] = listlinks
                
                boards = {}
                boards["board"] = board_keyvalue
                return str(boards)
            
        except:
            return 'Failed.!'

#
# Update a Board's Details
   def updateBoard(self, id, boardname, boardDesc, category, isPrivate):
        if not self.session.isSessionExists(id):
           return "Login First!!"  
        print '--> Update a Board'
#         try:
        if True == True:
            result = self.dbconn.updateBoard(id, boardname, boardDesc, category, isPrivate)
            if result == True:
                print '----------------------------------------------------------------------------------------------------------------'
                print '** Please find links for Viewing Board Details/ Updating Board/ Deleting Board/ Creating a pin on the Board **'
                print '----------------------------------------------------------------------------------------------------------------'
                url = '/users/'+ id+ '/boards/'+ boardname+ '/'
                urlgetBoards = {}
                urlgetBoards['url'] = url
                urlgetBoards['method'] = 'GET'
            
                updateBoard = {}
                updateBoard['url'] = url
                updateBoard['method'] = 'PUT'
             
                deleteBoard = {}
                deleteBoard['url'] = url
                deleteBoard['method'] = 'DELETE'
            
                createPin = {}
                createPin['url'] = url + 'pins/'
                createPin['method'] = 'POST'
            
                listlinks = [updateBoard, deleteBoard, createPin]
                links = {}
                links["links"] = listlinks
                return str(links)
            else:
                return 'No Board found with the BoardName : '+boardname + ' for user '+id
          
#         except:
#             return 'Failed.!'
            
#
#delete from board
   def deleteBoard(self, userId, boardName):
       if not self.session.isSessionExists(userId):
          return "Login First!!"  
       print '--> Delete a Board'
       try:
           result = self.dbconn.deleteBoard(userId, boardName)
           if result == True:
               print '-----------------------------------------------------------------------'
               print '** Please find links for Viewing Board Details/ Creating a new Board **'
               print '-----------------------------------------------------------------------'
               urlgetBoards = {}
               urlgetBoards['url'] = '/users/'+ userId+ '/boards/'+ boardName+ '/'
               urlgetBoards['method'] = 'GET'
           
               createBoard = {}
               createBoard['url'] = '/users/'+ userId+ '/boards/'
               createBoard['method'] = 'POST'
           
               listBoards = [urlgetBoards, createBoard]
               links = {}
               links["links"] = listBoards
               return str(links)
           else:
               return '** Board cannot be deleted.! **'
       
       except:
           return 'Failed.!'