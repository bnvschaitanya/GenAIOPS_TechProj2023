#!/usr/bin/python3

from twilio.rest import Client
import cgi


print("Content-type: text/html")
print()

form = cgi.FieldStorage()

num = form.getvalue("num")
msg = form.getvalue("msg")
account_SID="YOUR ACCOUNT SID"
account_token="YOUR ACCOUNT TOKEN"

twillios_phn ="+17624754370"
my_phn = "+YOUR PHONE NUMBER"

client = Client(account_SID,account_token)

message = client.messages.create(
    body=msg,
    from_= twillios_phn,
    to = my_phn
)

print("<pre>")
print(message)
print("</pre>")
                   