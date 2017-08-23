import requests
import json
import csv
import sys
v = sys.version
reload(sys)
sys.setdefaultencoding('utf-8')

base = "https://maps.googleapis.com/maps/api/geocode/json?address="
key = "&key=AIzaSyCB5mkUMlUb5jocXFv-6qb5B7WjB2zIK-8"
locations = ["Latitude","Longitude"]

def find_coordinates(address):
    if address[:4] == "Off ":
        address = address[4:]
    try:
        
        estimation = json.loads(requests.get(base + address + key).content)
        try:
            lat = estimation['results'][0]['geometry']['location']['lat']
            lng = estimation['results'][0]['geometry']['location']['lng']
            return [lat, lng]
        except IndexError:
            return ["Zero Results","Zero Results"]
    except UnicodeDecodeError:
        return ["Decode Error","Decode Error"]

with open('/Users/ianlewis/Documents/GitHub/ianlew.is/dev-projects/Map/Plane Crashes 2.csv','r') as csvfile:
    crash_data = csv.reader(csvfile)
    for row in crash_data:
        location = find_coordinates(row[2])
        print(location)
        locations.append(location)

with open("/Users/ianlewis/Documents/GitHub/ianlew.is/dev-projects/Map/Location Output.csv","wb") as outputfile:
    loc_data = csv.writer(outputfile, delimiter=',')
    for location in locations:
        loc_data.writerow(location)
