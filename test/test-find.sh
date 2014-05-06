#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" http://192.168.0.28:8080/moo/data/foo
echo -e "\n"
