import random
import time

time.sleep(2)
print('''


  ___                   ___ _               
 / __|_ __  __ _ __ ___/ __| |_ __ _ _ _ ___
 \__ \ '_ \/ _` / _/ -_)__ \  _/ _` | '_(_-<
 |___/ .__/\__,_\__\___|___/\__\__,_|_| /__/
     |_|                                    


''')

print("This is a game where Space happens")
time.sleep(2)
print("This is a game about stars")
time.sleep(2)
print("This is a game on how to get to Mars!")
time.sleep(2)

progress = 0
target = 5000

while True:
	print("How far do you want to go?")
	choice = input("Please enter a number of miles from 1-250 ")
	choice = int(choice)
	
	if choice > 250:
		choice = 250
	elif choice <= 0:
		choice = 1
		
	chance = random.randint(1,250)
	
	if choice > chance:
		print("You move forward",choice,"miles")
		progress += choice
	else:
		print("You move back",choice,"miles")			
		progress -= choice
		
	print("You are at",progress,"miles of",target,"miles")	

	if progress == target:
		print("You win!")
		break
		
	if chance > 200:
		print("\nYou have been attached by Space Cats!")
		progress -= 100
		print('乁། ˵ ◕ – ◕ ˵ །ㄏ\n')
	
	if chance > 250:
		print("Space boost!")
		progress += 100	
		
print('''


 __   __         __      ___      _ 
 \ \ / /__ _  _  \ \    / (_)_ _ | |
  \ V / _ \ || |  \ \/\/ /| | ' \|_|
   |_|\___/\_,_|   \_/\_/ |_|_||_(_)
                                    


''')		
#http://patorjk.com/software/taag/#p=display&f=Small&t=You%20Win!
#https://www.asciiart.eu/space
