import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template
from Pin import Pin

pin = None

def pinsetup(base,conf_fn):
    print '\n**** pin initialization ****\n'
    global pin 
    pin = Pin(base,conf_fn)

@route('/')
def root():
    print "--> root"
    return 'Welcome to PinItUp'

#
# Adding a pin to a board
#
@route('/users/<userId>/boards/<boardName>/pins/', method='POST')
def createPin(userId, boardName):
    print '---> create Pin for user :',userId , 'in board : ', boardName
    image = request.forms.get('image')
    pinDesc = request.forms.get('description')
    pinName = request.forms.get('pinName')
    return pin.add(userId, pinName, pinDesc, image, boardName)

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
@route('/users/<userId>/boards/<boardName>/pins/<pinId>', method='GET')
def getAPin(userId, boardName, pinId):
    print '--> Retrieving details of a pin on the board from DB'
    return pin.getAPin(userId,boardName, pinId)

#
#Update a pin based on board name
#
@route('/users/<userId>/boards/<boardName>/pins/<pinId>', method='PUT')
def updatePin(userId, boardName, pinId):
    print '---> create Pin for user :',userId , 'in board : ', boardName
    image = request.forms.get('image')
    pinDesc = request.forms.get('description')
    pinName = request.forms.get('pinName')
    return pin.updatePin(userId, pinName, pinDesc, image, boardName)

#
# Delete a pin
#
@route('/users/<userId>/boards/<boardName>/pins/<pinId>', method='DELETE')
def deletePin(userId, boardName, pinId):
    print '--> Delete a pin for user :',userId , 'in board : ', boardName
    return deletePin(userId, boardName, pinId)


def __format(request):
    #for key in sorted(request.headers.iterkeys()):
    #    print "%s=%s" % (key, request.headers[key])

    types = request.headers.get("Accept",'')
    subtypes = types.split(",")
    for st in subtypes:
        sst = st.split(';')
        if sst[0] == "text/html":
            return Pin.html
        elif sst[0] == "text/plain":
            return Pin.text
        elif sst[0] == "application/json":
            return Pin.json
        elif sst[0] == "*/*":
            return Pin.json

    # default
    return Pin.html

#
# The content type on the reply
#
def __response_format(reqfmt):
        if reqfmt == Pin.html:
            return "text/html"
        elif reqfmt == Pin.text:
            return "text/plain"
        elif reqfmt == Pin.json:
            return "application/json"
        else:
            return "*/*"
            
        # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc
