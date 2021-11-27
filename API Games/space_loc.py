import urllib.request
import json
import time

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
print("Did the API work?",result["message"])
print("Timestamp",time.ctime(result["timestamp"]))

lat = result["iss_position"]["latitude"]
lon = result["iss_position"]["longitude"]

print(lat,lon)

map_url = f'https://www.google.com/maps/place/{lat}+{lon}'
print(map_url)