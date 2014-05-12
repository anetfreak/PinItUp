import sys
import Requestor
sys.path.append('/usr/lib')

if __name__ == '__main__':
    
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
        print "1. Login to PinItUp"
        print "2. SignUp with PinItUp"
        if (authenticated):
            print "3. Pins"
            print "4. Boards"
        print "99. Quit"
      
        choice = int(raw_input("\nYour Option -> "))
        if choice == 1:
            #Login to PinItUp
            username = raw_input("Username: ").strip()
            password = raw_input("Password: ").strip()
            Requestor.httpPostRequest(host, port,"username="+username+"&password="+password , "/users/login/")
            authenticated = True
        elif choice == 2:
            #Signup with PinItUp
            print "Sign up functionality coming soon.."
        elif choice == 3:
            #Handling Pin functionality here
            pinMenu = True
            while pinMenu:
                print "Choose one of the following Pin operations: "
                print "a. Create a new Pin"
                print "b. View all Pins"
                print "c. Modify a Pin"
                print "d. Delete a Pin"
                print "e. Go Back"
                menuItem = raw_input("\nYour Option -> ")
                if menuItem == "a":
                    #Create Pin
                    print "Pin created.."
                elif menuItem == "b":
                    #Create Pin
                    print "All pins.."
                elif menuItem == "c":
                    #Create Pin
                    print "Pin modified.."
                elif menuItem == "d":
                    #Create Pin
                    print "Pin deleted.."
                elif menuItem == "e":
                    pinMenu = False
            
        elif choice == 4:
            #Handling Pin functionality here
            boardMenu = True
            while boardMenu:
                print "Choose one of the following Board operations: "
                print "a. Create a new Board"
                print "b. View all Boards"
                print "c. Modify a Board"
                print "d. Delete a Board"
                print "e. Go Back"
                menuItem = raw_input("\nYour Option -> ")
                if menuItem == 'a':
                    #Create Board
                    print "Board created.."
                elif menuItem == 'b':
                    #View all Boards
                    print "All boards.."
                elif menuItem == 'c':
                    #Modify Board
                    print "Board modified.."
                elif menuItem == 'd':
                    #Delete Board
                    print "Board deleted.."
                elif menuItem == 'e':
                    boardMenu = False
        elif choice == 99:
            print "Bye!"
            running = False
        else:
            print "Please choose a valid option. -> "