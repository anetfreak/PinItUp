#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "name='foo'&value='bar'"  http://192.168.0.28:8080/moo/data
echo -e "\n"
