#!/usr/bin/python3
# Author: Austin Cunningham
# Student Number: 20073379
# Version: 22/10/2016

import subprocess
# list all processes, search for nginx process but exclude the grep in the response
output = subprocess.call('ps -A | grep nginx | grep -v grep', shell=True)
if output != 0:
    print ("NOT RUNNING")
    #start nginx service if not running
    subprocess.call('sudo service nginx start', shell=True)
    print ("NOW STARTING NGINX SERVICE")
else:
    print ("RUNNING")


