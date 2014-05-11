#!/bin/bash
#
# test login service

echo -e "\n"
curl -i -H "Accept: application/json" --data "username=admin&password=admin"  http://localhost:8080/users/login
echo -e "\n"
