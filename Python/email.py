'''
Created on Mar 13, 2018

@author: abhinav.jhanwar
'''

import smtplib
import base64

filename = "emailTest.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'server@server.com'
reciever = 'emailaddress1'

marker = "heading"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <server@server.com>
To: To Person <emailaddress1>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('emailaddress2', 'password')
    smtpObj.sendmail(sender, reciever, message)
    print ("Successfully sent email")
except Exception:
    print ("Error: unable to send email")