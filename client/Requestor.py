# from subprocess import os
import sys
import json
import httplib

# 
# Method to call Curl commands via code..
#
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
        #try:
        if True == True:
            data = r1.read()
            data = data.replace("\'", "\"")
            data = data.replace("u\"", "\"")
            #data = '{"board":["board1","board2"]}'
            print 'Data is ', data
            jsonResp = json.loads(data) #Handle exception for this line..
            print jsonResp
            print "\nSuccess!"
            
            for item in jsonResp:
                item = item.lower()
                if item == "links":
                    print "URL's that you can navigate next to -> "
                    link = jsonResp[item]
                    for l in link:
                        for key, value in l.iteritems():
                            if key != None and value != None:
                                print key + " - \"" + value + "\""
                        print ""
                if item == "boards" or item == "pins" or item == "comments":
                    print item + " that user has -> "
                    boards = jsonResp[item]
                    for b in boards:
                        for key, value in b.iteritems():
                            if key != None and value != None:
                                print key + " - " + value
                        print ""
                if item == "board" or item == "pin" or item == "comment":
                    #print "Boards that user has -> "
                    boards = jsonResp[item]
                    templinks = None
                    print "Single " + item + " -> "
                    for key, value in boards.iteritems():
                        if key != None and value != None:
                            if key == "links":
                                templinks = value
                            else:
                                print key + " - " + value
                    print ""
                    print "URL's that you can navigate next to -> "
                    if templinks != None:
                        for links in templinks:
                            for lk, lv in links.iteritems():
                                if lk != None and lv != None:
                                    print lk + " - " + lv
                            print ""
            return True
        #except:
        else:
            print "\nFailure"
            print sys.exc_info()[0]
            return False
    else:
        print "\nFailure"
        print "Error occurred with status code " + str(r1.status)
        return False
    conn.close()
    
def formRequest(uri, method):
    if method == 'POST' or method == 'PUT':
        if uri.find("/boards/") != -1 and uri.find("/pins/") != -1:
            #Pin Flow
            print "Pin Post/ Put requests"
            name = raw_input("Pin Name: ").strip()
            desc = raw_input("Pin Desc: ").strip()
            image = raw_input("Image: ").strip()
            data = "pinName=" + name + "&description="+ desc + "&image=" + image
            return data
        elif uri.find("/boards/") != -1 and uri.find("/comment/") != -1:
            #Comments Flow
            print "Comment Post/ Put requests"
            desc = raw_input("Comment: ").strip()
            data = "description="+ desc
            return data
        elif uri.find("/boards/") != -1:
            #Boards Flow
            print "Boards Post/Put request received"
            name = raw_input("Board Name: ").strip()
            desc = raw_input("Board Desc: ").strip()
            category = raw_input("Category: ").strip()
            isPrivate = raw_input("private?: ").strip()
            data = "boardName=" + name + "&boardDesc="+ desc + "&category=" + category + "&isPrivate=" + isPrivate
            return data
    
