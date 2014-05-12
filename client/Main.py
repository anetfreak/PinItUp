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
            email = raw_input("Email: ").strip()
            password = raw_input("Password: ").strip()
            fname = raw_input("First Name: ").strip()
            lname = raw_input("Last Name: ").strip()
            status = Requestor.httpPostRequest(host, port,"emailId="+email+"&password="+password+"&firstName="+fname+"&lastName="+lname , "/users/signup/")
            if status:
                authenticated = True
                username = email
            else:
                username = None
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