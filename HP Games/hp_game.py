#importing the time module
import time


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\tA JOURNEY OF OPTIONS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

coin = 0
life = 7
briefcase = []
line = ""

def intro():                                                          #defining a function with name intro
    print("What is your first name?")                                 #user input firstname
    firstname = input(">>> ")
    print("What is your last name?")                                  #user input last name
    lastname = input(">>> ")
    print("")
    welcome(firstname,lastname)                                       #calling the last function

def welcome(firstname,lastname):            #defining function with arguments
    	print("To " + firstname +" "+lastname+", ")
    	print("")
    	print("We are pleased to inform you that you have been accepted in Hogwarts School of Wizcraft and Wizardy \U0001f600.")
    	time.sleep(1)
    	print("\nWe have sent you a list of neccessary equipments that you should carry. ")
    	time.sleep(1)
    	print("\nYou have to board the train at Station from Platform 9 3/4")
    	time.sleep(1)
    	print("\nI look forward to see you in the campus.")
    	time.sleep(1)
    	print("")
    	print("\nFrom : ")
    	time.sleep(1)
    	print("Deputy Headmistress")
    	time.sleep(1)
    	print("Hogwarts School of Witchcraft and Wizardry")
    	time.sleep(0.5)
    	print("")
    	print("Do you accept? (y/n)")                                      #user input for choice
    	accept = input(">>> ")
    	if accept == "y":                                                  #if y go to next function
    	    Stage1(firstname)
    	elif accept == "n":
		    Misschance()


def Misschance():                                                          #end function
	sure = input("Are you sure? y/n ")
	if sure == "n":
		Stage1()
	else:
		print("So you don't want to go to Hogwarts, huh? You miss a lifetime experience.")
		Exit()


def Exit():                                                               #exit function
    print("Are you sure you want to exit the game? (y/n)")
    exit = input(">>> ")
    time.sleep(2)
    if exit == 'y':
        print("Come back again if you change your mind. Bye. ")
        print("\U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600")      #assigning emoji

    else:
        intro()



def Stage1(firstname):
    print("")
    print("Great! Welcome aboard " + firstname + " now that you have accepted the offer, ")
    time.sleep(2)
    print("you need to earn coins for your school shopping.")
    time.sleep(2)
    print("You can get some magic coins by fulfilling different goals and missions in order to receive rewards.")
    time.sleep(2)
    print("These rewards can be earned by completing a Mystry test")
    time.sleep(2)
    print("For each correct answer you will earn 20 magic coins which you will use for your shopping.")
    time.sleep(1.5)
    print("Are you ready for the test? (y/n)")
    accept = input(">>> ")
    if accept == "y":
        game1(coin)
    elif accept == "n":
        print("\n You cannot proceed further without taking the test?")
        time.sleep(1.5)
        print("So, are you ready for the test? (y/n)")
        accept = input(">>> ")
        game1(coin)

def game1(coin):
    print("Answer the statement in true or false: ")
    print ("\n In space, you cannot cry.")
    choice = input(">>> ")
    if choice == 'true':
        coin += 20 #If correct, the user gets twenty coin
    else:
        coin += 0
    print ("\nThere is no word that rhymes with Orange.")
    choice = input(">>> ")
    if choice == 'true':
        coin += 20
    else:
        coin += 0

    print ("\nA sneeze is faster than an eye blink")
    choice = input(">>> ")
    if choice == 'true':
        coin += 20

    print ("\nFingernails grow faster than hair")
    choice = input(">>> ")
    if choice == 'false':
        coin += 20

    print ("\nA rabbit eats its own poops")
    choice = input(">>> ")
    if choice == 'true':
        coin += 20
    else:
        coin += 0
    print ("\nBravo you have finished the test. You got " + str(coin) + " coins out of 100")
    time.sleep(1)
    print("Here is a wallet for you to hold the coins.")
    time.sleep(2)
    print(f" \n Happy Shopping! ")
    print("\U0001F911 \U0001F911 \U0001F911 \U0001F911 \U0001F911 \U0001F911 ")
    briefcase.append('wallet')
    time.sleep (1.5)
    Shop1()

