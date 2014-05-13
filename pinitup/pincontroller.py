# bottle framework
from bottle import request, route
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
@route('/users/<id>/boards/<boardname>/pins/', method='POST')
def createPin(id, boardname):
    print '---> create Pin for user :',id , 'in board : ', boardname
    image = request.forms.get('image')
    pinDesc = request.forms.get('description')
    pinName = request.forms.get('pinName')
    return pin.add(id, pinName, pinDesc, image, boardname)

#
#Get list of pins for a particular board
#
@route('/users/<id>/boards/<boardname>/pins/', method='GET')
def getPins(id, boardname):
    print '--> Retrieving all pins for the Board'
    return pin.getPins(id, boardname)

#
# Get a single pin details for a board from DB
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/', method='GET')
def getAPin(id, boardname, pinId):
    print '--> Retrieving details of a pin on the board from DB'
    return pin.getAPin(id,boardname, pinId)

#
#Update a pin based on board name
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/', method='PUT')
def updatePin(id, boardname, pinId):
    print '---> create Pin for user :',id , 'in board : ', boardname
    image = request.forms.get('image')
    pinDesc = request.forms.get('description')
    pinName = request.forms.get('pinName')
    return pin.updatePin(id, pinName, pinDesc, image, boardname)

#
# Delete a pin
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/', method='DELETE')
def deletePin(id, boardname, pinId):
    print '--> Delete a pin for user :',id , 'in board : ', boardname
    return pin.deletePin(id, boardname, pinId)


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
