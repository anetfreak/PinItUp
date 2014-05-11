import sys
import os
import socket
import StringIO
import json

# from data.storage import Storage

class Pin(object):
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

   def add(self, userId, pinName, pinDesc, image, boardName):
      print '---> pin.add: userId:', userId, ' pinDesc:', pinDesc, 'pinName: ', pinName, 'image:', image, ' boardName:', boardName
      try:
          
          #generate a pinID after creating a PIN from the DB
          pinId = 0 #to be changed
          pinDetails = {}
          pinDetails['pinDetails'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'+pinId+'/'
          pinDetails['method'] = 'GET'
            
          updatePin = {}
          updatePin['updatePin'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'+pinId+'/'
          updatePin['method'] = 'PUT'
            
          deletePin = {}
          deletePin['deletePin'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'+pinId+'/'
          deletePin['method'] = 'DELETE'
            
          listPins = [pinDetails, updatePin, deletePin]
          return str(listPins)
         
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
       updatePin['updatePin'] = '/users/'+userId+'/boards/'+boardName+'/pins/'+pinId+'/'
       updatePin['method'] = 'PUT'
           
       deletePin = {}
       deletePin['deletePin'] = '/users/'+userId+'/boards/'+boardName+'/pins/'+pinId+'/'
       deletePin['method'] = 'DELETE'
           
       comments = {}
       comments['comments'] = '/users/'+userId+'/boards/'+boardName+'/pins/'+pinId+'/'
       comments['method'] = 'POST'
           
       pins = [updatePin, deletePin, comments]
       return str(pins)

   #
   #Update a Pin for a Board
   #
   def updatePin(self, userId, boardName, pinId):
       print '--> Update a Pin'
       #TODO : 
       try:
           pinDetails = {}
           pinDetails['pinDetails'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'
           pinDetails['method'] = 'GET'
       
           createPin = {}
           createPin['createPin'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'
           createPin['method'] = 'POST'
        
           updatePin = {}
           updatePin['updatePin'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'+pinId+'/'
           updatePin['method'] = 'PUT'
       
           pins = [pinDetails, createPin, updatePin]
           return str(pins)
       except:
           return 'Failed.!'
    
    
    #
    # Delete a Pin for a Board
    #
   def deletePin(self, userId, boardName, pinId):
        print '--Delete a pin'
        try:
            pinDetails = {}
            pinDetails['pinDetails'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'
            pinDetails['method'] = 'GET'
            
            createPin = {}
            createPin['createPin'] = '/users/'+ userId+ '/boards/'+ boardName+ '/pins/'
            createPin['method'] = 'POST'
            
            deletePins = [pinDetails, createPin]
            return str(deletePins)
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
