#!/usr/bin/python3

import cgi
import smtplib

print("Content-type: text/html")
print()

mydata = cgi.FieldStorage()

data = mydata.getvalue("cmd")

# send mails using python

import smtplib
#Simple Mail Transfer Protocol

senders_mail = "YOUR EMAIL"
password = "APP PASSWORD"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=senders_mail,password=password)


mail_content = "Subject: Email from EC2 Instance? \n\n Hey Buddy, how are you? I am send you this email using python on EC2 instance"


connection.sendmail(from_addr=senders_mail, to_addrs="malhotraakhil45@gmail.com", msg=mail_content)

connection.close()

print("<pre>")
print(output)
print("</pre>")