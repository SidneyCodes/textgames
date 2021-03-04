from time import sleep
import random
from os import system, name
import urllib.request
import json


item = []
money = 0 

print('''

  _____ ____   ____    __    ___      ______  ____    ____  ____  _     
 / ___/|    \ /    |  /  ]  /  _]    |      ||    \  /    ||    || |    
(   \_ |  o  )  o  | /  /  /  [_     |      ||  D  )|  o  | |  | | |    
 \__  ||   _/|     |/  /  |    _]    |_|  |_||    / |     | |  | | |___ 
 /  \ ||  |  |  _  /   \_ |   [_       |  |  |    \ |  _  | |  | |     |
 \    ||  |  |  |  \     ||     |      |  |  |  .  \|  |  | |  | |     |
  \___||__|  |__|__|\____||_____|      |__|  |__|\_||__|__||____||_____|
                                                                        

''')

def intro(item,money):
	
	print("One day, Isabel was tired of being a silent space and time travelling mime.")
	sleep(2)
	print("So, she went for a walk, out on the space platform, on star station Old Victoria,")
	sleep(2)
	print("and while walking, and floating down the space platform,")
	sleep(2)
	print("she found a newspaper! A real, old Earth, newspaper! Oh my, tut tut and chip chip doodle!")
	sleep(3)
	print("The newspaper looks old and magical, do you want to take it?\n")
	
	print("You can also play trivia by pressing [t]")
	choice = input("Do you take thy newspaper to readth with thine eyes? y/n ")
	
	sleep(2)
	if choice == 'y':
		print("You take the newspaper and stick it in your space sachel\n")
		item.append("newspaper")
		sleep(2)
	elif choice == 't':
		trivia(item,money)	
	else:
		print("You decide its best not to take that old Earth rag and keep on walking by\n")
		item.append("nothing")
		sleep(2)
	
	sam(item, money)	

def sam(item,money):
	
	
	print("You are stopped by a space cop, who asks what you have in your sachel")
	sleep(2)
	print("You open the sachel to show the space cop you have a whole lot of",item[0],"\n")
	sleep(2)
	
	if item[0] == 'newspaper':
		print("The Space Cop, who's name is Sam, wants to buy the newspaper for 500 space credits")
		sleep(2)
		print(f"For your information, one space credit is 620 human dollars, which gives you ${500*620}\n") 
		sleep(2)
		choice = input("Do you want to sell your newspaper to Sam? y/n ")
		if choice == 'y':
			print("You sell Sam the newspaper")
			money += 500
			item[0] = 'nothing'
		else:
			print("you dont sell the paper and Sam walks away dejected.\n")
			sleep(2)
			print("You wonder why someone would pay so much for something so ordinary\n")
			sleep(2)
		
		print("You look in your space sachel, and now have a whole lot of",item[0])
		sleep(2)
		print(f"Checking your bank account at Zegumungs, you have {money} space credits\n")
		sleep(3)	
	else:
		print("The Space Cop sighs and keeps walking")
		sleep(10)
		clear()
		
	print("\n\n")
	clear()
	spacies(item, money)

