import os
import socket
import StringIO
import json

# from pin_dao import DBConn
from pin_dao import DBConn

class Pin(object):
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

      self.dbconn = DBConn("127.0.0.1", 5984)
      
#
# add a new pin
#
   def add(self, userId, pinName, pinDesc, image, boardName):
      print '---> pin.add: userId:', userId, ' pinDesc:', pinDesc, 'pinName: ', pinName, 'image:', image, ' boardName:', boardName
      try:
          result = self.dbconn.createPin(userId, pinName, pinDesc, image, boardName)
          if result == True:
              print '** Please find links for Viewing Pin Details/ Updating Pin Details/ Deleting Pin Details **'
              url = '/users/' + userId + '/boards/' + boardName + '/pins/' + pinName + '/'
              pinDetails = {}
              pinDetails['url'] = url
              pinDetails['method'] = 'GET'
            
              updatePin = {}
              updatePin['url'] = url
              updatePin['method'] = 'PUT'
            
              deletePin = {}
              deletePin['url'] = url
              deletePin['method'] = 'DELETE'
            
              listlinks = [pinDetails, updatePin, deletePin]
              links = {}
              links["links"] = listlinks
              return str(links)
          else:
              return '** Pin cannot be created.! **'
         
      except:
         return 'Failed.! '

#
# Retrieve all pins for a board
   def getPins(self, userId, boardName):
       print '--> Get all pins for BoardName :' + boardName
       try:
           listPins = self.dbconn.getUserBoardPins(userId, boardName)
           if listPins == None:
               return '** No pins exist for the Board : ' + boardName
           else:
               listPinDetails = []
               for pinName in listPins
                   if pinName != None
                       pindetails = self.dbconn.getPinDetails(userId,boardName,pinName)
                       if pindetails != None
                           listPinDetails.append(pindetails)
               pins = {}
               pins["Pins"] = listPinDetails
               return str(pins)
       except:
             return 'Failed.!'
    
    
   #
   # Retrieve details of a pin
   def getAPin(self, userId, boardName, pinId):
       print'--> Get a Pin detail on a board'
       try:
           list = self.dbconn.getPinDetails(userId, boardName, pinId)
           if list == None:
               return '** No pin details exist for the Pin : ' + pinId
           else :
               print '** Please find links for Updating Pin Details/ Deleting Pin/ Adding a comment on the Pin **'
               url = '/users/' + userId + '/boards/' + boardName + '/pins/' + pinId + '/'
               updatePin = {}
               updatePin['url'] = url
               updatePin['method'] = 'PUT'
           
               deletePin = {}
               deletePin['url'] = url
               deletePin['method'] = 'DELETE'
           
               comments = {}
               comments['url'] = url
               comments['method'] = 'POST'
           
               pins = [updatePin, deletePin, comments]
               return str(pins)
       except:
           return 'Failure.!'
       
   #
   # Update a Pin for a Board
   def updatePin(self, userId, pinName, pinDesc, image, boardName):
       print '--> Update a Pin'
       try:
           result = self.dbconn.updatePin(userId, pinName, pinDesc, image, boardName)
           if result == True:
               print '** Please find links for Viewing Pin Details/ Adding a Pin/ Updating Pin Details**'
               url ='/users/' + userId + '/boards/' + boardName + '/pins/'
               pinDetails = {}
               pinDetails['url'] = url
               pinDetails['method'] = 'GET'
       
               createPin = {}
               createPin['url'] = url
               createPin['method'] = 'POST'
        
               updatePin = {}
               updatePin['url'] = url + pinName + '/'
               updatePin['method'] = 'PUT'
       
               pins = [pinDetails, createPin, updatePin]
               return str(pins)
           else:
               return '** Pin not updated.! **'
       except:
           return 'Failed.!'
    
    
    #
    # Delete a Pin for a Board
   def deletePin(self, userId, boardName, pinId):
        print '--> Delete a pin'
        try:
            result = self.dbconn.deletePin(userId, boardName, pinId)
            if result == True:
                print '** Please find links for Viewing Pin Details/ Adding a new Pin **'
                url = '/users/' + userId + '/boards/' + boardName + '/pins/'
                pinDetails = {}
                pinDetails['url'] = url
                pinDetails['method'] = 'GET'
            
                createPin = {}
                createPin['url'] = url
                createPin['method'] = 'POST'
            
                deletePins = [pinDetails, createPin]
                return str(deletePins)
            else :
                return '** Pin cannot be deleted.! **'
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
