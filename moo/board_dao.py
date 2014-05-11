import json
from subprocess import os
class DBConn():
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.createConn()

    def createConn(self):
        #Create new table userboards
        uri = "/userboards"
        request = "curl -X PUT http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()

        #Create new table boardsDetails
        uri = "/boarddetails"
        request = "curl -X PUT http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()

    def createBoard(self,userId, boardName, boardDesc, category, isPrivate):
        #Get previous Board record for this userId from DB
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/userboards/'+str(userId)
        response = os.popen(request).read()
        print 'current records ',response
        res = json.loads(response)
        rev = res.get("_rev")
        prev_boards = res["boardName"]
        

        #Create new json data to be inserted for this userId to DB
        data = {}
        data["_id"] = str(userId)
        #print 'Prev boards ',prev_boards
        if prev_boards != None:
            print 'I am here'
            boards = prev_boards
            boards.append(boardName)      #Here append new boardname for this user, logic for checking duplicate board not impl.
        else:
            boards = [boardName]
        data["boardName"] = boards

        uri = "/userboards"
        #Need rev number to update the record, if rev is None then it is first record
        if rev == None:
            request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        else:
            data["_rev"] = str(rev)
            request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri

        #Execute the DB update request
        print 'New request is ',request
        response = os.popen(request).read()
        print 'Response is: ', response

        #Insert Board Details in table boardDetails
        uri = "/boarddetails"
        data = {}
        data["userId"] = userId
        data["boardName"] = boardName
        data["boardDesc"] = boardDesc
        data["category"] = category
        data["isPrivate"] = isPrivate
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        print 'New request is ',request
        response = os.popen(request).read()
        print 'Response is: ', response

if __name__ == "__main__":
    dbconn = DBConn("127.0.0.1",5984)
    dbconn.createBoard(1234,"board1","my private board","test",True)
