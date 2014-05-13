import json
from subprocess import os
class DBConn():
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.createConn()

    def createConn(self):
        #Create new table sessions
        uri = "/sessions"
        request = "curl -X PUT http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()


# Add a session
    def addSession(self, userId):
        uri = "/sessions"
        session = {}
        session["_id"] = userId
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(session)+ "' http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()
        return True

#Delete a session
    def deleteSession(self,userId):
        uri = "/sessions"   
        request = "curl -i -H 'Accept: application/json' http://" + self.host + ":" + str(self.port) + uri + "/" + userId
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            rev = res["_rev"]
        else:
            return False
        
        request = "curl -X DELETE -H 'Accept: application/json' http://" + self.host + ":" + str(self.port) + uri + "/" + userId + "?rev=" + rev
        response = os.popen(request).read()
        
#Check is Session Exists
    def isSessionExists(self, userId):
        uri = "/sessions"   
        request = "curl -i -H 'Accept: application/json' http://" + self.host + ":" + str(self.port) + uri + "/" + userId
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            return True
        else:
            return False        
        