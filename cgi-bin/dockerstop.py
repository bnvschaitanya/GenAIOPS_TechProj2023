#!/usr/bin/python3

import cgi
import subprocess

print("Content-type: text/html")
print()

form = cgi.FieldStorage()


cmd =form.getvalue("cmd")


output = subprocess.getoutput("sudo docker kill $(docker ps -a -q)")
dockerps = subprocess.getoutput("sudo docker ps")

print("<pre>")
#print("Below is your Response")
print(output)
print(dockerps)
print("</pre>")