#!/usr/bin/python3
# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016
# -*- coding: utf-8 -*-

import subprocess
import sys
import security
import startStop
import Scripts
import checkList
import boto.ec2
import time


# menu function loops until user types q or Q
def menu(cp):
    case = True
    while case:
        subprocess.call('./menu', shell=True)
        case = input(":>")
        if case == '1':
            cp.securityName = security.securitycheck(cp.conn)

        elif case == '2':
            # checks to see if there is a security group
            if cp.securityName == None:
                print(colours.RED +"No security group present please select option 1 and enter one"+colours.NONE)
                time.sleep(3)
            else:
                cp.ip = startStop.run_instance(cp.pem, cp.conn, cp.securityName)

        elif case == '3':
            # Checks to see if the ip address exists
            if cp.ip == None:
                print(colours.RED +"No AWS instance running please select option 2 and create one"+colours.NONE)
                print(colours.RED +"You will also need a security group setup select option 1 to add one"+ colours.NONE)
                time.sleep(3)
            else:
                cp.filename = Scripts.uploadScript(cp.pem, cp.ip)

        elif case == ('4'):
            # checks to see if the ip exists and file has been uploaded
            if cp.ip == None:
                print(colours.RED +"No AWS instance running please select option 2 and create one"+colours.NONE)
                print(colours.RED +"You will also need a security group setup select option 1 to add one"+ colours.NONE)
            elif cp.filename == None:
                print(colours.RED + "No file uploaded plesase select option 3 to upload one")
            else:
                Scripts.runScript(cp.pem, cp.ip, cp.filename)
            time.sleep(3)
        elif case == '5':
            # checks to see if AWS ip address exists
            if cp.ip == None:
                print(colours.RED +"No AWS instance running please select option 2 and create one"+colours.NONE)
                print(colours.RED +"You will also need a security group setup select option 1 to add one"+ colours.NONE)
            else:
                Scripts.checkserverstats(cp.pem, cp.ip)
            time.sleep(3)
        elif case == '6':
            cp.res = checkList.reservationcheck()
            startStop.stopTerminate_instance(cp.res)
        elif case == 'q' or case == 'Q':
            print(colours.YELLOW +"goodbye"+ colours.NONE)
            break
        else:
            # catchall if not 1-6 or q,Q reload menu
            print (colours.RED +"Invalid selection try again"+ colours.NONE)
            time.sleep(3)

# class to contain all infomation about the connection
class connectionPem:
    def __init__(self, conn, pem, ip, res, securityName, filename):
        self.conn = conn
        self.pem = pem
        self.ip = ip
        self.res = res
        self.securityName = securityName
        self.filename = filename

# ANSI escape characters
class colours:
    NONE = '\033[00m'
    RED = '\033[01;31m'
    GREEN = '\033[01;32m'
    YELLOW = '\033[01;33m'
    BLUE = '\033[01;34m'
    PURPLE = '\033[01;35m'
    CYAN = '\033[01;36m'
    WHITE = '\033[01;37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Askes user to input there pem file
def inputPem():
    conn = boto.ec2.connect_to_region('us-west-2')
    ip = None
    res = None
    securityName = None
    filename = None
    pem = None
    # populates connectionPem class
    cp = connectionPem(conn, pem, ip, res, securityName, filename)
    subprocess.call("./pem")
    output = 1
    while output != 0 :
        print("\nEnter pem filename without extention")
             cp.pem = input(">:")
        output = subprocess.call("test -f ~/" + cp.pem + ".pem", shell=True)
        if output != 0:
            print(colours.RED +"Pem file " + cp.pem + ".pem not found in your home directory,\ncheck the to see if the file exists and try again"+ colours.NONE)
            time.sleep(3)
            print(colours.RED+ "If you wish to exit program ? y/n"+ colours.NONE)
            y = input(":>")
            if y == "y" or y == "Y":
                sys.exit("user exit")
    print(colours.YELLOW +"File " + cp.pem + ".pem found"+ colours.NONE)
    time.sleep(3)
    return cp


def main():
    cp = inputPem()
    menu(cp)

if __name__ == '__main__':
    main()
