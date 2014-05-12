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
        prev_boards = None     #is a list of boards
        rev = None             #is a _rev returned in query
        if "_rev" in res.keys():
            rev = res.get("_rev")
        if "boardName" in res.keys():
            prev_boards = res["boardName"]
        

        #Create new json data to be inserted for this userId to DB
        data = {}
        data["_id"] = str(userId)
        #print 'Prev boards ',prev_boards
        if prev_boards != None:
            if boardName in prev_boards:
                return "Failed: Record Already Exists"
            else:
                print 'I am here'
                boards = prev_boards
                boards.append(boardName)
                
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
        data["_id"] = boardName
        data["boardDesc"] = boardDesc
        data["category"] = category
        data["isPrivate"] = isPrivate
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        print 'New request is ',request
        response = os.popen(request).read()
        print 'Response is: ', response

    #returns boards list for user Id
    def getUserBoards(self, userId):
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/userboards/'+str(userId)
        response = os.popen(request).read()
        return json.loads(response)["boardName"]

    #get board details based on board name
    #returns dictonary of board details
    def getBoardDetails(self, userId,boardName):
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/boarddetails/'+boardName
        response = os.popen(request).read()
        return json.loads(response)
        

    #delete by board name from both tables user boards and board details TODO need to delete all pins for that board
    def deleteBoard(self, userId, boardName):
        prev = self.getBoardDetails(userId,boardName)
        print ' Prev record for delete: ', prev
        rev = None
        if "_rev" in prev.keys():
            rev = prev["_rev"]
        else:
            return "Success: No record found for delete"
        request = 'curl -X DELETE -H "Accept: application/json" http://127.0.0.1:5984/boarddetails/'+boardName+'?rev='+rev
        response = os.popen(request).read()
        print 'DELETE Board: ', response
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
            if boardName in prev_boards:
                print 'I am here'
                boards = prev_boards
                boards.remove(boardName)       
            else:
                return "Success: record not there in User Boards"
        else:
            return "Success: record not there in User Boards"

        data["boardName"] = boards

        uri = "/userboards"
        #Need rev number to update the record, if rev is None then it is first record
        if rev == None:
            return "Success: record not there in User Boards"
        else:
            data["_rev"] = str(rev)
            request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri

        #Execute the DB update request
        print 'New request is ',request
        response = os.popen(request).read()
        print 'Response is: ', response

    #update board details based on board name, update of board name not supported
    def updateBoard(self,userId, boardName):
        data = self.getBoardDetails(self, userId,boardName)
        #Insert Board Details in table boardDetails
        uri = "/boarddetails"
        data = {}
        data["userId"] = userId
        data["_id"] = boardName
        data["boardDesc"] = boardDesc
        data["category"] = category
        data["isPrivate"] = isPrivate
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        print 'New request is ',request
        response = os.popen(request).read()
        print 'Response is: ', response

        return "Success: board updated"

if __name__ == "__main__":
    dbconn = DBConn("127.0.0.1",5984)
    dbconn.createBoard(1234,"board3","my private board","test",True)
    res = dbconn.getBoardDetails(1234,"board1")
    print 'Board details: ',res
    res = dbconn.getBoardDetails(1234,"board2")
    print 'Board details: ',res
    res = dbconn.getBoardDetails(1234,"board3")
    print 'Board details: ',res
    res = dbconn.deleteBoard(1234, "board1")
