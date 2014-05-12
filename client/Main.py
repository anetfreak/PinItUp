import sys
import Requestor
sys.path.append('/usr/lib')

if __name__ == '__main__':
    
    username = None
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
            print "3. Logout"
        else:
            print "1. Login to PinItUp"
            print "2. SignUp with PinItUp"
        print "99. Quit"
      
        choice = int(raw_input("\nYour Option -> "))
        if choice == 1:
            #Login to PinItUp
            username = raw_input("Username: ").strip()
            password = raw_input("Password: ").strip()
            status = Requestor.httpPostRequest(host, port,"username="+username+"&password="+password , "/users/login/")
            if status:
                authenticated = True
            else:
                username = None    
        elif choice == 2:
            #Signup with PinItUp
            username = raw_input("Username: ").strip()
            password = raw_input("Password: ").strip()
        elif choice == 3:
            #Logout
            status = Requestor.httpGetRequest(host, port, "/users/" + username + "/logout/")
            if status:
                authenticated = False
                username = None
        elif choice == 99:
            print "Bye!"
            running = False
        else:
            print "Please choose a valid option. -> "