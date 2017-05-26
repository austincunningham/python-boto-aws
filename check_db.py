#!/usr/bin/python3
# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016


import subprocess
#subprocess.call runs OS commands
# list all processes, search for mysql but exclude the grep in the response
output = subprocess.call('ps -A | grep mysql | grep -v grep', shell=True)
# 0 is a successfull response from the command and has found a the mysql process running
if output == 1 or output == 2:
    print ("MYSQL NOT RUNNING")
    print ("Do you want to start MySQL? y/n")
    output = input(":>")
    if output == 'y' or output == 'Y':
        # install mysql server and start services if prompted
        subprocess.call('sudo yum -y install mysql-server', shell=True)
        subprocess.call('sudo service mysqld start', shell=True)
        output2 = subprocess.call('ps -A | grep mysql | grep -v grep', shell=True)
        if output2 == 0:
            print("NOW STARTING MySQL SERVICE")
else:
    print ("MYSQL RUNNING")
