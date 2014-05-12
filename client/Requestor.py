# from subprocess import os
import sys
import json
import httplib

# def makeRequest(uri, host, port, data):
#     if (data == None):
#         request = "curl -i -H 'Accept: application/json' http://" + host + ":" + str(port) + uri
#     else:
#         request = "curl -i -H 'Accept: application/json' --data '" +data+ "'  http://" + host + ":" + str(port) + uri
#     response = os.popen(request).read()
#     return json.dumps(response)


def httpRequest(host, port, body, uri, method):
    conn = httplib.HTTPConnection(host + ":" + port)
    if method == 'POST' or method == 'PUT':
        conn.request(method, uri, body)
    else:
        conn.request(method, uri)
    r1 = conn.getresponse()
    if r1.status == 200 or r1.status == 201:
        try:
            data = r1.read()
            data = data.replace("\'", "\"")
            jsonResp = json.loads(data)
            print "\nSuccess!"
            print "URL's that you can navigate next to -> "
            for item in jsonResp:
                for key, value in item.iteritems():
                    print key + " - \"" + value + "\""
                print ""
            return True
        except:
            print "\nFailure"
            print sys.exc_info()[0]
            return False
    else:
        print "\nFailure"
        print "Error occurred with status code " + str(r1.status)
        return False
    conn.close()