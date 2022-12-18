from __future__ import division

import json

import math

import platform

import subprocess

import warnings

warnings.filterwarnings(action='ignore',module='.*paramiko.*')

import paramiko

import winrm

import os

import colorama

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

 

#with open('c:\\server-check\\servers.json', 'r') as f:

#    data = json.load(f)

 

### get the verbals from azure and create the path ###

System = os.environ['Sys']

CMTeam = os.environ['CMT']

project = os.environ['Project']

env = os.environ['Env']

 

env = env.split(',')

project = project.split(',')

#PATH = System + CMTeam + "\Machina_List.json"

PATH = System + CMTeam + "\Servers.json"

#print (PATH)

with open(PATH, 'r') as f:

    data = json.load(f)

 

username = 'Username'

password = 'UserPass'

domain = 'Domain'

 

print('''#################################################################

################################################################''')

print('The Script will run on the follwing Environments:', env , 'in projects:', project)

print('''#################################################################

################################################################''')

#print('The Script will run on the follwing Environments:', env , 'in projects:', project)

#print('\033[31m' + 'The Script will run on the follwing Environments:', env , 'in projects:', project)

#print('##[section] Test')

#print(env + project)

#environments = ['Sap', 'BizTalk']

 

result1 = data["servers"]

for environment in env:

    for project_name in project:

        for r in result1:

 

            # windows machines

            if r['Env'] == environment:

                if r['Project'] == project_name:

                    if r['OS'] == "Windows":

 

                        #print the server name

                        server_name = (r['server_name'])

                        print('##[command] Server Name:' + server_name)

                        print("")

 

                        # ping check

                        command = ['ping', '-n', '1', server_name]

                        FNULL = open(os.devnull, 'w')

                        response = subprocess.call(command, stdout=FNULL)

                        if response == 0:

                            print("##[section]PING OK")

                            #print(Fore.GREEN + 'PING OK')

                        else:

                            print("##[error]THERE IS NO PING")

                            #print(Fore.RED + 'THERE IS NO PING')

 

                        #cpu and memory check

                        session = winrm.Session(server_name, auth=('{}@{}'.format(username,domain), password), transport='ntlm')

 

                        #memory

                        try:

                            r = session.run_ps("write-host ((((Get-WmiObject -ComputerName {} -Class win32_operatingsystem -ErrorAction Stop).TotalVisibleMemorySize - (Get-WmiObject -ComputerName {} -Class win32_operatingsystem -ErrorAction Stop).FreePhysicalMemory)*100)/ (Get-WmiObject -ComputerName {} -Class win32_operatingsystem -ErrorAction Stop).TotalVisibleMemorySize)".format(server_name, server_name, server_name))

                        except:

                            print("##[error]REOMOTE CONNECT TO MACHINE {} FAILED".format(server_name))

                            #print(Fore.RED + 'REOMOTE CONNECT TO MACHINE {} FAILED'.format(server_name))

                        else:

                            result_mem = r.std_out

                            #print(result_mem)

                            result_mem = result_mem.strip()

                            result_mem = int(float(result_mem))

                            if result_mem >= 90:

                                print("##[error]WARNING! MEMORY IS {}%".format(result_mem))

                                #print(Fore.RED + 'WARNING! MEMORY IS {}%'.format(result_mem))

                            else:

                                print("##[section]MEMORY OK {}%".format(result_mem))

                                #print(Fore.GREEN + 'MEMORY OK ')




                        #cpu

                        try:

                            r = session.run_ps("write-host (Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select Average)")

                        except:

                            print("##[error]REOMOTE CONNECT TO MACHINE {} FAILED".format(server_name))

                            #print(Fore.RED + 'REOMOTE CONNECT TO MACHINE {} FAILED'.format(server_name))

                        else:

                            result_cpu = r.std_out

                            #print(result_cpu)

                            result_cpu = result_cpu.replace("@{Average=","")

                            result_cpu = result_cpu.replace("}","")

                            result_cpu = result_cpu.strip()

                            result_cpu = int(float(result_cpu))

                            if result_cpu >= 90:

                                print("##[warning]WARNING! CPU IS {}%".format(result_cpu))

                                #print(Fore.RED + 'WARNING! CPU IS {}%'.format(result_cpu))

                            else:

                                print("##[section]CPU OK {}%".format(result_cpu))

                                #print(Fore.GREEN + 'CPU OK')

                        #disks

                        try:

                            r = session.run_ps("get-PSDrive | where {$_.Free -gt 0}")

                        except:

                            print("##[error]REOMOTE CONNECT TO MACHINE {} FAILED".format(server_name))

                            #print(Fore.RED + 'REOMOTE CONNECT TO MACHINE {} FAILED'.format(server_name))

                        else:

                            result_disk = r.std_out

                            #print(result_disk)

                            result_disk = result_disk.strip()

                            #print(result_disk)

                            result_disk = result_disk.splitlines()

                            number = len(result_disk)

                            for i in range(2,number):

                                info = (result_disk[i])

                                info = info.split()

                                #print(info)

                                disk_name = info[0]

                                used_space = info[1]

                                free_space = info[2]

    

                                #print("disk:{}, free:{}, used:{}".format(disk_name,free_space,used_space))

                                disk_per = float(used_space) / (float(free_space) + float(used_space))

                                disk_per = round((float(disk_per) * 100.0 ),2)

                                #print(disk_per)

                                if disk_per >= 90.0:

                                    #disk_per = math.trunc(disk_per)

                                    print("##[error]disk {} is almost FULL {}%".format(disk_name,disk_per))

                                    #print(Fore.YELLOW + 'disk {} is almost FULL'.format(disk_name))

                                else:

                                    #disk_per = math.trunc(disk_per)

                                    print("##[section]disk {} is OK {}%".format(disk_name,disk_per))

                                    #print(Fore.GREEN + 'disk {} is OK'.format(disk_name))

    

                    #   print("")

                    

 

                    # linux machines

                    else:

                        server_name = r['server_name']

                        print('##[command] Server Name:' + server_name)

                        print("")

                        # ping check

                        command = ['ping', '-c', '1', server_name]

                        FNULL = open(os.devnull, 'w')

                        response = subprocess.call(command, stdout=FNULL)

                        if response == 0:

                            print("##[section] PING OK")

                            #print(Fore.GREEN + 'PING OK')

                        else:

                            print("##[error]THERE IS NO PING")

                            #print(Fore.RED + 'THERE IS NO PING')

 

                        #username and password

                        port = '22'

                        username = 'UserName'

                        password = 'UserPass'

 

                        #connect to the server

                        s = paramiko.SSHClient()

                        s.load_system_host_keys()

                        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                        try:

                            s.connect(server_name, port, username, password)

                        except:

                            print("##[error]REOMOTE CONNECT TO MACHINE {} FAILED".format(server_name))

                            #print(Fore.RED + 'REOMOTE CONNECT TO MACHINE {} FAILED'.format(server_name))

                        else:

                            #memory check

                            command = "echo $[$(free | head -2| tail -1 | awk '{print $4}')] $[$(free | head -2| tail -1 | awk '{print $2}')]"

                            (stdin, stdout, stderr) = s.exec_command(command)

                            for mem_usage in stdout.readlines():

                                a = mem_usage.split(" ")

                                free_mem = a[0]

                                total_mem = a[1]

                                mem_usage = int(free_mem) / int(total_mem)

                                mem_usage = mem_usage * 100

                                #print(mem_usage)

                                if mem_usage >= 90:

                                    print("##[warning]WARNING! MEMORY IS {}%".format(mem_usage))

                                    #print(Fore.RED + 'WARNING! MEMORY IS {}%'.format(result_mem))

                                else:

                                    print("##[section]MEMORY OK {}% ".format(mem_usage))

                                    #print(Fore.GREEN + 'MEMORY OK')

 

                            #cpu check

                            command = "echo $[100-$(vmstat 1 2 | tail -1 | awk '{print $15}')]"

                            (stdin, stdout, stderr) = s.exec_command(command)

                            for cpu_usage in stdout.readlines():

                                cpu_usage = int(float(cpu_usage))

                                if cpu_usage >= 90:

                                    print("##[warning]WARNING! CPU IS {}%".format(cpu_usage))

                                    #print(Fore.RED + 'WARNING! CPU IS {}%'.format(result_cpu))

                                else:

                                    print("##[section]CPU OK {}%".format(cpu_usage))

                                    #print(Fore.GREEN + 'CPU OK')

 

                            #disks check

                            command = "df -h"

                            (stdin, stdout, stderr) = s.exec_command(command)

                            for fs_usage in stdout.readlines():

                                #print(fs_usage.strip())

                                fs_usage = fs_usage.strip()

                                fs_usage = fs_usage.encode("utf-8")

                                fs_usage = fs_usage.split()

                                #print(fs_usage)

                                fs_per = fs_usage[4]

                                fs_per = fs_per[:-1]

 

                                if fs_per != "Use":

                                    fs_per = int(fs_per)

                                    if fs_per >= 98:

                                        fs_name = fs_usage[5]

                                        print("##[warning]WARNING! {} is {}%".format(fs_name,fs_per))

                                        #print(Fore.RED + 'WARNING! {} is {}%'.format(fs_name,fs_per))

                                #print(fs_usage)

                                #print("")

                            s.close()

 

    # session = winrm.Session(server, auth=('{}@{}'.format(user,domain), password), transport = 'ntlm')

 

 