def spacies(item,money): 

	print('''
	           ___
	     |     | |
	    / \    | |   Welcome to Spacies, the Macys of Space
	   |--o|===|-|
	   |---|   |d|
	  /     \  |w|	 How can I help on this spacy afternoon?
	 | U     | |b|
	 | S     |=| |
	 | A     | | |             You can buy four things here
	 |_______| |_|           1. Space Bob Ross wigs - 250 SC
	  |@| |@|  | |           2. Zero gravity carrots - 10 SC
	___________|_|_     3. One small package of gravity (1G) - 1 SC
	                        4. A talking space potato - 1.5 SC
	''')
		
	print("\n\n")
	
	choice = input("What do you want to buy? 0 to quit ")
	choice = int(choice)
	
	if choice == 1:
		if money > 250:
			sleep(2)
			print("You buy the best wig on the space station")
			sleep(2)
			print("While you dont like it, you want to keep your friends, and stay a fashion icon")
			item.append("bob ross wig")
			money -= 250
			sleep(2)
			print(f'You now have {item[1]} and {money} space credits, which is ${money*620}')
			sleep(2)
		else:
			print("You cant buy anything, youre broke")	
	elif (choice == 2) and (money > 0):
		print("You buy a package of zero gravity carrots")
		sleep(2)
		print("Space carrots are hard to eat in zero gravity, but you manage")
		sleep(2)
		print("It seems to all work out, even though there are now but of orange floating around the station")
		sleep(2)
		print("Refreshed by the delicous snack, you continue on your adventure")
		money -= 10
		print(f'You now have {item[1]} and {money} space credits, which is ${money*620}')
		sleep(2)
	elif (choice == 3) and (money > 0):
		print("You buy a small package of gravity")
		sleep(2)
		print("You feel slightly heavier, the gravity seems to be working")
		sleep(2)
		print("Gravity will help with your mime abilities, but you may need more to time travel")
		sleep(2)
		print("Dimensional travel is possible though... you may consider it...")
		money -= 1
		print(f'You now have {item[1]} and {money} space credits, which is ${money*620}')
		sleep(2)
	elif (choice == 4) and (money > 0):
		print("You buy a talking space potato")
		sleep(2)
		print("His name is Bill, and he is a potato. He is very annoying and screams all the time")
		sleep(2)
		print("You scream things like 'Do you want to be a baked potato?' and 'Quiet or I mash you'")
		sleep(2)
		print("But it does not seem to help and the screaming continues ")
		money -= 1.5
		print(f'You now have {item[1]} and {money} space credits, which is ${money*620}')
		sleep(2)
	else:
		print("You decide not to buy anything")
	
	option = input("Do you want to buy anything else?")
	
	if option == 'y':
		spacies(item,money)	
	
	option = input('You see a mime room, do you want to enter it?')
	
	if option == 'y':
		mime(item,money)
	else:
		dimensional(item,money)
		
	print("\n\n")
	sleep(4)

def dimensional(item,money):
	print('''
	You approach a big sign that says:
	Welcome to the dimensional portal - fun to teleport to other dimensions
	There is also a small sign that says "Caution: Some Danger may Apply"
	
	 .              +   .                .   . .     .  .
	                   .                    .       .     *
	  .       *                        . . . .  .   .  + .
	            "You Are Here"            .   .  +  . . .
	.                 |             .  .   .    .    . .
	                  |           .     .     . +.    +  .
	                 \|/            .       .   . .
	        . .       V          .    * . . .  .  +   .
	           +      .           .   .      +
	                            .       . +  .+. .
	  .                      .     . + .  . .     .      .
	           .      .    .     . .   . . .        ! /
	      *             .    . .  +    .  .       - O -
	          .     .    .  +   . .  *  .       . / |
	               . + .  .  .  .. +  .
	.      .  .  .  *   .  *  . +..  .            *
	 .      .   . .   .   .   . .  +   .    .            +
	
	
	''')
	sleep(2)
		
	print("Would you like to use the dimensional transporter?")
	sleep(2)
	choice = input(f"The transporter costs 1 SC ($620). Are you interested? y/n ")
	
	if choice == 'y':
		if money > 0:
			print("you decide to try the transporter")
			sleep(2)
		else:
			print("you dont have any money, but they do need mimes on Zergalon Alpha")
			sleep(2)
			print("they let you get on the transporter")
			sleep(2)
	else:
		print("While you dont want to go, it seems like you are forced to anyways")
		sleep(2)
	
	zerg(item, money)	


def zerg(item,money):
	
	print("You step on the transporter, and you are zapped to another dimension")
	
	print('''
	
	
	  ____                  _              _   _      _         
	 |_  /___ _ _ __ _ __ _| |___ _ _     /_\ | |_ __| |_  __ _ 
	  / // -_) '_/ _` / _` | / _ \ ' \   / _ \| | '_ \ ' \/ _` |
	 /___\___|_| \__, \__,_|_\___/_||_| /_/ \_\_| .__/_||_\__,_|
	   __      __|___/                     __   |_|       _     
	   \ \    / /__| |__ ___ _ __  ___ ___ \ \ / /__ _  _| |    
	    \ \/\/ / -_) / _/ _ \ '  \/ -_|_-<  \ V / _ \ || |_|    
	     \_/\_/\___|_\__\___/_|_|_\___/__/   |_|\___/\_,_(_)    
	                                                            
	''')			

def mime(item,money):
	print("You enter the mime room, look around, and see cupcakes.\n'Tis surprising. They are mint toothpaste. \nYou shudder in disgust, you have a strange feeling you might not like mint toothpaste.")
	sleep(2)
	choice = input("Would you like to buy a disgusting minttoothpaste cupcake? ")
	
	if (choice == 'y') and (money > 0):
		print("You buy a cupcake and do not enjoy it because it is mint toothpaste. Mint Toothpaste tastes like mosquitos.")
	else:
		print("You dont have any money to buy the mint toothpaste cupcake.")
	
	spacies(item, money)
	
