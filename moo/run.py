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
  
  run(host='192.168.0.28', port=8888)
else:
  print "usage:", sys.argv[0],"[base_dir] [conf file]"

