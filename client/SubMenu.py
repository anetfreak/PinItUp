import Requestor

def showSubMenu(resp):
    if resp != None:
        for item in resp:
            for key, value in item.iteritems():
                print key + " - \"" + value + "\""
                print ""
            
        option = raw_input("Enter choice in URL|METHOD format - ").strip()
        return option
    
def processRequest(host, port, option):
    data = None
    request = option.split("|")
    uri = request[0]
    method = request[1]
    method = method.upper()
    if method == 'POST':
        resp = Requestor.httpPostRequest(host, port, data, uri)
    elif method == 'GET':
        resp = Requestor.httpGetRequest(host, port, uri)
    