import time

suspects = ['Mr. Bent','Ms. Stoon','Mrs. Locks']

name = input("Welcome to the mystery, detective. What is your name? ")

def intro(name=''):
	print('''
	
		      `'::::.          
	        _____A_               
 	       /      /\             
	    __/__/\__/  \___             
	---/__|" '' "| /___/\----          
	   |''|"'||'"| |' '||            
	   `""`""))""`"`""""`           
		
	''')
	print("Welcome Detective",name.title())
	time.sleep(3)
	print("You had been planning on going to the house, but..")
	time.sleep(3)
	print("Why does everyone seem so worried?")
	time.sleep(3)
	print("Has something happened here?") 
	time.sleep(3)
	print("You get a very bad feeling that something is wrong")
	time.sleep(3)
	
	print("You can gather [w]ho is at the house, or check the [f]lower beds outside")
	choice = input("Pick an option ")
	
	if choice == 'w':
		time.sleep(1)
		print("There are several people at the house")
		time.sleep(1)
		print(f'{suspects[0]},{suspects[1]},{suspects[2]}')
		time.sleep(1)
	else:
		time.sleep(1)
		print("You go outside and check out the flowers and find nothing interesting")
		time.sleep(1)
		intro()	
	
	choice = input(f'{name.title()}, would you like to [c]ontinue or [g]o home? ')
	time.sleep(1)
	
	if choice == 'c':
		print("You go in and see Mrs. Cortez on the floor")
		investigate()
	else:
		print("You decide to go home because mysteries are not your thing")
		intro()	

def investigate(name=''):
	print('You choose to investiate the room and take a look around')
	time.sleep(3)
	print('You notice that there are smashed teacups on the floor next to the body of Mrs. Cortez')
	time.sleep(3)
	print('you also notice some footprints')
	time.sleep(3)
	print('You go back to the living room')
	livingroom()
	
def livingroom(name=''):
	print('You can now interview your three suspects')
	print('Who do you want to interview?')
	print(f'''
	Press 1 for {suspects[0]}
	Press 2 for {suspects[1]}
	Press 3 for {suspects[2]} 
	''')
	choice = input("Pick an option ")
	if choice == 1:
		bent()
	elif choice == 2:
		stoon()
	else:
		lock()
	
def bent(name=''):
  print('mr Bent was the best painter in town he paints oaintings for mrs. Cortez.')
  print('\mrs. Cortezs home is actually his childhood home.')

def stoon(name=''):
  print('Ms. Stoon was the cook for mrs. Cortez.')
  print('She usually serves her tea.')

def locks(name=''):
  print('Mrs. LOcks is the maid for Mrs. Cortez.')
  print('She cleans and tidies rooms in the big mansion.')

def kitchen(name=''):
  print('You bringn every one in to the room.')
  time.sleep(3)
  print('you are to ask a question to reveal the murder.')
  time.sleep(3)
  print('What question should you ask?')
  time.sleep(3)
  print('a) Who murdered her!? or b) Who gave her tea this morning?')
  choice = input ("pick an option.")
  if choice == 'a':
    print('No one answers. YOU LOSE.')
  elif choice == 'b':
    print('Ms. Stoon breaks out in tears. She admitts she done it.')
    time.sleep(3)
    print('Mrs. Cortez had been planning a dinner party for a while.')
    time.sleep(3)
    print('She never invited her. So Ms. Stoon poisened her tea.')
    time.sleep(3)
    print('Congrats! You caught the murderer! YOU WIN.')

intro(name)

