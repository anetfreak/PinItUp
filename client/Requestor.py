from subprocess import os
import json
import httplib

def makeRequest(uri, host, port, data):
    if (data == None):
        request = "curl -i -H 'Accept: application/json' http://" + host + ":" + str(port) + uri
    else:
        request = "curl -i -H 'Accept: application/json' --data '" +data+ "'  http://" + host + ":" + str(port) + uri
    response = os.popen(request).read()
    return json.dumps(response)


def httpRequest():
    conn = httplib.HTTPConnection("127.0.0.1:8080")
    conn.request("POST", "/users/login/", "username=admin&password=admin")
    r1 = conn.getresponse()
    data = r1.read()
    print data
    jsonResp = json.loads(str(data))
    print jsonResp.__getitem__(0)
#     for item in json.loads(strippedData):
#         print item