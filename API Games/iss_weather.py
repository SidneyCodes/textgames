import urllib.request
import json
import time

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)

lat = result["iss_position"]["latitude"]
lon = result["iss_position"]["longitude"]
api = '65ad96e90e401baf71ab393dfffbc44d'

url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print(result)
print("The space station is at",lat,lon)
print((result["main"]["temp"] - 273.15) * 9/5 + 32,"F")
if result["name"] == "":
    print("The ISS is over water")
else:
    print("The ISS is over",result["name"],"in country of",result["sys"]["country"])    

#(0K − 273.15) × 9/5 + 32 = -459.7°F
