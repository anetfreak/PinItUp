import sys, random
import Requestor
sys.path.append('/usr/lib')

if __name__ == '__main__':
    
    username = None
    session = -1
    #Configure Server
    print "Enter the Server Endpoint Details: "
    host = raw_input("Enter host: ")
    port = raw_input("Enter port: ")
    #Display the menu to the user. Perform the necessary action as per his choice.. 
    running = True
    authenticated = False
    while running:
        print "\n   ====================="
        print "   Welcome to PinItUp!"
        print "   =====================\n"
        print "Choose one of the options below:"
        if authenticated:
            print "4. Logout"
        else:
            print "1. Login to PinItUp"
            print "2. SignUp with PinItUp"
        print "3. URL of choice"
        print "99. Quit"
      
        choice = int(raw_input("\nYour Option -> "))
        if choice == 1:
            #Login to PinItUp
            username = raw_input("Username: ").strip()
            password = raw_input("Password: ").strip()
            uri = raw_input("URI: ").strip()
            status = Requestor.httpRequest(host, port,"username="+username+"&password="+password , uri, "POST")
            if status:
                session = random.randint(1, 10000)
                authenticated = True
            else:
                username = None    
        elif choice == 2:
            #Signup with PinItUp
            email = raw_input("Email: ").strip()
            password = raw_input("Password: ").strip()
            fname = raw_input("First Name: ").strip()
            lname = raw_input("Last Name: ").strip()
            uri = raw_input("URI: ").strip()
            json = raw_input("JSON Format(y/n): ").strip()
            json = json.lower()
            if json == 'n':
                data = "emailId="+email+"&password="+password+"&firstName="+fname+"&lastName="+lname
            else:
                data = {}
                data["emailId"] = email
                data["password"] = password
                data["firstName"] = fname
                data["lastName"] = lname
            
            print data
            status = Requestor.httpRequest(host, port, data , uri, "POST")
            if status:
                authenticated = True
                username = email
            else:
                username = None
        elif choice == 4:
            #Logout
            status = Requestor.httpRequest(host, port, None, "/users/" + username + "/logout/", "GET")
            if status:
                session = -1
                authenticated = False
                username = None
        elif choice == 3:
            #Custom URL flow
            if session > 0:
                option = raw_input("Enter choice in URL|METHOD format - ").strip()
                data = None
                request = option.split("|")
                uri = request[0]
                method = request[1]
                method = method.upper()
                if method == 'POST' or method == 'PUT':
                    data = Requestor.formRequest(uri, method)
                    status = Requestor.httpRequest(host, port, data, uri, method)
                elif method == 'GET' or method == 'DELETE':
                    status = Requestor.httpRequest(host, port, None, uri, method)
                
                if status:
                    print "Success!"
                else:
                    print "Failure"
            else:
                print "Need to login first to proceed"
        elif choice == 99:
            print "Bye!"
            running = False
        else:
            print "Please choose a valid option. -> "