def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
	
def nothing_room(item, money):
	print("You walk through a plain white door in a mysterious and extremely dark hallway. You're not even sure it was white.")
	sleep(2)
	print("You are in a very dark room with nothing. LITERALLY nothing.")
	sleep(2)
	print("Or are youuuuu?")
	sleep(2)
	print("a creepy guy comes out.")
	sleep(2)
	print("he says 'hello, human.'And you are just confused because you are obviously a space and time traveling mime.")
	sleep(2)
	print("he says 'Would you like a vegetable?' You can now see that he is blind.")
	sleep(2)
	print("He magicly pulls out a variety of vegetables.")
	sleep(2)
	choice = input("Would you like a vegetable? They are magic and will grow in your stomach. y/n ")
	
	if (choice == 'y') and (money > 0):
	  print("You snatch a vegetable and realize you do not have to pay for it because he is old and blind and will not notice you took a his purple carrot. You know this is mean of you, but you enjoy purple carrots.")
	  sleep (2)
	  print("You flee the room swiftly, and once you're out of the old man's earshot, you take a bite out of your purple carrot.")
	  sleep(2)
	  print("You hate it. It's mint toothpaste! How dare that WITCH...")
	  sleep(2)
	  print("You've been fooled. Tricked. And quite possibly, bamboozled.")
	  sleep(2)
	else:
	  print("You don't want a vegetable. They might be mint toothpaste and you don't want to waste any money.")
	  sleep(2)
	  print("You walk out of the room sighing and saying 'Nah.'")


def learning(item,money):
	print("You enter the learning rooms. After looking around you find a spellbook on the floor. ")
	sleep(2)
	choice = input("Would you like to pick it up? ")
	
	if (choice == 'y') :
		print("You attempt to pick up the book, but to pick up the book you must achieve a 15 for luck roll")
	else:
		print("You leave the book on the floor")
	
	input("Press enter to roll")
	
	d20 = random.randint(1,20)
	
	print(d20)
	
	if d20 > 14:
		print("You take the book, putting it into your satchel unscaved")
	else:
		print("The book vanishes in your hands, never being seen again")
	
	spacies(item, money)

def chicken(item,money):
	 pause(2)
	 
	 print("You drive over in your fancy space car to McSpacedonalds.")
	 choice = input("Would you like to buy [a] a Space Mac or [b] a Buttermilk Space chicken sandwich")
	 order_name = input("What is the name of the order")
	 
	 if choice == "a":
		 print("Yeet")

def dog(item,money):
	print("You enter the dog room, when you look around there are a few things that you see, you see a mean lookin chicken, and a few dogs in cages! One is a cute french bulldog")
	sleep(2)
	choice = input("Would you like to buy the cute frenchie?? ")
	
	if (choice == 'y') and (money > 0):
		print("You buy the frenchy and it bites the chickens head off as you walk past.")
	else:
		print("Why dont you have any money???")
	
	spacies(item, money)

def spacefarm(item,money):
	print("You find yourself in a room full of cows, pigs, sheep and goats.")
	sleep(2)
	print("The smell is terrible, but you don't notice very much because you've been stuck with gross people on the same space station for months.")
	sleep(2)
	print("As you make your way through the room, you notice a little goat eating hay in the corner.")
	
	choice = input("Would you like to steal the goat? He is VERY cute...")
	
	if (choice == 'y') and (money > 0):
		print("You stuff the goat in your backpack and make a run for it.")
	else:
		print("You probably don't want a goat anyway. They make funny noises and eat furniture.")
	
	spacies(item, money)
	
def fight(item,money):
	print("You enter the fighting room, you see there are all kinds of swords\n but only one seems to get your attention,\n it is all steel with a red handle.")
	sleep(2)
	print("you go up to examine the sword and the cool metal makes you feel alive.")
	sleep(2)
	choice = input("Would you like to buy the sword for 50 space credits?")
	
	if (choice == 'y') and (money > 49):
		money -= 50
		print("You buy the sword and and leave the room thinking that if you get attacked you can fight back")
	else:
		print("You decide that having a sword around will draw suspicion to you so leave the room empty handed.")
	
	spacies(item, money)	

