import urllib.request
import json
import time

print("Welcome to the Space Station Passfinder!")
print("""
[1] Look up when the ISS will pass over Rome
[2] Look up your own lat/lon
[3] Look up the Titanic
""")
choice = input("Please make a selection:")
if choice == '1':
    lat,lon = 41.8839903,12.5099995
elif choice == '3':
    lat, lon = 14.5994, 28.6731    
else:
    while True:
        try:
            lat = float(input("Please enter the lat "))
            break
        except:
            print("Please try again")
            pass
    lon = float(input("Please enter the lon "))

url = f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
print("Did the API work?",result["message"])
print("There will be",result["request"]["passes"],"passes over your location")
for over in result["response"]:
    print("The ISS will be overhead at",time.ctime(over["risetime"]),"UTC for",over["duration"],"seconds")