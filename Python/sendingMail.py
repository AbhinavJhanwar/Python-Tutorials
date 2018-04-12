'''
Created on Mar 13, 2018

@author: abhinav.jhanwar
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

sender = 'AIWIZ@botAgent.com'
receivers = ['abhinav.jhanwar@accenture.com']

try:
    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = receivers
    msg['Subject'] = "SMTP e-mail test"
     
    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))
    
    '''# attachement
    filename = "emailTest.txt"
    attachment = open("emailTest.txt", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)'''
    
    print("step0")
    # connect to server
    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
    print("step1")
    server.starttls()
    print("step2") 
    #server.login('abhij.1994@gmail.com', "password")
    print("step3")
    text = msg.as_string()
    server.sendmail(sender, receivers, text)
    server.quit()
    print("E-mail sent.")
    
except:
    logging.exception("Here is the error:\n")