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


def httpPostRequest(host, port, data, uri):
    conn = httplib.HTTPConnection(host + ":" + port)
    conn.request("POST", uri, data)
    r1 = conn.getresponse()
    if r1.status == 200 or r1.status == 201:
        print "Success!"
        data = r1.read()
        data = data.replace("\'", "\"")
        jsonResp = json.loads(data)
        print""
        print "URL's that you can navigate next to -> "
        for item in jsonResp:
            for key, value in item.iteritems():
                print key + " - \"" + value + "\""
            print ""
        return True
    else:
        print "Error occurred with status code " + r1.status
        return False

def httpGetRequest(host, port, data, uri):
    conn = httplib.HTTPConnection(host + ":" + port)
    conn.request("GET", uri)
    r1 = conn.getresponse()
    data = r1.read()
    data = data.replace("\'", "\"")
    jsonResp = json.loads(data)