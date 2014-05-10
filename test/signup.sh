#!/bin/bash
#
# test login service

echo -e "\n"
curl -i -H "Accept: application/json" --data "firstName=chitra&lastName=soni&emailId=chitra@gmail.com&password=chitra"  http://localhost:8080/users/signup
echo -e "\n"
