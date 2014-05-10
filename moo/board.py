import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template
from Boards import Board

# virtual classroom implementation
board = None

def boardsetup(base,conf_fn):
   print '\n**** service initialization ****\n'
   global board 
   board = Board(base,conf_fn)

@route('/')
def root():
   print "--> root"
   return 'welcome to PinItUp'

@route('/users/<id>/boards', method='POST')
def createBoard(id):
   print '---> create Board for user :',id
   boardName = request.forms.get('boardName')
   boardDesc = request.forms.get('boardDesc')
   category = request.forms.get('category')
   isPrivate = request.forms.get('isPrivate')
   return board.add(boardName, boardDesc, category, isPrivate)
   #	return 'Add Board Success'


#
# Determine the format to return data (does not support images)
#
# TODO method for Accept-Charset, Accept-Language, Accept-Encoding, 
# Accept-Datetime, etc should also exist
#
def __format(request):
   #for key in sorted(request.headers.iterkeys()):
   #   print "%s=%s" % (key, request.headers[key])

   types = request.headers.get("Accept",'')
   subtypes = types.split(",")
   for st in subtypes:
      sst = st.split(';')
      if sst[0] == "text/html":
         return Board.html
      elif sst[0] == "text/plain":
         return Board.text
      elif sst[0] == "application/json":
         return Board.json
      elif sst[0] == "*/*":
         return Board.json

      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc

   # default
   return Board.html

#
# The content type on the reply
#
def __response_format(reqfmt):
      if reqfmt == Baord.html:
         return "text/html"
      elif reqfmt == Board.text:
         return "text/plain"
      elif reqfmt == Board.json:
         return "application/json"
      else:
         return "*/*"
         
      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc
