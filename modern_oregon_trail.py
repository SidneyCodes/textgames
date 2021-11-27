import time
import random
from os import system, name


total_miles = 0
medpacks = 0
booster = 1
golden_booster = 0
helth = 10
day = 1
spacecredits = 100
sickness = False
death=False
hunger = 10
food = 1
tip = "Here's a tip, type sc which to view your total space credits for every 10000 miles you travel you earn 500 Spacecredits from your sponsor. Cool right?\n"

name = input("What is your name? ")


def intro(name='',spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10):
    print(f"\n\tWelcome {name}\n")
    print("You are in space\n")
    time.sleep(2)
    print("You need food, water as well as medicine to survive\n")
    time.sleep(3)
    print(
        "The total journey will take over 2,000,000 miles and you travel 500 miles per day both lowering your food, water as well as your medicine if you get sick\n")
    time.sleep(3)

    print("there are 3 menus: The pharmacy where you can get all your medical needs.\n")
    time.sleep(3)
    print("The Future Mcdonalds are where you can get food & water for a low cost.\n")
    time.sleep(3)
    print(
        "And finally we have the booster store after every 20 days or 10000 miles you will have to buy booster or you can take a chance to last 3 extra days or have a chance of blowing your self up and dying which nobody wants so I recommended buying the booster\n ")
    time.sleep(4)
    print(
        "There a small chance of you getting a golden booster beside looking good it also gives you 30 days or 15000 miles before it has to be changed.\n")
    time.sleep(4)
    print(
        "All the prices in all the shop come with a description and cost with the universal credits, spacecredits. That sould be about it, Good luck \n")
    time.sleep(4)
    main(name, tip,spacecredits='', food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10)


def main(name='', tip='',spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10):
    ready = input(
        f"I know it might be a lot to take in, so take your time reading the paragraphs above thoroughly. Are you ready for your adventure {name} ? Y or y ")
    if ready == 'Y' or 'y':
        print(tip)
        time.sleep(4)
        print(
            f"Alrighty let get your spacesuit on {name} and get into the spaceship and we are lanching in 10,\n 9,\n 8,\n7,\n 6,\n 5,\n 4,\n 3,\n 2,\n 1\n and we have ignition\n")
        print('your spaceship hurls into the darkness as you exit low earth orbit and into space\n')
        time.sleep(4)
        print('You see the black inky darkness of space and the sun shining brightly\n')
        time.sleep(5)
        print(
            f"Sudenly you see a red light flash on your screen there a warning saying that you need to start your journey right now or you won't reach in time, I guess you better start moving {name}\n")
        menu(spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10)

def travel(spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=10,helth=10):
  while death == False:
    if hunger == 0:
        health = 0
        print(f'you are now starving {name}, good game ..... say your goodbye as you go toward the light')
    
    if health == 0:
        death = True
        print("you died next time try to use your food and water when you really need it")
        break
    else:
        print("type store to go to the store, travel, sc or eat")
        choice = input("Pick an option: store, travel, eat or sc ")
        if choice == 'store':
            store()
        elif choice == "travel":
            total_miles += 500
            hunger -= 1
            print(
                f"you have now traveled {total_miles} miles and you have {hunger} hunger points left, remember to eat if you hunger is lower than 3")
        elif choice == 'eat':
            food -= 1
            hunger += 10
            print(f"""{name} now has {hunger} hunger points and {food} burgers and fries left""")
            if food <= 0:
                print('You are out of food')
        elif choice == 'sc':
            print(f"you have a balence of {spacecredits} credits remember to spend it wisely ")
            print(tip)


def store(spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10):
    print(f"you have {spacecredits}")
    print('''
  This is the Menu
  f for Food
  m for Med Packs
  b for Booster store
  q to Quit
  ''')
    buy = input("What would you like to buy? ")
    if buy == "f":
        food += 10
        spacecredits -= 50
        print(f"You now have {spacecredits} spacecredits and now {food} burger and fries combos")
        store()
    elif buy == 'm':
        print('Welcome to the pharmacy')
        medpacks += 1
        spacecredits -= 200
        print(f"You now have {spacecredits} spacecredits and now {medpacks} medpacks")
        store()
    elif buy == 'b':
        print('Welcome to the booster store')
        if booster or golden_booster >= 2:
            print("You can only have one booster at a time")
        else:
            chance = random.randint(1, 10)
            if chance == 3:
                print(
                    'Omg, you got our golden booster, congrats my man or woman you now can last 30 days before you need to get it changed.')
                golden_booster += 1
                spacecredits -= 200
                print(
                    f"You now have {spacecredits} spacecredits and now {booster} {golden_booster} booster. Note: you can only have 1 booster at a time")
            else:
                booster += 1
                print(
                    f"You now have {spacecredits} spacecredits and now {booster} booster. Note: you can have 1 booster at a time")

        while death == False:
            if hunger == 0:
                helth = 0
                print(f'you are now starving {name}, good game ..... say your goodbye as you go toward the light')
                if helth == 0:
                    death = True
                    print("you died next time try to use your food and water when you really need it")
                    
def menu(spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10):
  while True:
    choice = input("1. Store, 2. Travel 3. Eat Space McDonalds ")
    if choice == '1':
      store(spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=0,helth=10)
    elif choice == '2':
      travel(spacecredits=0, food=0, medpacks=0, booster=0, golden_booster=0,death=False,hunger=10,helth=10)
    else:
        print("Please pick a valid option")    

intro(name)
