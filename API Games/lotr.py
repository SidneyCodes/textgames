import urllib.request
import json
import os


# Set the api endpoint to the OWM url
url = "https://the-one-api.herokuapp.com/v1/character"

# Make our request and get the decoded data read from the request
req = urllib.request.Request(url)
req.add_header("Authorization", "Bearer " + 'vB8eLFNL4t8akvnlGCAY')   

resp = urllib.request.urlopen(req)

resp = json.loads(resp.read())

#print(resp)

#print(resp["docs"][0]["name"])

print(len(resp["docs"]))

people = resp['docs']

for person in people:
	print(f'{person["name"]} is {person["gender"]} and is {person["race"]}')
	if person["realm"] != "":
		print(f'Lives in the realm of {person["realm"]} ')	

# Read the JSON data into a Python Data Type
#data = json.loads(resp)
#print(data.keys())

#with open('data.txt', 'w') as outfile:
#    json.dump(data, outfile)
#for item in data["docs"]:
#    if item["race"] == "Hobbit":
#        print(item["name"])