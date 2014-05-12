#!/bin/bash
#
# Run our web service
#

# working direct to set the path to our modules (not 
# the most efficient but it works)
export PIN_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}/"/)" && cd .. && pwd )"

echo -e "\n** starting service from $PIN_HOME **\n"

# configuration
export PYTHONPATH=${PIN_HOME}/moo:${PYTHONPATH}

# run
#python ${PIN_HOME}/pinitup/moo.py ${PIN_HOME} ${PIN_HOME}/conf/moo.conf
python ${PIN_HOME}/pinitup/run.py ${PIN_HOME} ${PIN_HOME}/conf/moo.conf
