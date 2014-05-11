import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template
from Comments import Comments

comments = None

def pinsetup(base,conf_fn):
    print '\n**** comments initialization ****\n'
    global pin 
    comments = Comments(base,conf_fn)

@route('/')
def root():
    print "--> root"
    return 'Welcome to PinItUp'

#
# Adding a comments to a pin
#
@route('/users/<userId>/boards/<boardName>/pins/<pinId>/comment/', method='POST')
def createPin(userId, boardName, pinId):
    print '---> create comment for the pin :',pinId
    description = request.forms.get('description')
    return comments.add(userId, boardName, pinId)

#
#Get list of pins for a particular board
#
@route('/users/<userId>/<boardName>/pins/', method='GET')
def getPins(userId, boardName):
    print '--> Retrieving all pins for the Board'
    return pin.getPins(userId, boardName)

#
# Get a single pin details for a board from DB
#
@route('/users/<userId>/boards/<boardName>/pins/<pinId>/', method='GET')
def getAPin(userId, boardName, pinId):
    print '--> Retrieving details of a pin on the board from DB'
    return pin.getAPin(userId,boardName, pinId)



def __format(request):
    #for key in sorted(request.headers.iterkeys()):
    #    print "%s=%s" % (key, request.headers[key])

    types = request.headers.get("Accept",'')
    subtypes = types.split(",")
    for st in subtypes:
        sst = st.split(';')
        if sst[0] == "text/html":
            return Comments.html
        elif sst[0] == "text/plain":
            return Comments.text
        elif sst[0] == "application/json":
            return Comments.json
        elif sst[0] == "*/*":
            return Comments.json

    # default
    return Comments.html

#
# The content type on the reply
#
def __response_format(reqfmt):
        if reqfmt == Comments.html:
            return "text/html"
        elif reqfmt == Comments.text:
            return "text/plain"
        elif reqfmt == Comments.json:
            return "application/json"
        else:
            return "*/*"
            
        # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc
