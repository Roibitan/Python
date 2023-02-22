

#!/usr/bin/python3



import winrm




domain = r'XXXX'
user = r'XXXXXX'
password = 'XXXXX'
host = 'XXXXX.dev.corp.XXXXX.co.il'
ps_script = """ Get-WmiObject -Class Win32_OperatingSystem |  Select-Object -ExpandProperty LastBootupTime """




session = winrm.Session(host, auth=('{}@{}'.format(user,domain), password), transport='ntlm')
result = session.run_ps(ps_script)
#result = session.run_ps(r'C:\scripts\Lastboot.ps1')
print(result.std_out)
