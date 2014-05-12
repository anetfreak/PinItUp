import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template
from Comments import Comments

comments = None

def commentsetup(base,conf_fn):
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
def createComment(userId, boardName, pinId):
    print '---> create comment for the pin :',pinId
    description = request.forms.get('description')
    return comments.add(userId, boardName, pinId, description)

#
#Get list of comments for a particular pin
#
@route('/users/<userId>/<boardName>/pins/<pinId>/comment/', method='GET')
def getComments(userId, boardName, pinId):
    print '--> Retrieving all comments for the Pin: '+pinId
    return comments.getComments(userId, boardName, pinId)

#
#Update a comment based on pin name
#
@route('/users/<userId>/boards/<boardName>/pins/<pinId>/<commentId>', method='PUT')
def updateComment(userId, boardName, pinId, commentId):
    print '---> Update comment for a pin : '+pinId
    description = request.forms.get('description')
    return comments.updateComment(commentId, description)

#
# Delete a pin
#
@route('/users/<userId>/boards/<boardName>/pins/<pinId>/<commentId>', method='DELETE')
def deleteComment(userId, boardName, pinId, commentId):
    print '--> Delete a comment for user :',userId , 'in pin : ', pinId
    return comments.deleteComment(userId, boardName, pinId, commentId)


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
