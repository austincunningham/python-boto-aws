# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016

import subprocess
import time

# Start by connecting to a particular EC2 region. For Oregon
# the following will do it:
def securitycheck(conn):
    # import the colours class
    from run_newwebserver import colours
    colours = colours()
    subprocess.call("clear", shell=True)
    subprocess.call("./security", shell=True)
    output = 1
    # will loop until user exits or enters a valid security group
    while output != 0:
        print(colours.RED +"Do you wish to create a new security group? "+colours.NONE)
        create = input("y/n :")

        if create == 'y' or create == 'Y':
            #redirect to the create new security group script
            securityName = security(conn)
            return securityName
        # get all securtiy groups
        rs = conn.get_all_security_groups()
        # if rs is not greater that one only default security group exists
        if len(rs) == 1:
            print(colours.RED +"\nNo security group present, except default, \nyou will need an a security group that allows ssh "+colours.NONE)
            time.sleep(4)
            # create new security group
            securityName =security(conn)
            return securityName
        else:
            print(colours.RED +"\nSecurity Group required to continue, "
                  "\nbelow are the list of current security groups "
                  "\nSelect a group that has ssh access to continue"
                  "\nAny groups created in this script will have ssh access")
            #list all security groups except default and prompt user to enter one
            print("_______________________________________________________________________________\n")
            for name in rs:
                if name.name != "default":
                    print(colours.YELLOW+ ""+name.name+""+colours.RED)
            print("\n_______________________________________________________________________________")
            print("Enter the security group name"+colours.NONE)
            securityName = input(":>")
            # check to see if the entered security group exists return to run_newwebserver.menu if exists
            for name in rs:
                if name.name == securityName:
                    return securityName
            # if group entered doesn't exist prompt user
            print (colours.RED +"Error no matching security group found ")
            time.sleep(2)
            print ("Do you wish to try again y/n"+colours.NONE)
            again = input(":>")
            # if not y then return to run_newwebserver.menu
            if again == "y" or again == "Y":
                output = 1
            else:
                return

def security(conn):
    # import the colours class
    from run_newwebserver import colours
    colours = colours()
    subprocess.call("./security", shell=True)
    # find all security groups
    # if the lengtt of all security groups is greater that one then there is more than the default group present
    # create security group for http and ssh
    # Note that ‘0.0.0.0/0’ indicates authorization of traffic from any IP address

    print(colours.RED+"Enter security group name"+colours.NONE)
    securityName = input(":>")
    secgroup = conn.create_security_group(securityName, 'Only HTTP and SSH')
    secgroup.authorize('tcp', 80, 80, '0.0.0.0/0')  # HTTP
    secgroup.authorize('tcp', 22, 22, '0.0.0.0/0')  # SSH

    print (colours.RED+"security group created "+securityName+""+colours.NONE)
    time.sleep(2)
    return securityName
