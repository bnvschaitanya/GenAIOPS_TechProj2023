#!/usr/bin/env python3
import cgi
from geopy.geocoders import Nominatim

form = cgi.FieldStorage()

location_name =form.getvalue("cmd")

def get_location_info(location_name):
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.geocode(location_name)
    return location

print("Content-type: text/html")
print()

location = get_location_info(location_name)

print("<html>")
print("<head>")
print("<title>Location Information</title>")
print("</head>")
print("<body>")
print("<h1>Location Information</h1>")

if location:
    print("<p>Address: {}</p>".format(location.address))
    print("<p>Latitude: {}</p>".format(location.latitude))
    print("<p>Longitude: {}</p>".format(location.longitude))
else:
    print("<p>Location not found.</p>")

print("</body>")
print("</html>")