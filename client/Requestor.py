from subprocess import os
import json
import httplib
import re

def makeRequest(uri, host, port, data):
    if (data == None):
        request = "curl -i -H 'Accept: application/json' http://" + host + ":" + str(port) + uri
    else:
        request = "curl -i -H 'Accept: application/json' --data '" +data+ "'  http://" + host + ":" + str(port) + uri
    response = os.popen(request).read()
    return json.dumps(response)


def httpPostRequest(host, port, data, uri):
    conn = httplib.HTTPConnection(host + ":" + port)
    conn.request("POST", uri, data)
    r1 = conn.getresponse()
    data = r1.read()
    data = data.replace("\'", "\"")
    jsonResp = json.loads(data)

def httpGetRequest(host, port, data, uri):
    conn = httplib.HTTPConnection(host + ":" + port)
    conn.request("GET", uri)
    r1 = conn.getresponse()
    data = r1.read()
    data = data.replace("\'", "\"")
    jsonResp = json.loads(data)