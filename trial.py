from geopy.geocoders import Nominatim
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode("mumbai")
 
# printing address
print(getLoc.address)
 
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)
# Import module
from geopy.geocoders import Nominatim
 
# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
 
# Assign Latitude & Longitude
Latitude = 23
Longitude = 85

latitude1 = 30.594095
longitude2 = 70.137566
 

 
# Get location with geocode
# location = geolocator.geocode(Latitude+","+Longitude)


# location = list((location))[0]
# place = []
# for x in location:
    
#     place.append(x)
#     if ',' in x:
#         break
# places = "".join(place)
# places = places[0:-1]
# print(places)

import geocoder
g = geocoder.ip('me')
print(g.latlng)

a = g.latlng

lat2 = a[0]
lon2 = a[1]

loc1 = (Latitude,Longitude)
loc2 = (lat2,lon2)
import haversine as hs
from haversine import Unit

print("abc")
a = hs.haversine(loc1,loc2,unit = Unit.MILES)
print(a)


