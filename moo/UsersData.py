import sys
import os
import socket
import StringIO
import json

# moo 
# from data.storage import Storage

class UsersData(object):
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

     
     #
     # login method for user
     #
   def login(self, username, password):
       print '--> Login check for username : ', username, 'and password --> ', password
       try:
           if username == "admin":
               urlgetBoard = {}
               urlgetBoard['urlgetBoard'] = '/users/',username,'/boards/'
               urlgetBoard['method'] = 'GET'
               urladdBoard = {}
               urladdBoard['urladdBoard'] = '/users/',username,'/boards/'
               urladdBoard['method'] = 'POST'
               listBoards = [urlgetBoard, urladdBoard]
               print '--------------------------------------'
               print '*** Log In Successful.! ***'
               print 'Please find links for Get/Add Boards'
               print '-------------------------------------- \n\n'
               return str(listBoards)
           else:
               print 'User does not exists.!'
       except:
           print 'Error Encountered in Login..!'

    #
    # signup method for user
    #
   def signup(self, firstName, lastName, emailId, password):
        print '--------------------------------------'
        print '** Signing Up New User Details **'
        print 'First Name : ', firstName
        print 'Last Name : ', lastName
        print 'Email : ', emailId
        print 'Password : ', password
        print '--------------------------------------'
        try:
            print '\n \n** Congrats..! You are a registered User of PinItUp.! **'
            print 'Please find link for login \n \n'
            urllogin = {}
            urllogin['urllogin'] = '/users/login'
            urllogin['method'] = 'POST'
            listLogin = [urllogin]
            return str(listLogin)
        except:
            print '--> Error encountered in SignUp.!'

        
