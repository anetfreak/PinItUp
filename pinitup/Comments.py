import sys
import os
import socket
import StringIO
import json

# from data.storage import Storage
from comments_dao import DBConn

class Comments(object):
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
         raise Exception("Configuration file not found..")

      self.dbconn = DBConn("127.0.0.1",5984)
      
#
# Add comment to a pin
#
   def add(self, userId, boardName, pinId, description):
      print '---> comments.add: userId:', userId, ' boardName:', boardName, 'pinId:', pinId
      try:
          result = self.dbconn.createComment(userId, boardName, pinId, description)
          commentId = result
          
          print '** Please find links for Updating Comment / Deleting Comment**'
          
          url = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'+pinId+'/comment/'
          updateComment = {}
          updateComment['url'] = url
          updateComment['method'] = 'PUT'
            
          deleteComment = {}
          deleteComment['url'] = url
          deleteComment['method'] = 'DELETE'
            
          listComments = [updateComment, deleteComment]
          links = {}
          links["links"] = listComments
          return str(listComments)
         
      except:
         return 'failed'

#
# Retrieve all comments for a Pin
#
   def getComments(self,userId, boardName, pinName):
       print '--> getComments for Pin: '+ pinName
       try:
           commentDetails = self.dbconn.getUserBoardPinComments(userId, boardName, pinName)
           if commentDetails == None:
               return '** No comments exists for this pin.! **'
           else:
               comments = {}
               comments["Comments"] = commentDetails
               return str(comments)
       except:
             return 'Failed.!'
    
#
# Update a comment based on commentId
#    
   def updateComment(self, commentId, description):
        print '--> Update comment for CommentID: '+commentId
        try:
            result = self.dbconn.updateComment(commentId, description)
            if result == True:
                return '** Comment updated.! **'
            else:
                return '** Cannot update comment..! **'
        except:
            return 'Failed.!'

#
# Delete a comment for a user for a pin
#                
   def deleteComment(self, userId, boardName, pinId, commentId):
        print '--> Delete a comment'
        try:
            result = self.dbconn.deleteComment(userId, boardName, pinId, commentId)
            if result == True:
                print '** Please find links for Viewing Comments/ Adding a Comment **'
                url = '/users/' + userId + '/boards/' + boardName + '/pins/'+ pinId + '/comment/'
                commentDetails = {}
                commentDetails['url'] = url
                commentDetails['method'] = 'GET'
            
                createComment = {}
                createComment['url'] = url
                createComment['method'] = 'POST'
            
                deleteComments = [commentDetails, createComment]
                links = {}
                links["links"] = deleteComments
                return str(links)
            else :
                return '** Comment cannot be deleted.! **'
        except:
            return 'Failed.!'
        
        
   #
   # output as xml is supported through other packages. If
   # you want to add xml support look at gnosis or lxml.
   #
   def __conf_as_xml(self):
      return "xml is hard"

   #
   #
   #
   def __conf_as_json(self):
      try:
         all = {}
         all["base.dir"] = self.base
         all["conf"] = self.conf
         return json.dumps(all)
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
