# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016

import checkList
import time
import subprocess


def run_instance(pem,conn,securityName):
    # import the colours class
    from run_newwebserver import colours
    colours = colours()
    subprocess.call("./startaws", shell=True)
    #create	the	instance.You use the run_instances() method	to launch an instance
    reservation = conn.run_instances('ami-7172b611',key_name = pem,instance_type ='t2.micro',security_groups=[securityName])
    instance = reservation.instances[0]
    #print("ip address :",instance.ip_address)
    instance.add_tag('Austin', 'nginx-check')
    # List connections
    # check for pending ip address and return
    ip = checkList.listcheck()
    print(colours.YELLOW+"Starting : " + colours.GREEN +""+ ip +""+colours.NONE)
    time.sleep(2)
    # run to test ssh connection
    checkList.sshcheck(pem, ip)
    return ip


def stopTerminate_instance(res):
    # stop instance and terminate if not exist send error message.
    subprocess.call("./stopaws", shell=True)
    if res == None:
        print("No instances running returning to menu")
        time.sleep(2)
        return
    instance = res.instances[0]
    instance.update()
    print("Do you wish to stop instance of ip address " + instance.ip_address +" and terminate instance ? y/n")
    stop = input (":>")
    if stop == "y" or stop == "Y":
        instance.stop()
        instance.terminate()
        print("instancse stopped")
        time.sleep(2)
    else:
        print("GoodBye")