def Shop1(): #to buy wand

	print("\nYou travel to Diagon Alley to do your school shopping.")
	time.sleep(0.8)
	print("Do you know where to find your wand?")
	print("")
	print("A. Weasley's Shop")
	print("B. Gamphor's Wands")
	print("C. Ollivanders: Makers of Fine Wands since 305 B.C.")
	print("")
	wandshop = input("A, B, or C? ")
	if wandshop == "A":
		print("\nOops!! Weasley's Shop isn't in Diagon Alley \U0001F606 ")
		time.sleep(3)
		Shop1()
	elif wandshop == "B":
		print("\nGamphore's Wands isn't in Diagon Alley, Silly!")
		time.sleep(3)
		Shop1()

	elif wandshop == "C":
		print("You're headed on the right track to be a great witch or wizard.")
		print("\U0001f600")
		time.sleep(3)
		Wand(coin)

#red is a comment
def Wand(coin):
	print("Welcome to Ollivander's Wand Shop!!!")
	print("")
	print("Are you most:")
	print("A. Kind and Generous")
	print("B. Tenacious")
	print("C. A good leader")
	print("D. Full of life")
	print("")
	wood = input(">>> ")
	print("")
	if wood == "A":
		print("You recieve an Ash Wand, 13 4/17 inches, with a Unicorn Tail Hair core.")
		print("")
		briefcase.append('wand')
		coin += -10
		print(f"You spent 10 coins on your wand. \nYou have {briefcase} in your briefcase now.")
		time.sleep(1)
		Shop2()

	elif wood == "B":
		print("You receive an Ivy Wand, 9 2/9 inches, with a Dragon Heartstring core.")
		print("")
		briefcase.append('wand')
		print(f"You spent 10 coins on your wand . You have {briefcase} in your briefcase now.")
		time.sleep(1)
		Shop2()

	elif wood == "C":
		print("You receive a Holly Wand, 11 1/2 inches, with a Phoenix Feather core.")
		print("")
		briefcase.append('wand')
		print(f"You spent 10 coins on your wand . You have {briefcase} in your briefcase now.")
		time.sleep(1)
		Shop2()

	elif wood == "D":
		print("You receive a Birch Wand, 10 3/4 inches, with a Dragon Heartstring core.")
		print("")
		time.sleep(5)
		briefcase.append('wand')
		print(f"You spent 10 coins on your wand . You have {briefcase} in your briefcase now.")
		time.sleep(1)
		Shop2()

def Shop2():
    print("\nWhere do you want to go next?")
    time.sleep(2)
    print("A. To buy uniform")
    print("B. To buy books")
    print("C. Go to Platform")
    shop = input(">>>")
    if shop == "A":
        Uniform(coin)
    elif shop == "B":
        print("You will get all your books at Hogwarts Library.")
        Shop2()
    else:
        Station()

def Uniform(coin):
    print("\nWelcome to Madam Malkin's Robes for All Occasions Shop.")
    print("")
    print("\nAre you a first year student at Hogwarts? (y/n)")
    time.sleep(0.5)
    choice = input(">>>")
    if choice == "y":
        print("Perfect! Let me get you your uniform.")
        time.sleep(1.5)
        print("Here it is:\nOne winter cloak.\nThree sets of plain work robes.\nOne plain pointed hat for day wear.\nOne pair of protective gloves.")
        time.sleep(1)
        briefcase.append('uniform')
        print(f"You spent 20 coins in your uniform! Now you have {briefcase} in your briefcase.")
        time.sleep(5)
        Station()
    else:
        print("Dont lie to her! ")
        Uniform(coin)

def Station():
    print("\n Now you need to get onto the platform")
    print("")
    print("\n \t WELCOME TO PUBLIC STATION.")
    time.sleep(1)
    print("")
    print("\nDo you know how to get to Platform 9 3/4?")
    print("A. Cast a spell to reach Hogwarts")
    print("B. Run at the barrier between platforms nine and ten")
    print("C. Fly a car to Hogwarts.")
    print("")
    platform = input(">>> ")
    if platform == "A":
        print(f"You have not learn to cast a spell yet. Silly!")
        time.sleep(1.5)
        Station()
    elif platform == "B":
        print("Wow, that was a nice run.You make it onto the platform.")
        time.sleep(1)
        print("Get ready to board the train.")
        time.sleep(5)
        HogwartsExpress()
    elif platform == "C":
        print("You don't own a flying car yet. Sorry!")
        time.sleep(1.5)
        Station()

