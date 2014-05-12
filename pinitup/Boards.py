import sys
import os
import socket
import StringIO
import json

from board_dao import DBConn

class Board(object):
   json, xml, html, text = range(1, 5)

   # setup the configuration for our service
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

      self.dbconn = DBConn("127.0.0.1",5984)


   def createBoard(self, userId, boardName, boardDesc, category, isPrivate):
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
               print 'Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board'
               # Create response to Client
               url = 'users/'+ userId+ '/boards/'+ boardName+ '/'
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
               createPin['url'] = url + '/pins/'
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
         print '--> getBoards for user', userId
         #try:
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
         #except:
         #    return 'Failed.!'


#
# Return a single board value for a UserID
   def getABoard(self, userid, boardname):
        print '--> Get a single Board'
        try:
            board_keyvalue = self.dbconn.getBoardDetails(userid, boardname)
            if board_keyvalue == None:
                return '** No Board Details for '+boardname + 'for user '+userid
            else :
                print '** Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board **'
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
   def updateBoard(self, userId, boardName, boardDesc, category, isPrivate):
        print '--> Update a Board'
        try:
            result = self.dbconn.updateBoard(userId, boardName, boardDesc, category, isPrivate)
            if result == True:
                print '** Please find links for Viewing Board Details/ Updating Board/ Deleting Board/ Creating a pin on the Board **'
                url = 'users/'+ userId+ '/boards/'+ boardName+ '/'
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
                return 'No Board found with the BoardName : '+boardName + ' for user '+userId
          
        except:
            return 'Failed.!'
            
#
#delete from board
   def deleteBoard(self, userId, boardName):
       print '--> Delete a Board'
       try:
           result = self.dbconn.deleteBoard(userId, boardName)
           if result == True:
               print '** Please find links for Viewing Board Details/ Creating a new Board **'
               urlgetBoards = {}
               urlgetBoards['url'] = 'users/'+ userId+ '/boards/'+ boardName+ '/'
               urlgetBoards['method'] = 'GET'
           
               createBoard = {}
               createBoard['url'] = 'users/'+ userId+ '/boards/'
               createBoard['method'] = 'POST'
           
               listBoards = [urlgetBoards, createBoard]
               links = {}
               links["links"] = listBoards
               return str(links)
           else:
               return '** Board cannot be deleted.! **'
       
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
