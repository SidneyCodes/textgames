import urllib.request
import json
import time
import webbrowser
import random
import requests
import os

chuck = ['Chuck-Norris','Chuck-Norris-Approves','Chuck-Norris-Finger','Chuck-Norris-Flex','Chuck-Norris-Guns','Chuck-Norris-Laughing','Chuck-Norris-Phone','Chuck-Norris-With-Guns']
option2 = ['Angry-Birds-Pig','Chemistry-Cat','Blob','Advice-Doge','Grumpy-Cat-Not-Amused','Grumpy-Cat-Star-Wars','Han-Solo','Deadpool-Surprised','Grumpy-Cat','Grumpy-Cat-Bed','Grumpy-Cat-Birthday','Grumpy-Cat-Christmas','Grumpy-Cat-Does-Not-Believe','Advice-Yoda']

random.shuffle(option2)

choice1 = input("What should top text be? ")
choice2 = input("What should bottom text be? ")
choice3 = input("Do you want Chuck Norris or Option [B]? ")
count = input("How many memes do you want? ")

count = int(count)

loop = 0

pick = ''

if choice3 == 'B':
	pick = option2
else:
	pick = chuck	

while True:
	url = f'http://apimeme.com/meme?meme={random.choice(pick)}&top={choice1}&bottom={choice2}'
	r = requests.get(url, allow_redirects=True)

	open(f'picture_meme{loop}.jpg', 'wb').write(r.content)
	filename = 'file:///'+os.getcwd()+'/' + f'picture_meme{loop}.jpg'
	
	webbrowser.open(filename)

	print("Meme Complete!")

	loop += 1
	
	if loop == count:
		break

print("Meme complete!")		

#http://apimeme.com/?ref=apilist.fun

