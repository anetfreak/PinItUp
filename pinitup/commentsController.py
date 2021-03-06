import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template
from Comments import Comments

comments = None

def commentsetup(base,conf_fn, session):
    print '\n**** comments initialization ****\n'
    global comments
    comments = Comments(base,conf_fn, session)

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
