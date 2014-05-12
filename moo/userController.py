'''
Created on May 5, 2014
File for userController - Login and Register
'''

# bottle framework
from bottle import request, response, route, run, template
from UsersData import UsersData

# virtual classroom implementation
user = None

def usersetup(base, conf_fn):
   print '\n**** User initialization ****\n'
   global user 
   user = UsersData(base, conf_fn)

# setup the configuration for our service
@route('/')
def root():
   print "--> login"
   return '**Welcome to PinItUp**'


@route('/users/login/', method='POST')
def loginUser():
   print '---> Login for User'
   username = request.forms.get('username')
   password = request.forms.get('password')
   response.status = 200
   return user.login(username, password)
   #    return 'Login result'
   
#
# Logout function
#
@route('/users/<username>/logout/', method='GET')
def logoutUser(username):
    print '--> User Logout'
    return user.logout(username)
   
@route('/users/signup/', method='POST')
def signup():
    firstName = request.forms.get('firstName')
    lastName = request.forms.get('lastName')
    emailId = request.forms.get('emailId')
    password = request.forms.get('password')
    return user.signup(firstName, lastName, emailId, password)

