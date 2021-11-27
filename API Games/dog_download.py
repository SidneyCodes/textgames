import urllib.request
import json
import requests
import random

counter = 0

choice = input("How many dog pictures can I get for you?")
choice = int(choice)

for dog in range(1,choice):
    url = 'https://dog.ceo/api/breeds/image/random'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    #print(result)
    url = result["message"]
    r = requests.get(url, allow_redirects=True)
    #print(r)

    open(f'dog{counter}.jpg', 'wb').write(r.content)
    counter += 1
    print(counter, "Dog downloaded")

