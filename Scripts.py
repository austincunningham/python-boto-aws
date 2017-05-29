# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016

import subprocess
import time

def uploadScript(pem,ip):
    #import the colours class
    from run_newwebserver import colours
    colours = colours()
    #load banner
    subprocess.call("./copyscript", shell=True)
    #display menu
    print("\n"+colours.CYAN+" ________________________________________________________ ")
    print("|                                                        |")
    print("|     "+colours.GREEN+"        1. Upload check_webserver.py    "+colours.CYAN+"           |")
    print("|     "+colours.GREEN+"        2. Upload check_db.py            "+colours.CYAN+"          |")
    print("|________________________________________________________|\n"+colours.NONE)
    # assign filename a value depending on number entered
    case = True
    while case:
        case = input(":>")
        if case == '1':
            filename = 'check_webserver.py'
            break
        elif case == '2':
            filename = 'check_db.py'
            break
    #secure copy filename to home directory of instance
    subprocess.call("scp -i ~/" + pem + ".pem "+filename+" ec2-user@" + ip + ":~/", shell=True)
    #check to see if the file copied
    output = subprocess.call("ssh -i ~/" + pem + ".pem ec2-user@" + ip + " 'ls -A | grep "+filename+"'", shell=True)
    if output == 0:
        #print success message and change premissions on the file
        print(colours.YELLOW + "file "+filename+" uploaded" + colours.NONE)
        output2 = subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip + " 'chmod 700 "+filename+"'", shell=True)
        if output2 == 0:
            print(colours.YELLOW + "script "+filename+" is now executable" + colours.NONE)
            time.sleep(3)
            return filename
    else:
        print(colours.RED + "Error in upload" + colours.NONE)




def runScript(pem,ip, filename):
    #import the colours class
    from run_newwebserver import colours
    colours = colours()
    #load the banner
    subprocess.call("./runscript", shell=True)
    print(colours.YELLOW +"The following , update server time, install nginx ,\ninstall python35 and run the script "+filename+""+colours.NONE)
    # run an update command to check the network time at ntp.ubuntu.com
    output = subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip + " 'sudo ntpdate ntp.ubuntu.com'", shell=True)
    if output == 0:
        print (colours.YELLOW+'server time updated'+colours.NONE)
    # install nginx
    output = subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip + " 'sudo yum -y install nginx'", shell=True)
    print (output)
    if output == 0:
        print (colours.YELLOW+'nginx server started'+colours.NONE)
    # install python 3.5
    output = subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip + " 'sudo yum -y install python35'", shell=True)
    if output == 0:
        print (colours.YELLOW+'python 3.5 installed'+colours.NONE)
    # run the uploaded file
    output = subprocess.call("ssh -i ~/" + pem + ".pem ec2-user@" + ip + " '~/"+filename+"'", shell=True)
    # check for success/failure of attempted run
    if output != 0:
        print (colours.RED+"The file "+filename+" was not found, you need to run option 3 from the menu"+colours.NONE)
        time.sleep(3)
    else:
        print(colours.YELLOW + ""+filename+" has been found and run" + colours.NONE)
        time.sleep(3)


def checkserverstats(pem, ip):
    #import the colours class
    from run_newwebserver import colours
    colours = colours()
    print(colours.YELLOW +"CPU usage resources : " + colours.GREEN)
    # check AWS instance CPU usage using top
    subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip +" 'top -n 1 -b | grep Cpu'", shell=True)
    print(colours.YELLOW +"Checking PORT 80 need for nginx to work as a web server :"+ colours.GREEN)
    # check port 80 to see what is running on it
    subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip +" 'sudo netstat -tulpn | grep 80'", shell=True)
    print(colours.YELLOW +"Process count :"+ colours.GREEN)
    # check out the number of process that are running on AWS instance using word count of a ps command
    subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip + " 'ps -Al |  wc -l'", shell=True)
    print(colours.YELLOW +"Checking MEMORY :"+ colours.GREEN)
    # check memory usage using vmstat command
    subprocess.call("ssh -t -i ~/" + pem + ".pem ec2-user@" + ip + " 'vmstat 1 1'", shell=True)
    time.sleep(5)
    print(colours.NONE)