def HogwartsExpress():
    print("\n\tHOGWARTS EXPRESS")
    print("\nHogwarts Express welcomes all the students on board. Safe travels!! ")
    print("\nYou sit in a compartment and make friends with a boy and a girl who call themselves Luna and Felix.")
    time.sleep(2.564)
    print(f"You introduce yourself and starts talking with them")
    time.sleep(1.78)
    print(f"\n Felix: Hello, nice meeting you. Which Hogwarts house do you want to be? ")
    time.sleep(1.876)
    print("\nYou answer....")
    print("A. Gryffindor, bravest of the Hogwarts Four")
    print("B. Hufflepuff, fairest of the Hogwarts Four")
    print("C. Ravenclaw, clever of the Hogwarts Four")
    print("D. Slytherin, greatest of the Hogwarts four")
    print("")
    houses = input("A, B, C or D? >>>")
    if houses == "A" or "B" or "C" or "D":
        print("Luna: Sounds cool.Now I can't wait to reach Hogwarts. ")
        time.sleep(2.87654)
    Sortinghat()

def Sortinghat():
    print("\nIn the misty moonlight, you reach the beautiful Great Hall")
    time.sleep(2.456)
    print("of Hogwarts for the Welcoming Feast.")
    time.sleep(4)
    print("The room is filled with Hogwarts students, Hogwarts Staff and Hogwarts Ghost.")
    time.sleep(4)
    print(".... and there you hear the voice of an man speaking.")
    time.sleep(4)
    print("\nAlbus Dumbeldore: The very best of evenings to you!")
    time.sleep(3)
    print("Welcome to our new students, welcome, to our old students!")
    time.sleep(3)
    print("Another year full of magical education awaits you.")
    time.sleep(3)
    print("\nLET THE SORTING HAT CEREMONY BEGIN!!!")
    print("")
    time.sleep(3)
    print("________________________________________")
    print("\nThe ceremony's purpose is to assign first years to one of the four")
    print("school Houses: Gryffindor, Hufflepuff, Ravenclaw, or Slytherin.")
    print("It is done through the use of the famous Hogwarts Sorting Hat. The Sorting Hat's ")
    print("decision is final.")
    print("_________________________________________")
    time.sleep(5)

    print("The Sorting Hat started calling out students names.")
    time.sleep(2)
    print("\n")
    print("")
    print("Young, Laura")
    print("Hat: Griffindor!")
    time.sleep(3)

    print("\n")
    print("Weasley, Fred")
    time.sleep(2.6785)
    print("Hat: Ravenclaw!")

    print("")
    time.sleep(1.34)
    print(f"Hat: Hello there ")
    time.sleep(3)
    print("Do you pride yourself on your")
    print("")
    print("A. Benevolence")
    print("B. Intelligence")
    print("C. Courageousness")
    print("D. Knavishness")
    print("")
    pride = input(">>> ")
    if pride == "A":
        house = "Hufflepuff!"
    elif pride == "B":
        house = "Ravenclaw!"
    elif pride == "C":
        house = "Gryffindor!"
    elif pride == "D":
        house = "Slytherin!"
    print("Congratulations on being sorted into " + house)
    time.sleep(5)
    Welcomefeast()

foodchoice = ""
def Welcomefeast():
	print("\nNow that you have completed the Sorting Hat ceremony you")
	time.sleep(3)
	print("approch to the dining hall for lunch")
	time.sleep(3)
	print("\nThe tables are piled high with all sorts of fancy food. And after")
	time.sleep(3)
	print("such a long day, you surely must be hungry.")
	time.sleep(5)
	menu = """
	Here is your menu:

	Butterbeer Cupcakes
	Cheese and Pretzel Broomsticks
	Treacle Tart
	Chocolate Golden Snitches
	Shepherd's pie
	Firewhisky
	Pumpkin Pasties
	"""
	print(menu)
	time.sleep(2)
	print("")
	print("What do you want to eat? Please type...")
	food = input(foodchoice)

	print("You indulge in " + food + " and enjoy them greatly.")
	time.sleep(3)
	print("\nNow its time for you to get some rest and prepare yourself for your first class!")
	time.sleep(3)
	print("\U0001f6cc\U0001f634\U0001f4a4\U0001f6cc\U0001f634\U0001f4a4\U0001f6cc")
	Day1()

