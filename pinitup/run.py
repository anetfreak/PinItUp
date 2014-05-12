#
# start the server
#

import sys

from bottle import run
from moo import setup 
from board import boardsetup
from userController import usersetup

if len(sys.argv) > 2:
  base = sys.argv[1]
  conf_fn = sys.argv[2]
  #setup(base,conf_fn)
  boardsetup(base,conf_fn)
  usersetup(base,conf_fn)
  
  run(host='127.0.0.1', port=8080)
else:
  print "usage:", sys.argv[0],"[base_dir] [conf file]"

