import urllib.request
import json
import time
import webbrowser

count = 0

while True:
	url = 'https://aws.random.cat/meow'
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())

	print(result)
	
	webbrowser.open(result["file"])
	time.sleep(1)
	
	count += 1
	
	if count == 10:
		break
