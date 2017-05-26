# ReadMe

This is a project that uses Python 3.4/5 and the boto libary to start/stop Amazon Web Services(AWS) instances. There are also scripts that start services on remote instance.

## Pre-requistes

To get started, you will need to have the following requirements setup

- python 3 or greater
- bash
- ssh/scp installed and allowed access to the internet on port 22
- An AWS account with RSA public/private key setup see http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html for more information
- It is required that a copy of your pem file is save in the root of your ~/ home directory
- You will need your boto libary configured to interact with AWS see http://boto3.readthedocs.io/en/latest/guide/configuration.html for more information

# Starting the App
- extract the zipped folder and cd to the directory
- ./run_newwebserver.py

# Expected output
````
Add the pem file

____________________________________________________________ 
        _          _       _     ____               
       / \      __| |   __| |   |  _ \    ___   _ __ ___      
      / _ \    / _  |  / _  |   | |_) |  / _ \ |  _   _ \       
     / ___ \  | (_| | | (_| |   |  __/  |  __/ | | | | | |           
    /_/   \_\  \__,_|  \__,_|   |_|      \___| |_| |_| |_|           
 ____________________________________________________________ 
 ____________________________________________________________ 
Enter pem filename without extention
````
Menu
````
____________________________________________________________ 
               __  __                        
              |  \/  |   ___   _ __    _   _ 
              | |\/| |  / _ \ | '_ \  | | | |
              | |  | | |  __/ | | | | | |_| |
              |_|  |_|  \___| |_| |_|  \__,_|
 ____________________________________________________________ 
 ____________________________________________________________ 
        ______________________________________________ 
       |                                              |
       | Welcome. Please choose one of the following: |
       |                                              |
       |   1. Check Security Group                    |
       |   2. Start up AWS instance                   |
       |   3. Copy file to AWS server                 |
       |   4. Run check_webserver                     |
       |   5. Terminate the instance                  |
       |                                              |
       | Enter a Number or q to quit :                |
       |______________________________________________|

````
# Author:
Austin Cunningham
Email: austincunningham@oceanfree.net


