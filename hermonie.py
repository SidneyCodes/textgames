import urllib.request
import json
import time
import random

url = 'https://raw.githubusercontent.com/SidneyCodes/advice/master/advice.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print("You are walking along at Hogwarts, and see Hermonie")
time.sleep(2)
print("As a new student, you wonder if she has any advice for you")
time.sleep(2)
print("Hermonie says...")
time.sleep(2)
print(result[random.randint(1,49)]['advice'])
