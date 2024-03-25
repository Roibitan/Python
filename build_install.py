#!/bin/pythonX
import os
import datetime, time
from shutil import copyfile
import argparse
from subprocess import call
import logging
import subprocess
import sys
import datetime, time
import shutil
import json
from pprint import pprint
import socket
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from distutils.dir_util import copy_tree
import traceback
import re


ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
parser = argparse.ArgumentParser(description='')
parser.add_argument('-env','--env', help='Environment: XXX, XXX_QA, XXX_QA_LIKE,XXX_PROD', required=True)
parser.add_argument('-Buildnum','--Buildnum', help='Buildnumber: vXX5_X0XX09XX.X ', required=True)
args = parser.parse_args()
hostname = socket.gethostname()

dEnv = {"XXXXXX_PROD" : {"env" : "XX.X.X.XX", "url" : "http://XX.X.X.XX:XXXX/api/ws_testDeploy?token=ProdToken", "database" : "Prod"},
        "XXXXXX_DRP" : {"env" : "XX.X.X.XXX", "url" : "http://XX.X.X.XXX:XXXX/api/ws_testDeploy?token=ProdToken", "database" : "Prod"},
        "XXXXXX_QA" : {"env" : "XX.XX.XX.XXX", "url" : "http://XX.XX.XX.XXX:XXXX/api/ws_testDeploy?token=DevToken", "database" : "QA"},
        "XXXXXX_QA_LIKE" : {"env" : "XX.XX.XX.XXX", "url" : "http://XX.XX.XX.XXX:XXXX/api/ws_testDeploy?token=DevToken", "database" : "QA_LIKE"},
        "XXXXXX_INT" : {"env" : "XX.XX.XX.XXX", "url" : "http://XX.XX.XX.XXX:XXXX/api/ws_testDeploy?token=DevToken", "database" : "INT"},
        }


#############################################################################

print(" ### Variables ### ")
envChoice = dEnv[args.env]
					
Buildnumber = args.Buildnum
KXview_HOME =  os.getenv("HOME")
KX_HOME =subprocess.getoutput(['source /opt/apps/kXview/.bash_profile && echo $KX_HOME'])
PATH =subprocess.getoutput(['source /opt/apps/kXview/.bash_profile && echo $PATH'])
os.environ["PATH"] = PATH
PATH=os.getenv("PATH")
KX_HOME=os.getenv("KX_HOME")
JAVA_HOME=os.getenv("JAVA_HOME")

version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
print (version)
###########################################################################################								   

def send_mail(send_from, send_to, subject, text, files=None, server="SMTPserver"):
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

log_file_name = os.environ['HOME'] + "/DevOps/logs/log_deploy." + ts

class Logger(object):
        def __init__(self, log_filename=log_file_name):
                self.terminal = sys.stdout
                self.log = open(log_file_name, "w")

        def write(self, message):
                self.terminal.write(message)
                self.log.write(message)

        def flush(self):
                pass

        def close(self, message):
                self.log.close()

sys.stdout = Logger(log_file_name)

if args.env is not None:
        print('The Project Name is {}'.format(args.env))
else:
        print('Oh well ; No args, no problems')


#ludb_data = json.load(open('ludb.json'))
env_dir = args.env
print(args.env)
path = "{}/DevOps/{}/".format(KXview_HOME, Buildnumber)

srcfullpath = os.path.join(path,args.env,'Implementation/LogicalUnits')
srcpath = os.path.join(path,args.env)



print (srcfullpath)
fullpath_dirs = os.listdir(srcfullpath)
print(fullpath_dirs)



print("****************")
print(srcpath)


items = []
# hello
class Item():
        def  __init__(self, env, logicalunit, files, file_count):
                self.env = args.env
                self.logicalunit = logicalunit
                self.files = files
                self.file_count = file_count

root_destdir = os.environ['HOME'] + '/DevOps/'

FROM = "XXXXXX@XXXXXX.com"
SUBJECT = hostname + ": X.X.X_X Deploy Status"
TO = ['XXXXXX@XXXXXX.com','XXXXXX@XXXXXX.com','XXXXXX@XXXXXX.com','XXXXXX@XXXXXX.com']


for logicalunit in fullpath_dirs:
    #print("logicalunit:")
    #print(logicalunit)
    #print(" ")

    com_build_art = com_build_art =  os.environ['HOME'] + "/fabric/scripts/buildAndDeployArtifacts.sh -pd " + os.environ['HOME'] + "/DevOps/" + Buildnumber + "/{X} -s TRUE -l {X}".format(Buildnumber,env_dir,logicalunit)
    print("com_build_art:")
    print('##[command]' + com_build_art)
    print(" ")
		   
   

    # Execute the shell command
    p = subprocess.Popen(com_build_art, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = p.communicate()
																																																													   

    print(output.decode('utf-X'))
												   
    print(" ")
    print(" ")
    #print("################################")
    #print(errors.decode('utf-X'))
    #print("################################")
    Err = output.decode('utf-X')
    if " error " in Err  or " errors " in Err or " faild " in Err or " Failed: " in Err:
       print('##[error]')
       print(errors.decode('utf-X'))
       print(" ")
       print(" ")
       sys.exit(X)
    else:
       pass
    pattern = r"Deploy.*Failed:"
    result = re.search(pattern, Err)
    if result:
       print('##[error]')
       print(errors.decode('utf-X'))
       print(" ")
       print(" ")
       sys.exit(X)
    else:
       pass
							
																  

url_r = envChoice['url']

print(url_r)


