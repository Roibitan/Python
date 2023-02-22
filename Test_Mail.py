
#!/usr/bin/python3
#!/usr/bin/python


print('Hellow World')



import smtplib

sender = 'Test@fromdomain.com'
receivers = ['XXXXXX@XXXXXXX.co.il']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('XXXXX.XXXXX.XXXXX.XXXXX')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