def kill(item,money):
	print("You see a man who has just beaten up an elderly woman, do you either hit A, and kill the man, or do you quietly tell him to stop")
	choice = input("What do you choose? ")
	if choice == "A":
		print("the man sees you and shoots you with a BRWD, a bob ross wig dart and you fall to the groud wounded")
	else:
		print("the man gets scared and  drops the purse, you seethe money in it and decide to either A, try to find the woman, or B, and greedily steal it for your self ")

	choice = input("What do you choose? ")
	if choice == "C":
		print("you cant find the woman, so you decide to go to Spacies to try to find the women")
	else:
		print(" A space cop sees you and hauld you off t0 mime prison")
	
	spacies(item, money)

def bank(item,money):
	print("Welcome to Zegumungs")
	sleep(2)
	print("Banking for the Stars since Decalon Beta was Decalon Alpha!")
	sleep(2)
	
	office()
	
	while True:
		print(''' Welcome to Zegumungs!
				  This is what you can do at the bank:
				  0. Check your bank balance
				  1. Deposit Space Credits
				  2. Withdrawl Space Credits
				  3. Rob the bank
				  4. Buy the bank
				  ''')
		choice = input("Please pick an option")
		
		if choice == '1':
			print("You deicde to deposit SC")
			
		elif choice == '0':
			print("You check your bank balance")
		
		elif choice == '2':
			print("You deicde to withdrawl SC")
			
		elif choice == '3':
			print("You deicde to rob the bank")
		
		elif choice == '4':
			print("You deicde to buy the bank")
			print("The bank costs 10,000,000 SC, which is $",10_000_000 * 620)
			print("The bank asks you to make an offer for how much you want to pay")
			choice = input("How much do you offer to buy the bank?")
			choice = int(choice)
			
			if choice < random.randint(8_000_000,10_000_000):
				print("You are now the owner of the bank!")
			else:
				print("You do not buy the bank")
		else:
			print("Please pick a valid option")			
				  

def office(item,money):
	print('''
	 __________________________________________
|.'',        Welcome to the Bank          ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|???????|'|,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%Spicer%%%%%%\____________;|
	
	''')


def perform(item, money):
	print("You go to a fancy party hall and perform your mime routine for")
	print("the many assembeled guests")
	

def training(item, money):
  print("'See us next week, and see if you are prepared for your lightsaber, we shall.'")

  print("You enter a room with a sign above it stating 'FREE CUPCAKES'. You see Baby Yoda.. he walks up to you")
  sleep(2)
  print("'Train you to be a Jedi like E.T., I shall.' He says.")
  sleep(2)

  choice = input("Do you accept your training? Y or N.")
  if choice == 'N':
    print("E.T. is dissapointed. He thinks you may be a Sith. He jumps up from behind you and stabs you in the back with his orange lightsaber.")
    sleep(2)
    print("The medics come and E.T. claims he has nothing to do with your injury.")
    sleep(2)
    print("You are unconscious, but the medics frown and quickly put a fast-working healing serum on your wound.")
    sleep(2)
    print("E.T. and Baby Yoda high-five after the medics have dragged you out of the room ona stretcher. Another potential Sith defeated.")

  else:
    print("Baby Yoda happily smiles at you, an you can see E.T. in the dark hallway ahead nodding.")
    sleep(2)
    print("Baby Yoda leads you down the dark hallway, and E.T. joins him.")
    sleep(2)
    print("Baby Yoda looks up at you and says 'Now, your training begins, young Padawan.'")
    sleep(2)
    print("Young? YOUNG? you are obviously centuries old, as any space and time traveling mime is!")
    sleep(2)
    print("And Padawan? Pffttttt! What was this? the 347th century? You are a glorious bell, as your name states.")
    sleep(2)
    print("You should, quite obviously, be called and referred to as 'Master Mime', for that is who you are.")
    sleep(2)
    print("Only your closest friends could ever call you Isabel. Padawan? Why, you are so much more!")
    sleep(2)
    print("You roll your eyes and sigh.")
    sleep(2)
    print("E.T. complains to Baby Yoda in an entirely different language. One of the few languages unfamiliar to you.")
    sleep(2)
    print("'Brought you here to groan, I have not.' Why did Baby Yoda have to be so rude?")
    sleep(2)
    print("He tells you one last thing before sending you off...")
    sleep(2)
    print("'Next week, see us. Decide if you are yet worthy of a lightsaber, we then will.'")


