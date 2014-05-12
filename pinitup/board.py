# bottle framework
from bottle import request, route
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
   return '*** Welcome to PinItUp ***'

@route('/users/<id>/boards/', method='POST')
def createBoard(id):
   print '---> create Board for user :',id
   boardName = request.forms.get('boardName')
   boardDesc = request.forms.get('boardDesc')
   category = request.forms.get('category')
   isPrivate = request.forms.get('isPrivate')
   return board.createBoard(id,boardName, boardDesc, category, isPrivate)


#return all the boards for a User
@route('/users/<id>/boards/', method='GET')
def listBoards(id):
    print '--> List boards for a user : ',id
    return board.getBoards(id)


#Return single board for a user
@route('/users/<id>/boards/<boardname>/', method='GET')
def getABoard(id, boardname):
    print '--> retrieve a single board for the userid :',id
    return board.getABoard(id,boardname)


# update a board details
@route('/users/<id>/boards/<boardname>/', method='PUT')
def updateBoard(id, boardname):
     print '---> Update Board Details :',boardname
     boardName = request.forms.get('boardName')
     boardDesc = request.forms.get('boardDesc')
     category = request.forms.get('category')
     isPrivate = request.forms.get('isPrivate')
     return board.updateBoard(id,boardName, boardDesc, category, isPrivate)
 

# Delete a board
@route('/users/<UserId>/boards/<boardName>/', method='DELETE')
def deleteBoard(userId, boardName):
    print '--> Delete Board: ',boardName
    return board.deleteBoard(userId, boardName)


def __format(request):
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
      if reqfmt == Board.html:
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
