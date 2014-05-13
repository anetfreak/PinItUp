import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template
from Comments import Comments

comments = None

def commentsetup(base,conf_fn):
    print '\n**** comments initialization ****\n'
    global comments
    comments = Comments(base,conf_fn)

@route('/')
def root():
    print "--> root"
    return 'Welcome to PinItUp'

#
# Adding a comments to a pin
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment/', method='POST')
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment', method='POST')
def createComment(id, boardname, pinId):
    print '---> create comment for the pin :',pinId
    description = request.forms.get('description')
    return comments.add(id, boardname, pinId, description)

#
#Get list of comments for a particular pin
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment/', method='GET')
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment', method='GET')
def getComments(id, boardname, pinId):
    print '--> Retrieving all comments for the Pin: '+pinId
    return comments.getComments(id, boardname, pinId)

#
#Update a comment based on pin name
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment/<commentId>/', method='PUT')
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment/<commentId>', method='PUT')
def updateComment(id, boardname, pinId, commentId):
    print '---> Update comment for a pin : '+pinId
    description = request.forms.get('description')
    return comments.updateComment(commentId, description)

#
# Delete a pin
#
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment/<commentId>/', method='DELETE')
@route('/users/<id>/boards/<boardname>/pins/<pinId>/comment/<commentId>', method='DELETE')
def deleteComment(id, boardname, pinId, commentId):
    print '--> Delete a comment for user :',id , 'in pin : ', pinId
    return comments.deleteComment(id, boardname, pinId, commentId)


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
