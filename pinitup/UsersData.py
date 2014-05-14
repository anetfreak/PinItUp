import sys
import os
import socket
import StringIO
import json

# moo 
# from data.storage import Storage
from user_dao import DBConn
from SessionManager import SessionManager
class UsersData(object):
   # very limited content negotiation support - our format choices 
   # for output. This also shows _a way_ of representing enums in python
   json, xml, html, text = range(1, 5)
   
   
   #
   # setup the configuration for our service
   #
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

      # create storage
      self.dbconn = DBConn("127.0.0.1",5984)
      self.session = session
     #
     # login method for user
     #
   def login(self, username, password):
       print '--> Login check for username : ', username, 'and password --> ', password
       try:
           result = self.dbconn.userSignIn(username, password)
           if result == True:
               if not self.session.isSessionExists(username):
                   self.session.addSession(username)
                   
               urlgetBoard = {}
               urlgetBoard['url'] = '/users/'+username+'/boards/'
               urlgetBoard['method'] = 'GET'
               urladdBoard = {}
               urladdBoard['url'] = '/users/'+username+'/boards/'
               urladdBoard['method'] = 'POST'
               listBoards = [urlgetBoard, urladdBoard]
               print '--------------------------------------'
               print '*** Log In Successful.! ***'
               print 'Please find links for Get/Add Boards'
               print '-------------------------------------- \n\n'
               links = {}
               links["links"] = listBoards
               return str(links)
           else:
               print 'User does not exist.!'
       except:
           print 'Error Encountered in Login..!'

    #
    #Logout
    #
   def logout(self, username):
        print '--> Logout for user : ',username
        try:
            self.session.removeSessionCache(username)    
            urllogin = {}
            urllogin['url'] = '/users/login/'
            urllogin['method'] = 'POST'
            listLogin = [urllogin]
            
            signup = {}
            signup['url'] = '/users/signup/'
            signup['method'] = 'POST'
            
            listlinks = [urllogin, signup]
            links = {}
            links["links"] = listlinks
            return str(links)
        except:
            return 'Failure!'
        
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
            result = self.dbconn.userSignUp(firstName, lastName, emailId, password)
            if result == True:
                print '\n \n** Congrats..! You are now a registered User of PinItUp.! **'
                print 'Please find link for login \n \n'
                urllogin = {}
                urllogin['url'] = '/users/login/'
                urllogin['method'] = 'POST'
                listLogin = [urllogin]
                links = {}
                links["links"] = listLogin
                return str(links)
            else:
                return False
        except:
            print '--> Error encountered in SignUp.!'

        
