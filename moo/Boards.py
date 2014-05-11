import sys
import os
import socket
import StringIO
import json

# moo 
# from data.storage import Storage
from boards_dao import DBConn

class Board(object):
   # very limited content negotiation support - our format choices 
   # for output. This also shows _a way_ of representing enums in python
   json, xml, html, text = range(1, 5)
   
   #
   # setup the configuration for our service
   #
   def __init__(self, base, conf_fn):
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

      # create storage
      self.dbconn = DBConn()
      
      
      # self.__store = Storage()

   def createBoard(self, userId, boardName, boardDesc, category, isPrivate):
      print '---> board.add: boardName:', boardName, ' boardDesc:', boardDesc, ' category:', category, ' isPrivate:', isPrivate
      try:
         # Insert userId and Board mapping in DB (key = User Id)
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

         print 'Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board'
         # Create response to Client
         urlgetBoards = {}
         urlgetBoards['urlgetBoards'] = 'users/', userId, '/boards/', boardName, '/'
         urlgetBoards['method'] = 'GET'
         
         updateBoard = {}
         updateBoard['updateBoard'] = '/users/', userId, '/boards/', boardName, '/'
         updateBoard['method'] = 'PUT'
            
         deleteBoard = {}
         deleteBoard['deleteBoard'] = '/users/', userId, '/boards/', boardName, '/'
         deleteBoard['method'] = 'DELETE'
         
         createPin = {}
         createPin['createPin'] = 'users/', userId, '/boards/', boardName, '/pins/'
         createPin['method'] = 'POST'
            
         list = [urlgetBoards, updateBoard, deleteBoard, createPin]
         # print 'DEBUG: reading from DB'
         # self.dbconn.readFromDB("AllBoards",keyObj)
         # Return result to Client
         return str(list)
      except:
         return 'Failed.!'

#
# Return All the boards for a UserId
#
   def getBoards(self, userId):
         print '--> getBoards for user', userId
         try:
             keyObj = self.dbconn.createKey_Obj(userId)
             list = self.dbconn.readFromDB("UserBoards", keyObj)
             return str(list)
         except:
             return 'Failed.!'


#
# Return a single board value for a UserID
#
   def getABoard(self, userid, boardname):
        print '--> Get a single Board'
        try:
            # TODO : fetch the board details from the db
            print 'Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board'
            updateBoard = {}
            updateBoard['updateBoard'] = '/users/', userid, '/boards/', boardname, '/'
            updateBoard['method'] = 'PUT'
            
            deleteBoard = {}
            deleteBoard['deleteBoard'] = '/users/', userid, '/boards/', boardname, '/'
            deleteBoard['method'] = 'DELETE'
            
            createPin = {}
            createPin['createPin'] = '/users/', userid, '/boards/', boardname, '/pins/'
            createPin['method'] = 'POST'
            
            listBoards = [updateBoard, deleteBoard, createPin]
            return str(listBoards)
            
        except:
            return 'Failed.!'

#
# Update a Board's Details
#
   def updateBoard(self, userId, boardName, boardDesc, category, isPrivate):
        print '--> Update a Board'
        try:
            # TODO update values for the board in DB
            urlgetBoards = {}
            urlgetBoards['urlgetBoards'] = 'users/', userId, '/boards/', boardName, '/'
            urlgetBoards['method'] = 'GET'
            
            updateBoard = {}
            updateBoard['updateBoard'] = '/users/', userId, '/boards/', boardName, '/'
            updateBoard['method'] = 'PUT'
             
            deleteBoard = {}
            deleteBoard['deleteBoard'] = '/users/', userId, '/boards/', boardName, '/'
            deleteBoard['method'] = 'DELETE'
            
            createPin = {}
            createPin['createPin'] = '/users/', userId, '/boards/', boardName, '/pins/'
            createPin['method'] = 'POST'
            
            listBoards = [updateBoard, deleteBoard, createPin]
            return str(listBoards)
          
        except:
            return 'Failed.!'
            
#
#delete from board
#
   def deleteBoard(self, userId, boardName):
       print '--> Delete a Board'
       try:
           #TODO Delete a boardName from the DB
           urlgetBoards = {}
           urlgetBoards['urlgetBoards'] = 'users/', userId, '/boards/', boardName, '/'
           urlgetBoards['method'] = 'GET'
           
           createBoard = {}
           createBoard['createBoard'] = 'users/', userId, '/boards/'
           createBoard['method'] = 'POST'
           
           listBoards = [urlgetBoards, createBoard]
           return str(listBoards)
       
       except:
           return 'Failed.!'
       
            
   def conf_as_json(self):
      try:
         url = {}
         url["url"] = 'users/{UserId}/boards/{boardName}'
         url["method"] = 'GET'
         list = [url]
         # return json.dumps(list)
         return str(list)
      except:
         return "error: unable to return configuration"

   #
   #
   #
   def __conf_as_text(self):
      try:
        sb = StringIO.StringIO()
        sb.write("Room Configuration\n")
        sb.write("base directory = ")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("configuration:\n")
        
        for key in sorted(self.conf.iterkeys()):
           print >> sb, "%s=%s" % (key, self.conf[key])
        
        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
      return "text"

   #
   #
   #
   def __conf_as_html(self):
      try:
        sb = StringIO.StringIO()
        sb.write("<html><body>")
        sb.write("<h1>")
        sb.write("Room Configuration")
        sb.write("</h1>")
        sb.write("<h2>Base Directory</h2>\n")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("<h2>Configuration</h2>\n")
        
        sb.write("<pre>")
        for key in sorted(self.conf.iterkeys()):
           print >> sb, "%s=%s" % (key, self.conf[key])
        sb.write("</pre>")
     
        sb.write("</body></html>")

        str = sb.getvalue()
        return str
      finally:
        sb.close()
