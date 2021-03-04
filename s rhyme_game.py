import time
import random
import urllib.request
import json
import requests

health = 100
money = 0
name = ''

print('''

 __          __  _                          _ 
 \ \        / / | |                        | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___(_)
                                              
                                              
''')



name = input("You wandered far to join our game, weary traveller, what is your name? ")

url = 'https://api.datamuse.com/words?rel_rhy=' + name
response = urllib.request.urlopen(url)
result = json.loads(response.read())
rhyme = result[random.randint(0, len(result)-1)]
word = rhyme['word'] 

url2 = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1'
response2 = urllib.request.urlopen(url2)
result2 = json.loads(response2.read())
word2 = result2['text']

def intro():
	print(f'Welcome {name}! I am glad to see you on this adventure\n')
	time.sleep(1)
	print(f'{name}, did you know {word2}\n')
	
	print(f'The wise old man says {name}! Funny, that sounds like {word.title()}!\n')
	time.sleep(1)
	print(f'''{word.title()}, I mean {name.title()}...  You are at {health} health and have {money} space credits! \n
		You wake up and find yourself in a tiny room
		You wonder if {word} really should be your name...
		No! you are going to stick with {name}, not {word}!
		You have no idea where you are, and see nothing in
		the inky darkness other than a tiny door.
		
		You have three choices:
		1. You can stay in the room and sleep
		2. You can throw open the door and fight
		3. You can open the door and sneak out in the darkness''')

	choice = input("\nPlease pick an option: ")
	choice = int(choice)

	if choice == 1:
		time.sleep(1)
		print("You decide to do nothing, and fall asleep\n\n\n\n\n")
		time.sleep(2)
		intro()
	elif choice == 2:
		fight()
	elif choice == 9:
		question()
	else:
		sneak()

def fight():
    time.sleep(2)
    print('You decide you are going to fight.')
    print('The bad guy says you have to pick a number between 1 and 10.')
    print('Guess right and you win!')
    print(f'You are at {health} health')

    choice = input("Please pick a number from 1-10: ")
    choice = int(choice)

    computer = random.randint(1,10)

    if choice == computer:
        print("You win!")
        intro()
    else:
        time.sleep(1)
        print("You did not win, and got thrown back in the dark room\n\n\n\n\n\n")
        time.sleep(1)
        intro()

def sneak():
	print("You decide to sneak out")
	time.sleep(2)
	print("you open the door")
	time.sleep(2)
	print("and feel your way to another door")
	time.sleep(2)
	print("and get sucked out into the void of space.\n")
	time.sleep(2)
	print("Game over!\n\n")
	time.sleep(2)
	print("Or is it?... As you float away from what you now realize was a space station, ")
	time.sleep(2)
	print("You get sucked up by a passing Valdorki space ship\n")
	time.sleep(2)
	valdorki()
    
def valdorki():
	print(f'You find yourself on the Valdorki ship shivering and cold')
	time.sleep(1)
	print(f'in a brightly lit cargo bay. Welcome {word.title()}! booms a thunderous voice')
	time.sleep(1)
	print(f'in the distance. You look up to see a strange looking creature staring')
	time.sleep(1)
	print(f'at you. Why are they calling me {word.title()}? dont they know my name is {name.title()}')
	time.sleep(1)
	print(f'you wonder?')
	time.sleep(1)
	print('The creature thinks for a moment and says, "let me tell you a story about')
	time.sleep(1)
	print('Why you are here...')
	choice = input("Do you want to hear why you are here? ")
	time.sleep(1)
	
	if choice == "y":
		cargo_hold()
	else:
		cargo_hold()	
	
	
