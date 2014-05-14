# bottle framework
from bottle import request, route, static_file
from Pin import Pin

pin = None

def pinsetup(base,conf_fn, session):
    print '\n**** pin initialization ****\n'
    global pin 
    pin = Pin(base,conf_fn, session)

@route('/')
def root():
    print "--> root"
    return 'Welcome to PinItUp'

#
# Adding a pin to a board
#
@route('/users/<id>/boards/<boardname>/pins/', method='POST')
@route('/users/<id>/boards/<boardname>/pins', method='POST')
def createPin(id, boardname):
    print '---> create Pin for user :',id , 'in board : ', boardname
    image = request.forms.get('image')
    pinDesc = request.forms.get('description')
    pinName = request.forms.get('pinName')
    #upload image file
    filedata = request.files.data
    imageUrl = ""
    if filedata and filedata.file:
        #raw = filedata.file.read()
        filename = filedata.filename
        filepath = './static/files'+'/'+id+'/'+boardname+'/'+pinName+'/'+filename
        with open(filepath,'w') as open_file:
            open_file.write(filedata.file.read())
        imageUrl = '/users/'+id+'/boards/'+boardname+'/pins/'+pinName+'/file/'+filename
    return pin.add(id, pinName, pinDesc, image, boardname, imageUrl)

#
#Get list of pins for a particular board
#
@route('/users/<id>/boards/<boardname>/pins/', method='GET')
@route('/users/<id>/boards/<boardname>/pins', method='GET')
def getPins(id, boardname):
    print '--> Retrieving all pins for the Board'
    return pin.getPins(id, boardname)

#
# Get a single pin details for a board from DB
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/', method='GET')
@route('/users/<id>/boards/<boardname>/pins/<pinId>', method='GET')
def getAPin(id, boardname, pinId):
    print '--> Retrieving details of a pin on the board from DB'
    return pin.getAPin(id,boardname, pinId)

#
#Update a pin based on board name
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/', method='PUT')
@route('/users/<id>/boards/<boardname>/pins/<pinId>', method='PUT')
def updatePin(id, boardname, pinId):
    print '---> create Pin for user :',id , 'in board : ', boardname
    image = request.forms.get('image')
    pinDesc = request.forms.get('description')
    #pinName = request.forms.get('pinName')
    return pin.updatePin(id, pinId, pinDesc, image, boardname)

#
# Delete a pin
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/', method='DELETE')
@route('/users/<id>/boards/<boardname>/pins/<pinId>', method='DELETE')
def deletePin(id, boardname, pinId):
    print '--> Delete a pin for user :',id , 'in board : ', boardname
    return pin.deletePin(id, boardname, pinId)

@route('/users/<id>/boards/<boardname>/pins/<pinId>/file/<filename>', method='GET')
def getImageFile(id,boardname,pinId,filename):
    filepath = '/'+id+'/'+boardname+'/'+pinId+'/'+filename
    return static_file(filepath,'./static/files')
    #return pin.getImageFile(id,boardname,pinId,filename)
    #return static_file(filepath, root='/path/to/your/static/files')