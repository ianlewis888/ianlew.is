import requests
import json

base = "https://maps.googleapis.com/maps/api/geocode/json?address="
key = "&key=AIzaSyCB5mkUMlUb5jocXFv-6qb5B7WjB2zIK-8"
address = "Fort Myer, Virginia"

estimation = json.loads(requests.get(base + address + key).content)
lat = estimation['results'][0]['geometry']['location']['lat']
lng = estimation['results'][0]['geometry']['location']['lng']
print('lat: '+str(lat)+', long: '+str(lng))
