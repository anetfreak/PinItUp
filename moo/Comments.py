import sys
import os
import socket
import StringIO
import json

# from data.storage import Storage

class Comments(object):
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
         raise Exception("Configuration file not found..")

      # create storage
      # self.__store = Storage()

#
# Add a pin to a board in DB
#
   def add(self, userId, boardName, pinId):
      print '---> comments.add: userId:', userId, ' boardName:', boardName, 'pinId:', pinId
      try:
          #generate a commentId  after adding a comment to the pin in the DB
          commentId = 0 #to be changed
          
          updateComment = {}
          updateComment['updateComment'] = '/users/', userId, '/boards/', boardName, '/pins/',pinId,'/comment'
          updateComment['method'] = 'PUT'
            
          deleteComment = {}
          deleteComment['deleteComment'] = '/users/', userId, '/boards/', boardName, '/pins/',pinId,'/comment'
          deleteComment['method'] = 'DELETE'
            
          listComments = [updateComment, deleteComment]
          return str(listComments)
         
      except:
         return 'failed'

#
# Retreive all pins for a board
#
   def getPins(self,userId, boardName):
       print '--> getPins for board', boardName
       try:
           #TODO : fetch list of pins for a board from DB
           return str(list)
       except:
             return 'Failed.!'
    
    
   #
   #Retreive details of a pin
   #
   def getAPin(self, userId, boardName, pinId):
       print'--> get a pin details on a board'
       #TODO : fetch the board details from the db
       print 'Please find links for Updating Board Details/ Deleting Board/ Creating a pin on the Board'
       updatePin = {}
       updatePin['updatePin'] = '/users/',userId,'/boards/',boardName,'/pins/',pinId,'/'
       updatePin['method'] = 'PUT'
           
       deletePin = {}
       deletePin['deletePin'] = '/users/',userId,'/boards/',boardName,'/pins/',pinId,'/'
       deletePin['method'] = 'DELETE'
           
       comments = {}
       comments['comments'] = '/users/',userId,'/boards/',boardName,'/pins/',pinId,'/'
       comments['method'] = 'POST'
           
       pins = [updatePin, deletePin, comments]
       return str(pins)

            
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
