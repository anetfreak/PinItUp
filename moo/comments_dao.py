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
    def createPin(self,userId, boardName, pinName, comment):
        uri = "/comments"
        data = {}
        data["comment"] = comment

        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        response = os.popen(request).read()
        res = json.loads(response)
        uniqueId = res["_id"]



        #insert pin to userboardpins table
        #prev_pins = self.getUserBoardPins(userId, boardName)
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/pincomments/'+str(userId)+boardName+pinName
        response = os.popen(request).read()
        res = json.loads(response)
        rev = None
        commentIds = None
        if "_rev" in res.keys():
            rev = res["_rev"]
        if "pinName" in res.keys():
            prev_commentIds = res["commentId"]
        #Create new json data to be inserted for this userId and boardName to DB
        data = {}
        data["_id"] = str(userId)+boardName+pinName
        #print 'Prev boards ',prev_boards
        if prev_commentIds != None:
            commentIds = prev_commentIds
            commentIds.append(uniqueId)
                
        else:
            pins = [pinName]
        data["pinName"] = pins
        
        uri = "/userboardpins"
        #Need rev number to update the record, if rev is None then it is first record
        if rev == None:
            request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        else:
            data["_rev"] = str(rev)
            request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri

        #Execute the DB update request
        #print 'New request is ',request
        response = os.popen(request).read()
        #print 'Response is: ', response

        #Insert Board Details in table boardDetails
        
        return True

    #returns pin list for userId and boardName
    def getUserBoardPins(self, userId, boardName):
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/userboardpins/'+str(userId)+boardName
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            return res["pinName"]
        else:
            return None

    #get pin details based on userId and boardName
    #returns dictonary of pin details
    def getPinDetails(self, userId,boardName,pinName):
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/pindetails/'+str(userId)+boardName+pinName
        response = os.popen(request).read()
        res = json.loads(response)
        if "_id" in res.keys():
            return res
        return None
        

    #delete by board name from both tables user boards and board details TODO need to delete all pins for that board
    def deletePin(self, userId, boardName, pinName):
        prev = self.getPinDetails(userId,boardName, pinName)
        #print ' Prev record for delete: ', prev
        rev = None
        if "_rev" in prev.keys():
            rev = prev["_rev"]
        else:
            return False
        request = 'curl -X DELETE -H "Accept: application/json" http://127.0.0.1:5984/pindetails/'+str(userId)+boardName+pinName+'?rev='+rev
        response = os.popen(request).read()
        
        #Get previous Board record for this userId from DB
        request = 'curl -X GET -H "Accept: application/json" http://127.0.0.1:5984/userboardpins/'+str(userId)+boardName
        response = os.popen(request).read()
        #print 'current records ',response
        res = json.loads(response)
        if res == None:
            return False
        if "_rev" in res.keys():
            rev = res.get("_rev")
        else:
            return False
        prev_pins = res["pinName"]
        

        #Create new json data to be inserted for this userId to DB
        data = {}
        data["_id"] = str(userId)+boardName
        #print 'Prev boards ',prev_boards
        if prev_pins != None:
            if pinName in prev_pins:
                pins = prev_pins
                pins.remove(pinName)       
            else:
                return False
        else:
            return False

        data["pinName"] = pins

        uri = "/userboardpins"
        #Need rev number to update the record, if rev is None then it is first record
        if rev == None:
            return False
        else:
            data["_rev"] = str(rev)
            request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri

        #Execute the DB update request
        #print 'New request is ',request
        response = os.popen(request).read()
        #print 'Response is: ', response
        return True

    #update board details based on board name, update of board name not supported
    def updatePin(self,userId, pinName, pinDesc, image, boardName):
        data = self.getPinDetails(userId,boardName,pinName)
        #Insert Board Details in table boardDetails
        uri = "/pindetails"
        if data == None:
            return False
        rev = None
        if "_rev" in data.keys():
            rev = data["_rev"]
        else:
            return False

        data["pinDesc"] = pinDesc
        data["image"] = image
        request = "curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' --data '" +json.dumps(data)+ "' http://" + self.host + ":" + str(self.port) + uri
        #print 'New request is ',request
        response = os.popen(request).read()
        #print 'Response is: ', response

        return True

if __name__ == "__main__":
    dbconn = DBConn("127.0.0.1",5984)

    for i in range(10):
        res = dbconn.createPin(i,"pin"+str(i),"my pin","image"+str(i),"board"+str(i))
        print 'Pin Created: ',res
    	res = dbconn.getPinDetails(i,"board"+str(i),"pin"+str(i))
    	print 'Pin details: ',res
    	res = dbconn.getUserBoardPins(i, "board"+str(i))
    	print 'Total Pins: ',res
    	
    	#res = dbconn.deleteBoard(i, "board"+str(i))
    	#print 'Delete board: ', res
    	res = dbconn.updatePin(i,"pin"+str(i),"updated pin","image"+str(i),"board"+str(i))
    	print 'Update Pin: ', res
        res = dbconn.deletePin(i,"board"+str(i),"pin"+str(i))
    	print 'Delete Pin: ',res

