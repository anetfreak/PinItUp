import os
import socket
import StringIO
import json

# from pin_dao import DBConn
from pin_dao import DBConn
from SessionManager import SessionManager

class Pin(object):
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
         raise Exception("Configuration file not found..")

      self.dbconn = DBConn("127.0.0.1", 5984)
      self.session = session
#
# add a new pin
#
   def add(self, userId, pinName, pinDesc, image, boardName, imageUrl):
      if not self.session.isSessionExists(userId):
          return "Login First!!"
      print '---> pin.add: userId:', userId, ' pinDesc:', pinDesc, 'pinName: ', pinName, 'image:', image, ' boardName:', boardName
#       try:
      if True==True:
          result = self.dbconn.createPin(userId, pinName, pinDesc, image, boardName, imageUrl)
          if result == True:
              print '--------------------------------------------------------------------------------------------'
              print '** Please find links for Viewing Pin Details/ Updating Pin Details/ Deleting Pin Details **'
              print '--------------------------------------------------------------------------------------------'
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
              
              addComment = {}
              addComment['url'] = url + 'comment/'
              addComment['method'] = 'POST'
            
              listlinks = [pinDetails, updatePin, deletePin, addComment]
              links = {}
              links["links"] = listlinks
              return str(links)
          else:
              return '** Pin cannot be created.! **'
         
#       except:
#          return 'Failed.! '

#
# Retrieve all pins for a board
   def getPins(self, userId, boardName):
       if not self.session.isSessionExists(userId):
          return "Login First!!"
       print '--> Get all pins for BoardName :' + boardName
       try:
           listPins = self.dbconn.getUserBoardPins(userId, boardName)
           if listPins == None:
               return '** No pins exist for the Board : ' + boardName
           else:
               listPinDetails = []
               for pinName in listPins:
                   if pinName != None:
                       pindetails = self.dbconn.getPinDetails(userId,boardName,pinName)
                       if pindetails != None:
                           listPinDetails.append(pindetails)
               pins = {}
               pins["Pins"] = listPinDetails
               return str(pins)
       except:
             return 'Failed.!'
    
    
   #
   # Retrieve details of a pin
   def getAPin(self, userId, boardName, pinId):
       if not self.session.isSessionExists(userId):
          return "Login First!!"
       print'--> Get a Pin detail on a board'
       try:
           pindetails = self.dbconn.getPinDetails(userId, boardName, pinId)
           if pindetails == None:
               return '** No pin details exist for the Pin : ' + pinId
           else :
               print '--------------------------------------------------------------------------------------------'
               print '** Please find links for Updating Pin Details/ Deleting Pin/ Adding a comment on the Pin **'
               print '--------------------------------------------------------------------------------------------'
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
               
               
               listlink = [updatePin, deletePin, comments]
               pindetails["links"] = listlink
               resp = {}
               resp["board"] = pindetails
               return str(resp)
       except:
           return 'Failure.!'
       
   #
   # Update a Pin for a Board
   def updatePin(self, userId, pinName, pinDesc, image, boardName):
       if not self.session.isSessionExists(userId):
          return "Login First!!"
       print '--> Update a Pin'
       try:
           result = self.dbconn.updatePin(userId, pinName, pinDesc, image, boardName)
           if result == True:
               print '----------------------------------------------------------------------------------'
               print '** Please find links for Viewing Pin Details/ Adding a Pin/ Updating Pin Details**'
               print '----------------------------------------------------------------------------------'
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
       
               listlinks = [pinDetails, createPin, updatePin]
               links = {}
               links["links"] = listlinks
               return str(links)
           else:
               return '** Pin not updated.! **'
       except:
           return 'Failed.!'
    
    
    #
    # Delete a Pin for a Board
   def deletePin(self, userId, boardName, pinId):
        if not self.session.isSessionExists(userId):
            return "Login First!!"
        print '--> Delete a pin'
        try:
            result = self.dbconn.deletePin(userId, boardName, pinId)
            if result == True:
                print '-----------------------------------------------------------------'
                print '** Please find links for Viewing Pin Details/ Adding a new Pin **'
                print '-----------------------------------------------------------------'
                url = '/users/' + userId + '/boards/' + boardName + '/pins/'
                pinDetails = {}
                pinDetails['url'] = url
                pinDetails['method'] = 'GET'
            
                createPin = {}
                createPin['url'] = url
                createPin['method'] = 'POST'
            
                listlinks = [pinDetails, createPin]
                links = {}
                links["links"] = listlinks
                return str(links)
            else :
                return '** Pin cannot be deleted.! **'
        except:
            return 'Failed.!'
