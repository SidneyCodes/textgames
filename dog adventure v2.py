import time
import random

clean = False
money = 0
health = 100


def intro():
    print("Welcome to a day in the life of a dog")
    time.sleep(2)
    name = input("Hello dog, what is your name? ")
    time.sleep(2)

    while True:
        money = 1

        try:
            money = int(money)
            break
        except ValueError:
            print("Please enter a number")

    school(name,money,health,clean)


def school(name,money,health,clean):
    print(f"{name.title()}, you are at dog school, learning all kinds of important things")
    print("You have this many bones", money)
    time.sleep(2)
    print("You can start the game over [1], or [2] go to the store ")
    choice = input("Where do you want to go next?")
    time.sleep(2)
    if choice == '1':
        intro(name,money,health,clean)
    else:
        print("You go to the store")
        time.sleep(2)
        store(name,money,health,clean)


def store(name,money,health,clean):
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
        school(name,money,health,clean)
    elif choice == '2':
        vet(name, money, health, clean)
    elif choice == '3':
        grooming(name,money,health,clean)
    elif choice == '4':
        print("Thanks for playing the game, goodbye")
    else:
        print("Please pick a valid option")
        store(name,money,health,clean)


def vet(name, money, health, clean):
    print("You are at the vet")
    if clean == False:
        print("You cant go to the vet dirty!")
        grooming(name, money, health, clean)

    time.sleep(2)

    print(f"{name.title()}, you get a bunch of needles are not not happy")
    print(f'You have {health}% health')
    print(f'You have {money} bones\n')
    time.sleep(2)
        
    health += random.randint(50,100)
    print("The vet makes you feel all better")
    #print(f'You have {health}% health')
    
    if health >= 100:
        health = 100
        print("The vet fixes you up and you are at max health")
    
    print("""\t\t\nYou now have choices:
             [1] go to the store
             [2] go to grooming
             [3] go look to fight a squirrel
             [4] to quit""")
    choice = input("Please pick an option ")
    if choice == '1':
        store(name,money,health,clean)
    elif choice == '2':
        grooming(name,money,health,clean)
    elif choice == '3':
        fight(name,money,health,clean)
    elif choice == '4':
        print("Thanks for playing the game, goodbye")
    else:
        print("Please pick a valid option")
        vet(name,money,health,clean)


def grooming(name,money,health,clean):
    print("You are at grooming")
    time.sleep(2)
    print("They comb your fur and you now smell nice")

    clean = True

    print("""\t\t\nYou now have choices:
             [1] go to the vet
             [2] go to store
             [3] to quit""")
    choice = input("Please pick an option ")
    if choice == '1':
        vet(name,money,health,clean)
    elif choice == '2':
        store(name,money,health,clean)
    elif choice == '3':
        print("Thanks for playing the game, goodbye")
    else:
        print("Please pick a valid option")
        grooming(name,money,health,clean)


def checkwin(name,money,health,clean):
    if money == 25:
        print("You win! You got to the max")
        time.sleep(2)
        print("Enjoy your lifetime supply of bones!")
        time.sleep(2)
    else:
        fight(name,money,health,clean) 


def fight(name,money,health,clean):
    health = 100
    level = 0

    time.sleep(2)
    print("You see a scary squirrel, get ready for...")
    time.sleep(2)
    print("Squirrel Mania!")
    time.sleep(2)
    
    main_fight(name,money,health,clean,level)
    
def main_fight(name,money,health,clean,level):
    
    while True:
        print("\nThis is level", level)
        print(f'You have {health}% health')
        print(f'You have {money} bones\n')

        time.sleep(2)

        dog = random.randint(1, 10)
        squirrel = random.randint(1, (10 + level))

        if dog == squirrel:
            print("\nIts a tie and nothing happens\n")
            print(f'You have {health}% health')
            print(f'You have {money} bones\n')
        elif squirrel > dog:
            print("\nThe squirrel does something crazy and wins\n")
            health -= level
            print(f'You have {health}% health')
            print(f'You have {money} bones\n')
            print(f'You are now very dirty')
            clean = False
        else:
            print("\nYou win and beat the silly squirrel!\n")
            money += level
            print(f'You have {health}% health')
            print(f'You have {money} bones\n')
            
        level += 1
        
        if health < 25:
            print("You should really go to the vet")

        if money >= 25:
            c2 = 1
            while True:
                print("You win the game!"*c2)
                c2 += 1
                time.sleep(0.1)
            if c2 == 500:
                break        

        choice = input("\nDo you want to play again? y/n \n")

        if choice == 'n':
            vet(name,money,health,clean)
        else:
            main_fight(name,money,health,clean,level)    


intro()

print('''

   ___                 ___              _
  / __|__ _ _ __  ___ / _ \__ _____ _ _| |
 | (_ / _` | '  \/ -_) (_) \ V / -_) '_|_|
  \___\__,_|_|_|_\___|\___/ \_/\___|_| (_)


''')

