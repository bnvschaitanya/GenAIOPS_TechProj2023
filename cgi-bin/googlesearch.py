#!/usr/bin/python3

import cgi
from googlesearch import search
'''
try:
    from googlesearch import search
except ImportError:
    print("Content-type: text/html\n")
    print("No module named 'google' found")
    exit()
'''
# Print the HTTP header
print("Content-type: text/html\n")


form = cgi.FieldStorage()

query = cgi.getvalue("cmd")

# HTML content
print("<html>")
print("<head><title>CGI Google Search</title></head>")
print("<body>")

# Search query
#query = "Sudhanshu Namdev"

# Perform the search
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print("<p>" + j + "</p>")

print("</body>")
print("</html>")