def Tavern(item, money):
	print("You are about to enter the next room when a man is thrown out of the door. He is knocked unconscious.")

	choice = input("Do you search him for anything of value? y/n")
	if choice =='y':
		print("You search him and find 30 space credits in his space wallet.")
		money+=80
	else:
		print("You decide it's best not to search someone while they're knocked out. You never know if they will wake up as you're doing it.")
		print("You enter what is known as the stary sky tavern, the few patrons of the place already sat down and enjoying their drinks.")
		#print('When you walk in an employee of the tavern walked up to you, asking you "Hello') 
    #print('maam, what are you here for?')
    
def tavern_menu(item,money):
	""" THis is what this function is about"""
		
	print('''Your options are you can 
	 1. rent a room to rest(20SC). 
	 2. order a drink (Which costs 5SC) and 
	 3. order a meal (Which costs 10 SC)
	 4.You can even ponder why you are here''')
	
	choice=input("So what would you like? (press 0 to leave to another destination)")
	
	if choice == 1:
		if money > 19:
			print("You are handed a key, walking to the room that key unlocks. You lay down and rest")
		else:
			print ("You realize you don't have enough money and reconsider your choice")
		tavern_menu(item,money)
	
	elif choice == 2:
		if money > 4:
			print("You buy a drink, taking a seat and chugging it down. You would gain some kind of drunk status effect if I knew how to write one.")
		else:
			print("You realize you don't have enough money and reconsider your choice")
		tavern_menu(item,money)
	
	elif choice==3:
		if money > 14:
			print("You enjoy a hefty meal, devouring it. You can't remember the last time you ate, the last time you actually ate was a terrible mint chip muffin.")
		else:
			print("You realize you don't have enough money and reconsider your choice")
		tavern_menu(item,money)
	'''
	elif choice == 4:
    print("You say that you choose to ponder, the employee giving you something to ponder on and asks")
    print("You ever wonder why were here?")
		print("""You respond with"" It's one of life's great mysteries isn't it? Why are we here? I mean, are we the product of some cosmic coincidence, or is there really a God watching everything? You know, with a plan for us and stuff. I don't know, but it keeps me up at night.""")
		print("They just stare at you, a bit weirded out""No I mean at this station... so... is there anything you'd actually like?" ")
		tavern_menu(item,money)
    
    else:
      print("You decide to just leave and not do anything, leaving after saying goodbye")
		intro(item,money)'''


def bell_room(item,money):
	
	print("you enter a room with a sign above it saying the you will die room. You are but a small bell who is stupid enough to enter.")
	sleep(2)
	print("you go in and a voice says answer my riddle and you won't die")
	sleep(2)
	print("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
	sleep(2)
	print("a(n) what")
	sleep(2)
	
	choice = input("Make a choice")
	if choice == ' an echo':
		print('you have been spared and walk out of the room safely')
	else:
		print("you got it wrong you run for the door and somehow make it out safely but lost 3 fingers")

def miles(item,money):
	print("you fall into a hole of some kind and see lots of strange writing.")
	sleep(2)
	choice = input("do you traslate the writing? y/n ")
	
	sleep(2)
	if choice == 'y':
		print("you pull out you trusty transalator and hold it up to the writing. It translates to Joe Mamma")
	else:
		print("You climb out the hole and pretend nothing happend. You wounder why the writing looked familiar")


def trivia(item,money):
	counter = 1
	points = 0

	while True:
	    print("You have",points,"points")
	
	    triviaurl = 'https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple'
	    response = urllib.request.urlopen(triviaurl)
	    result = json.loads(response.read())
	    #print(result)
	
	    questions = []
	    questions.append(result["results"][0]["correct_answer"])
	    for wrong in result["results"][0]["incorrect_answers"]:
	        questions.append(wrong)
	    random.shuffle(questions)
	
	    print("Question",counter)
	    counter += 1
	    print(result["results"][0]["question"])
	    print("Your options are:")
	    for item in questions:
	        print(item)
	
	    choice = input("What is your answer?")
	
	    if choice.lower() == result["results"][0]["correct_answer"].lower():
	        print("You are right!")
	        points += 1
	        money += 5
	    else:
	        print("You are wrong")
	        print("The correct answer is:",result["results"][0]["correct_answer"])
	        print("You lose 2 SC")
	        print(f"You have {money}SC")
	        points -= 1
	        money -= 2
	
	    choice = input("Play again? y/n")
	
	    if choice == 'n':
	        break
	        intro(item,money)
   		
intro(item,money)

















	


		
