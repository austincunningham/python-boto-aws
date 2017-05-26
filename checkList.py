#!/usr/bin/python3
# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016

import subprocess
import boto.ec2
import time
import sys


def listcheck():
    #import colours class
    from run_newwebserver import colours
    colours = colours()

    print('Opening connection... ')
    conn =  boto.ec2.connect_to_region("us-west-2")
    reservations = conn.get_all_reservations()
    #reservations = conn.get_all_instances()
    time.sleep(1)
    # Checking all reserviations and instances for an instance of state pending, to find the newest connection
    # return the ip address if found
    ip = ""
    while ip == "":
        for res in reservations:
            for inst in res.instances:
                print("%s [%s] ip: %s" % (inst.id, inst.state, inst.ip_address))
                if inst.state == "pending":
                    ip = inst.ip_address
                    return ip #returns the newest open connection
        # if the above condition is not met check for running connections and return ip address for that
        # this is never run in the current version
        for res in reservations:
            for inst in res.instances:
                print("%s [%s] ip: %s" % (inst.id, inst.state, inst.ip_address))
                if inst.state == "running":
                    ip = inst.ip_address # if no new connections then use available
                    return ip



def reservationcheck():
    #search reservations and return a running instance
    conn = boto.ec2.connect_to_region("us-west-2")
    reservations = conn.get_all_reservations()
    for res in reservations:
        for inst in res.instances:
            if inst.state == "running":
                return res
            else :
                print("Error no running instances")



def sshcheck(pem, ip):
    # import the colours class
    from run_newwebserver import colours
    colours = colours()

    print (colours.YELLOW+'Checking to see if your AWS instance is accepting ssh connections, \nthis may take a while'+colours.NONE)
    #time.sleep(45)

    # better that time.sleep , progress bar
    barLength = 50
    endValue = 101
    # loop for 101
    for i in range(endValue):
        percent = int(i)/endValue # get percentage
        eq = '=' * int(round(percent * barLength)) # equals length worked on as a precentage of bar length
        space = ' ' * (barLength - len(eq))# spaces is the remainder
        sys.stdout.write(colours.GREEN)
        # format command populates what is in the {} brackets
        sys.stdout.write("\rProcessing [{0}] {1} %".format(eq + space, int(percent * endValue)))
        sys.stdout.write(colours.NONE)
        #sys.stdout.write("\r [{0}]".format(eq + space))
        # clears the buffer
        sys.stdout.flush()
        time.sleep(.5)

    print("\n")
    # ssh pole new instance and check standard out for zero , command run successful
    output = 2 # set default output value
    while output != 0:
        output = subprocess.call("ssh -o StrictHostKeyChecking=no -i ~/"+ pem +".pem ec2-user@"+ ip +" 'exit'",shell=True)
    print(colours.YELLOW+'Your AWS instance now accepts ssh connections'+colours.YELLOW)
    time.sleep(3)



