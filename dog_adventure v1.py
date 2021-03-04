import time

def intro():

    print("Welcome to a day in the life of a dog")
    time.sleep(2)
    name = input("Hello dog, what is your name? ")
    time.sleep(2)

    while True:
        money = input("How much dog money do you want? ")

        try:
            money = int(money)
            break
        except ValueError:
            print("Please enter a number")

    school(name,money)

def school(name,money):
    print(f"{name.title()}, you are at dog school, learning all kinds of important things")
    print("You have $", money)
    time.sleep(2)
    print("You can start the game over [1], or [2] go to the store ")
    choice = input("Where do you want to go next?")
    time.sleep(2)
    if choice == '1':
        intro()
    else:
        print("You go to the store")
        time.sleep(2)
        store(name)

def store(name):
    print("You are in the store")
    time.sleep(2)
    print("You buy a bunch of stuff, and are very happy")
    print("""\t\t\nYou now have choices:
             [1] go to school
             [2] go to the vet
             [3] go to the groomer
             [4] to quit""")
    choice = input("Please pick an option ")
    if choice == '1':
        school(name)
    elif choice == '2':
        vet(name)
    elif choice == '3':
        grooming(name)
    elif choice == '4':
        print("Thanks for playing the game, goodbye")
    else:
        print("Please pick a valid option")
        store(name)

def vet(name):
    print("You are at the vet")
    time.sleep(2)
    print("You get a bunch of needles are not not happy")
    print("""\t\t\nYou now have choices:
             [1] go to the store
             [2] go to grooming
             [3] to quit""")
    choice = input("Please pick an option ")
    if choice == '1':
        store(name)
    elif choice == '2':
        grooming(name)
    elif choice == '3':
        print("Thanks for playing the game, goodbye")
    else:
        print("Please pick a valid option")
        vet(name)

def grooming(name):
    print("You are at grooming")
    time.sleep(2)
    print("They comb your fur and you now smell nice")
    print("""\t\t\nYou now have choices:
             [1] go to the vet
             [2] go to store
             [3] to quit""")
    choice = input("Please pick an option ")
    if choice == '1':
        vet(name)
    elif choice == '2':
        store(name)
    elif choice == '3':
        print("Thanks for playing the game, goodbye")
    else:
        print("Please pick a valid option")
        grooming(name)



intro()

print('''

   ___                 ___              _
  / __|__ _ _ __  ___ / _ \__ _____ _ _| |
 | (_ / _` | '  \/ -_) (_) \ V / -_) '_|_|
  \___\__,_|_|_|_\___|\___/ \_/\___|_| (_)


''')
