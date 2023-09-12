#!/usr/bin/env python3
import geocoder

print("Content-type: text/html\n")

g = geocoder.ip('me')
latlng = g.latlng

print("<html>")
print("<head>")
print("<title>IP Geolocation</title>")
print("</head>")
print("<body>")
print("<h1>IP Geolocation</h1>")
print("<p>Latitude: {}</p>".format(latlng[0]))
print("<p>Longitude: {}</p>".format(latlng[1]))
print("</body>")
print("</html>")