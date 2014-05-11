from subprocess import os

def makeRequest(uri, host, port, data):
    if (data == None):
        request = "curl -i -H 'Accept: application/json' http://" + host + ":" + str(port) + uri
    else:
        request = "curl -i -H 'Accept: application/json' --data '" +data+ "'  http://" + host + ":" + str(port) + uri
    response = os.popen(request).read()
    return response