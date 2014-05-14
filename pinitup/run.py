#
# start the server
#

import sys

from bottle import run
from moo import setup 
from board import boardsetup
from userController import usersetup
from pincontroller import pinsetup
from commentsController import commentsetup
from SessionManager import SessionManager

if len(sys.argv) > 2:
  base = sys.argv[1]
  conf_fn = sys.argv[2]
  session = SessionManager()
  #setup(base,conf_fn)
  boardsetup(base,conf_fn, session)
  pinsetup(base,conf_fn, session)
  commentsetup(base,conf_fn, session)
  usersetup(base,conf_fn, session)
  
  run(host='127.0.0.1', port=8080)
else:
  print "usage:", sys.argv[0],"[base_dir] [conf file]"

