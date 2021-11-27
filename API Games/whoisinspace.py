import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
print("Did the API work?",result["message"])
print("There are",result["number"],"people in space:")
for astro in result["people"]:
    print("\t",astro["name"],"is on the",astro["craft"])
