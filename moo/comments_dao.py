import json
from subprocess import os
class DBConn():
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.createConn()

    def createConn(self):
        #Create new table pincomments
        uri = "/pincomments"
        request = "curl -X PUT http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()

        #Create new table comments
        uri = "/comments"
        request = "curl -X PUT http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()
        return "Success: Create DB Connection"

#create a new pin
    def createComment(self,userId, boardName, pinName, comment):
        uri = "/comments"
        data = {}
        data["comment"] = comment

        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()
        print 'response: ',response
        #res = json.loads(response)
        #lines = 
        line =  response.split()
        l_index = line.index("Location:")
        location = line[l_index+1]
        print 'Line : ' ,location
        lsplit = location.split('/')
        
        uniqueId = lsplit[-1]
        print 'unique Id: ', uniqueId

        #insert pin to userboardpins table
        #prev_pins = self.getUserBoardPins(userId, boardName)
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/pincomments/'+str(userId)+boardName+pinName
        response = os.popen(request).read()
        res = json.loads(response)
        rev = None
        prev_commentIds = None
        if "_rev" in res.keys():
            rev = res["_rev"]
        if "commentId" in res.keys():
            prev_commentIds = res["commentId"]
        #Create new json data to be inserted for this userId and boardName to DB
        data = {}
        data["_id"] = str(userId)+boardName+pinName
        #print 'Prev boards ',prev_boards
        if prev_commentIds != None:
            commentIds = prev_commentIds
            commentIds.append(uniqueId)   
        else:
            commentIds = [uniqueId]
        data["commentId"] = commentIds
        #Need rev number to update the record, if rev is None then it is first record
        if rev != None:
            data["_rev"] = str(rev)
        
        uri = "/pincomments"

        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri

        #Execute the DB update request
        #print 'New request is ',request
        response = os.popen(request).read()
        #print 'Response is: ', response

        #Insert Board Details in table boardDetails
        
        return uniqueId

    #returns pin list for userId and boardName
    def getUserBoardPinCommentIds(self, userId, boardName, pinName):
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/pincomments/'+str(userId)+boardName+pinName
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            return res["commentId"]
        else:
            return None
        
    def getUserBoardPinComments(self, userId, boardName, pinName):
        commentIds = self.getUserBoardPinCommentIds(userId, boardName, pinName)
        comments = []
        for commentId in commentIds:
            comment = self.getComment(commentId)
            if comment != None:
                comments.append(comment)
        return comments

    def getComment(self, commentId):
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/comments/'+commentId
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            return res
        else:
            return None
        
    def getAllComment(self, listId):
        comments = []
        for commentId in listId:
            comment = self.getComment(commentId)
            if comment != None:
                comments.append(comment)
        return comments
        

    #delete by board name from both tables user boards and board details TODO need to delete all pins for that board
    def deleteComment(self, userId, boardName, pinName,commentId):
        prev = self.getComment(commentId)
        #print ' Prev record for delete: ', prev
        rev = None
        if "_rev" in prev.keys():
            rev = prev["_rev"]
        else:
            return False
        request = 'curl -X DELETE -H "Accept: application/json" http://127.0.0.1:5984/comments/'+commentId+'?rev='+rev
        response = os.popen(request).read()
        
        #Get previous Board record for this userId from DB
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/pincomments/'+str(userId)+boardName+pinName
        response = os.popen(request).read()
        #print 'current records ',response
        res = json.loads(response)
        if res == None:
            return False
        if "_rev" in res.keys():
            rev = res.get("_rev")
        else:
            return False
        prev_commentIds = res["commentId"]
        
        commentIds = None
        #Create new json data to be inserted for this userId to DB
        data = {}
        data["_id"] = str(userId)+boardName
        #print 'Prev boards ',prev_boards
        if prev_commentIds != None:
            if commentId in prev_commentIds:
                commentIds = prev_commentIds
                commentIds.remove(commentId)       
            else:
                return False
        else:
            return False

        data["commentId"] = commentIds

        uri = "/pincomments"
        #Need rev number to update the record, if rev is None then it is first record
        if rev == None:
            return False
        data["_rev"] = str(rev)
        
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri

        #Execute the DB update request
        #print 'New request is ',request
        response = os.popen(request).read()
        #print 'Response is: ', response
        return True

    #update board details based on board name, update of board name not supported
    def updateComment(self, commentId, comment):
        data = self.getComment(commentId)
        #Insert Board Details in table boardDetails
        uri = "/comments"
        if data == None:
            return False
        rev = None
        if "_rev" in data.keys():
            rev = data["_rev"]
        else:
            return False

        data["comment"] = comment
        
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        #print 'New request is ',request
        response = os.popen(request).read()
        #print 'Response is: ', response

        return True

if __name__ == "__main__":
    dbconn = DBConn("127.0.0.1",5984)
    i = 3
    for j in range(10):
        res = dbconn.createComment(i, "board"+str(i), "pin"+str(i), "comment"+str(i))
        print 'Comment Created: ',res
        id = res
        res = dbconn.updateComment(id, "updated")
        print  'Update Comment ',res
        res = dbconn.deleteComment(i, "board"+str(i), "pin"+str(i), id)
        print 'Delete Comment ',res
    	#res = dbconn.getPinDetails(i,"board"+str(i),"pin"+str(i))
    	#print 'Pin details: ',res
    	#res = dbconn.getUserBoardPins(i, "board"+str(i))
    	#print 'Total Pins: ',res
    	
    	#res = dbconn.deleteBoard(i, "board"+str(i))
    	#print 'Delete board: ', res
    	#res = dbconn.updatePin(i,"pin"+str(i),"updated pin","image"+str(i),"board"+str(i))
    	#print 'Update Pin: ', res
        #res = dbconn.deletePin(i,"board"+str(i),"pin"+str(i))
    	#print 'Delete Pin: ',res
    res = dbconn.getUserBoardPinCommentIds(i,"board"+str(i), "pin"+str(i))
    print 'All Comment Ids ', res
    res = dbconn.getAllComment(res)
    print 'All comments: ',res

    res = dbconn.getUserBoardPinComments(i,"board"+str(i), "pin"+str(i))
    print 'All comments 2: ',res