def Day1():
    print("\n \t Welcome to Day 1 at Hogwarts")
    time.sleep(2)
    print("\nYou woke up to a beautiful morning, all refreshed and excited about the day in front of you.")
    time.sleep(2)
    print("You have your first charms and defence class. ")
    time.sleep(2)
    print("\nHow do you want to get there?")
    print("")
    print("A. Through the passage beneath a one-eyed witch statue")
    print("B. Through the passage behind a talking mirror")
    print("C. Through the passage under the Whomping Willow")
    print("")
    path = input("A, B, or C? >>>")                                            #user input for options
    if path == "A" or "B" or "C":
        print("Intresting!! But the passage to your first class is not so easy.")
        time.sleep(2)
        print("\nYou entered the Hangman Dungeon full of Dementors.")
        time.sleep(2)
        print("You have to play a game to open the doors to your class")
        print("\n Are you ready for it? (y/n)")
        choice = input(">>>")
        print("")
        if choice == 'y':
            Hangman()
        else:
            print("There is no way out once you are in. Win or Die ")
            time.sleep(2)
            print("Don't be sacred...")
            Hangman()


def Hangman():                                                              #defining function hangman
    print("\nOh hello there, I see you got stuck on your way to class.")
    time.sleep(2)
    print("\nI am Bagwig, the keeper of this dungeon. Inside you will play a game")
    time.sleep(0.5)
    print("of Hangman. If you lose the game, ")
    time.sleep(0.5)
    print("and the dementors will eat you...... ")
    time.sleep(2)
    print("\n The game starts in ........")
    time.sleep(4)
    print("3")
    time.sleep(4)
    print("2")
    time.sleep(4.6543)
    print("1")
    time.sleep(4)

    print("")

    #wait for 1 second
    time.sleep(1)

    print("Start guessing a word/letter that best fit the blank...")
    time.sleep(0.5)

    #here we set the secret
    word = "butterbeeracromantula"

    #creates an variable with an empty value
    guesses = ''

    #determine the number of turns
    turns = 10

    # Create a while loop

    #check if the turns are more than zero
    while turns > 0:

        # make a counter that starts with zero
        failed = 0

        # for every character in secret_word
        for char in word:

        # see if the character is in the players guess
            if char in guesses:

            # print then out the character
                print(char)

            else:

            # if not found, print a dash
                print ("_")

            # and increase the failed counter with one
                failed += 1

        # if failed is equal to zero

        # print You Won
        if failed == 0:
            print("\nWonderful!! Alohomora let the doors open")
            time.sleep(2)
            print("\nYou made it to your class. Study hard! ")
            time.sleep(3)
            print("""\
                                                   _   _
                                           | | | |
  _   _  ___  _   _  __      _____  _ __   | | | |
 | | | |/ _ \| | | | \ \ /\ / / _ \| '_ \  | | | |
 | |_| | (_) | |_| |  \ V  V / (_) | | | | |_| |_|
  \__, |\___/ \__,_|   \_/\_/ \___/|_| |_| (_) (_)
   __/ |
  |___/                                            """)


        # exit the script
            intro()

        print("\nGuess a word/letter")
        guess = input(">>>")    # ask the user go guess a character

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:

        # turns counter decreases with 1 (now 9)
            turns -= 1

        # print wrong
            print ("oops! that a wrong move.")

        # how many turns are left
            print ("\nYou have", + turns, 'more life left' )

        # if the turns are equal to zero
            if turns == 0:

            # print "You Lose"
                print ("\nYou cannot make it to the class.")
                time.sleep(2)
                print("""\
 __     __                     _                 _
 \ \   / /                    | |               | |
  \ \_/ /    ___    _   _     | |   ___    ___  | |_
   \   /    / _ \  | | | |    | |  / _ \  / __| | __|
    | |    | (_) | | |_| |    | | | (_) | \__ \ | |_
    |_|     \___/   \__,_|    |_|  \___/  |___/  \__|

                                                       """)


while True:
    intro()


##################################################################################
#REFERENCE:
#1. https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman
#2. https://harry-potter-sorting.itbarsoum.repl.run/
#3. https://repl.it/@itbarsoum/harry-potter-text-adventure