def cargo_hold():	

	food = ['butterbeer','cupcakes','hamburger','water']
	color = ['blue','purple','orange','gray','black','white','a color that has no name']
	weather = ['cloudy','rainy','snowy','sunny']
	action = ['walk','swim','jump','dance','run','sing']

	food2 = random.choice(food)

	eatdrink = ''

	if food2 == 'water':
		eatdrink = 'drank'
	elif food2 == 'butter beer':
		eatdrink = 'drank'	
	else:	
		eatdrink = 'ate'
		
	url = 'https://api.datamuse.com/words?rel_rhy=' + food2
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	rhyme2 = result[random.randint(0, len(result)-1)]
	food2 = rhyme2['word'] 	

	print(f'\t\nOne day, {word.title()}, I mean {name.title()}, went for a {random.choice(action)} because they had turned {random.choice(color)}.')
	time.sleep(2)
	print(f'\t{name.title()} noticed that the sky was a strange shade of {random.choice(color)}.')
	time.sleep(2)
	print(f'\tGood thing that {name.title()} stayed inside on this very {random.choice(weather)} day.')
	time.sleep(2)
	print(f'\tFor lunch on the space station they were serving {random.choice(color)} {random.choice(food)}')
	time.sleep(2)
	print(f'\tEveryone decided to eat {random.randint(1,40)} servings of {random.choice(color)} {food2}')
	time.sleep(2)
	print(f'\t{name.title()} {eatdrink} more {random.choice(color)} {food2} than everyone!')
	time.sleep(2)
	print(f'\tThen {name.title()} woke up on the Valdorki ship, and the rest is history')
	time.sleep(2)
	print(f'\tYour mouth feeling like cotton candy, you slowly say')
	time.sleep(2)
	print(f'\t"that made no sense at all..."')
	time.sleep(2)
	
	url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1'
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	word2 = result['text']
	
	print(f'\nWant to know why we call you {word.title()}?')
	print(f"It's because {word2}")
	
	time.sleep(2)
	
	print(f'\nYou now have two choices, you can run for the void of space,')
	print(f'or you can ask the strange alien a question')
	
	choice = input("1 for escape, and 2 for question \n")
	choice = int(choice)
	
	if choice == 1:
		bounce()
	else:
		question()	
	
def bounce():
	print('you try to run at the force field')
	time.sleep(1)
	print('then realize its a force field and bounce off')
	time.sleep(1)
	question()

def question():
	number = input("Give me a number and we can then get to your question ")
	
	#https://github.com/zanadaniel/numbers-api/blob/master/script.py	
	# checks if the user input is valid, if true, it'll make a GET request using that number and respond with a fact about it
	if number.isdigit():
		response = requests.get("http://numbersapi.com/" + str(number))
		print("\n\n" + response.text)

	# if user input is not valid, it'll notify the user accordingly and then give them a fact about some random generated number
	else:
		print("You didn't enter a whole number, but here's a random number fact anyways!")
		random_number = random.randrange(1, 200)
		response = requests.get("http://numbersapi.com/" + str(random_number))
		print("\n\n" + response.text)

	time.sleep(1)
	print("\nNow that you know a little bit about numbers, let me tell you my story\n")
	time.sleep(1)
	print('A long time ago, in a galaxy far far away...')
	time.sleep(1)
	print('It is a period of civil wars in the galaxy. A brave alliance ')
	time.sleep(1)
	print('of underground freedom fighters has challenged the tyranny ')
	time.sleep(1)
	print('and oppression of the awesome GALACTIC EMPIRE.')
	time.sleep(1)
	print('Striking from a fortress hidden among the billion stars of the galaxy, ')
	time.sleep(1)
	print('rebel spaceships have won their first victory in a battle with the ')
	time.sleep(1)
	print('powerful Imperial Starfleet. The EMPIRE fears that another defeat could ')
	time.sleep(1)
	print('bring a thousand more solar systems into the rebellion, and Imperial ')
	time.sleep(1)
	print('control over the galaxy would be lost forever.')
	time.sleep(1)
	print('To crush the rebellion once and for all, the EMPIRE is') 
	time.sleep(1)
	print('constructing a sinister new battle station. Powerful enough to ')
	time.sleep(1)
	print('destroy an entire planet, its completion spells certain ')
	time.sleep(1)
	print('doom for the champions of freedom.')
	print('\n\n')
	time.sleep(2)
	print('...and now it is time to tell you I am Sheldon Cooper! \n')
	time.sleep(1)
	print('''
	
           ___
     |     | |
    / \    | |
   |--o|===|-|
   |---|   |d|
  /     \  |w|
 | U     | |b|
 | S     |=| |
 | A     | | |
 |_______| |_|
  |@| |@|  | |
___________|_|_
The end or just the beginning?   

   ''')
	
	
intro()
