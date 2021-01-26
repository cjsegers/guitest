#!/usr/bin/env python3
import paramiko
import sys

def checkForGUI(host,user,passwd):
    e_code = None   #exit code
    diagnostic = None
    ssh_client.connect(hostname=host, username=user, password=passwd)
    stdin,stdout,stder = ssh_client.exec_command("ps ax --forest | grep 'gdm\|lightdm\|sddm'")
    output = stdout.readlines()
    if "/usr/sbin/gdm" in str(output[0]):
        diagnostic = "GUI is running"
        e_code = 2      #exit code 2 because this script is for situations where we *don't* want the GUI running
    elif "/usr/sbin/lightdm" in str(output[0]):
        diagnostic = "GUI is running"
        e_code = 2      #exit code 2 because this script is for situations where we *don't* want the GUI running
    elif "/usr/sbin/sddm" in str(output[0]):
        diagnostic = "GUI is running"
        e_code = 2      #exit code 2 because this script is for situations where we *don't* want the GUI running
    else:
        diagnostic = "GUI is not running"
        e_code = 0
    return e_code, diagnostic
 
    
if len(sys.argv) == 1:
	print("\tUsage: python3 guitest.py <targetip> <targetuser> <targetpass>")
	sys.exit(3)
host_name = sys.argv[1] 	#"172.19.250.3"
user_name = sys.argv[2] 	#"sshtest"
pass_word = sys.argv[3] 	#"----"

diagnostic_message = None   # Describes success or failure
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # if the server is not in known_hosts, add it and proceed
exit_code = None
     
try:
    exit_code, diagnostic_message = checkForGUI(host_name,user_name,pass_word)
 
except Exception as e:
    diagnostic_message = e
    exit_code = 2

print("Exit code is {}. {}".format(exit_code,diagnostic_message)) 
sys.exit(exit_code)