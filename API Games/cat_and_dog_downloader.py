import urllib.request
import json
import time
import webbrowser
import random
import requests
import os


def intro():
	print("Welcome to the cat/kitten/dog downloader")
	
	
	choice = input("Do you want cats or dogs? ")

	option_c = ['c','C','cat','Cat','CAT','cats','Cats','CATS']

	if choice in option_c:
		loop = 0
		
		choice = input("Do you want to [d]ownload or [v]iew in browser? ")
		
		if choice.lower() == 'v':
			while True:
				url = 'https://api.thecatapi.com/v1/images/search'
				response = urllib.request.urlopen(url)
				result = json.loads(response.read())
			
				picture = result[0]['url']
			
				webbrowser.open(picture)
			
				loop += 1
				
				time.sleep(2)
			
				if loop == 10:
					break
		else:
			choice = input("Do you want [c]ats or [k]ittens? ")
			
			if choice == 'k':
				download_kitten()
			else:
				download_cat()	 
			
		
	else:
		download_dog()
		
def download_kitten():
	counter = 0

	choice = input("Has cat? How many kitten pictures can I get for you? ")
	
	try:
		choice = int(choice)
	except ValueError:
		choice = 2
	else:
		choice = 2	


	for cat in range(0,choice):
		url = f'http://placekitten.com/{random.randint(100,500)}/{random.randint(100,500)}'
		r = requests.get(url, allow_redirects=True)

		open(f'cat{counter}.jpg', 'wb').write(r.content)
		counter += 1
		print(counter,"Kitten downloaded!")
	time.sleep(3)
	intro()	



def download_dog():
	counter = 1

	choice = input("Has dog? How many dog pictures can I get for you? ")
	choice = int(choice)

	for cat in range(1,choice):
		url = f'https://placedog.net/640/480?random'
		r = requests.get(url, allow_redirects=True)

		open(f'dog{counter}.jpg', 'wb').write(r.content)
		counter += 1
		print(counter,"Dog downloaded!")
	
	time.sleep(3)
	
	intro()	

	
	


def download_cat():
	counter = 1

	choice = input("Has cat? How many cat pictures can I get for you? ")
	choice = int(choice)
	
	for cat in range(1,choice):
		url = 'https://api.thecatapi.com/v1/images/search'
		response = urllib.request.urlopen(url)
		result = json.loads(response.read())
		picture = result[0]['url']
		
		r = requests.get(picture, allow_redirects=True)
		
		open(f'cat{counter}.jpg', 'wb').write(r.content)
		counter += 1
		print(counter,"Cat downloaded!")
	time.sleep(3)	
	intro()	
	

intro()
