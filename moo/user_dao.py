import json
from subprocess import os
class DBConn():
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.createConn()

    def createConn(self):
        #Create new table userboards
        uri = "/users"
        request = "curl -X PUT http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()



    def userSignUp(self, fname, lname, email, pwd):
        #Check if userId already exists, return user already exists
        uri = "/users"
        #request = "curl -X GET -H 'Accept: application/json' http://" + self.host + ":" + str(self.port) + uri+ "/"+email
        #response = os.popen(request).read()

        res = self.getUser(email)
        #Checking if user already exists
        if res != None:
            print 'current records ',res
            return "Failed: User already Exists" 
     
        user = {}
        user["_id"] = email
        user["fname"] = fname
        user["lname"] = lname
        user["pwd"] = pwd      
	request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(user)+ "' http://" + self.host + ":" + str(self.port) + uri

        response = os.popen(request).read()
        return "Success: User Created"


    def getUser(self,email):
        uri = "/users"
        request = "curl -X GET -H 'Accept: application/json' http://" + self.host + ":" + str(self.port) + uri+ "/"+email
        #print request
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            return res
        return None

    def userSignIn(self,email,pwd):
        res = self.getUser(email)
        if res != None:
            if res["pwd"] == pwd:
                return True
        return False
    
    def updateUser(self,fname,lname,email,pwd):
        res = self.getUser(email)
        if res == None:
            return False
        res["fname"] = fname
        res["lname"] = lname
        res["pwd"] = pwd
        #rev = res["_rev"]
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(user)+ "' http://" + self.host + ":" + str(self.port) + uri

        response = os.popen(request).read()
        return True

if __name__ == "__main__":
    dbconn = DBConn("127.0.0.1",5984)
    #dbconn.createConn()
    res = dbconn.userSignUp("Amit","Agrawal","abc2@gmail.com","pwd1234")
    print 'result ', res
    res = dbconn.getUser("abc2@gmail.com")
    print 'result ', res
    res = dbconn.userSignIn("abc4@gmail.com","pw1234")
    print 'User Login ', res

