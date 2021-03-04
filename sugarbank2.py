from random import randint as r
from time import sleep as s
print("This is a story about an ant")

sugar = 0
bank = 5_000_000
chocolate = 0
chocoxplode = 0
cost = 0

def intro(sugar, bank, chocolate, chocoxplode, cost):
  s(2)
  print("\nIt is a true story\n")
  s(2)
  print(f'Your sugar balance is {sugar}')	
  s(2)
  choice = input("\nHow much sugar would you like?")
  s(1)
  choice = int(choice)
  if choice < 10000:
    sugar += choice
    bank -= choice
    sugarbank(sugar, bank, chocolate, chocoxplode, cost)
  else:
    print('You greedy monkey! No sugar for you.')
    sugarbank(sugar, bank, chocolate, chocoxplode, cost)

def sugarbank(sugar, bank, chocolate, chocoxplode, cost):
  s(2)	
  print(f'\n\nYour sugar balance is {sugar}')	
  print('''
  Welcome to the sugar bank!
  Would you like to make a deposit or a wishdrawl?
  Type CAT for deposit
  Type SNAKEFACE for withhdrawl
  Type HAMSTER to rob the bank
  Type MANGO to light your sugar on fire
  Type GORILLA to give the bank your money
  Type RAVEN to trade some sugar for chocolate
  Type LADYBUG to play the lottery
  Type WOLF to make chocoxplode (exploding chocolate with enchaned flavor)
  ''')

  choice = input("Please pick an option")
    
  if choice == 'CAT':
      choice = input("How many sugars do you want to deposit")
      choice = int(choice)
      print("You deposit {choice} sugars")
      sugar -= choice
      bank += choice
  elif choice == 'HAMSTER':
      print("You rob the bank")
      print("You now have a huge amount of sugar")
      sugar += 50000
      bank -= 50000
  elif choice == 'MANGO':
      print("You light your sugar on fire")
      sugar = 0	
      print("You now have no sugar.")
      print("I hope you feel the pain of sugar poverty!\n")
  elif choice == 'GORILLA':
    bank += sugar
    sugar = 0
    print("You give all your sugar to the bank. The bank will remember your kindness.")
    s(2)
    print("But a gorilla hears you calling it so it rampages and nearly kills you. ")
    s(2)
    print("But it kills you. You die. The end,.")
    s(5)
    print("Just kidding! The bank remembers your kindness and gives the gorilla 100 sugar. It agrees to leave you alone. ")
    bank -= 100
  elif choice == 'LADYBUG':
    if sugar < 5:
      print("You can't afford the lottery!")
    else:
      winning = []
      winning.append(r(1,10))
      winning.append(r(1,10))
      winning.append(r(1,10))
      lottery = []
      print("You decide to play the lottery")
      print("The lottery costs {cost} sugar")
      sugar -= cost
      cost *= 1.4
      for i in range(3):
        choice = input("Pick a number ")
        choice = int(choice)
        lottery.append(choice)
      print(f'The winning lottery numbers are:')
      for number in winning:
        print(number)
      if lottery in winning:
        print("You won the lottery!")
        sugar += 10*number
  elif choice == 'BREAD':
    print("You go to the bread bank")
    url = open("bread.txt")
    html = url.read()
    print(html)
  
  elif choice == 'RAVEN':
    print("1 chocobar => 50 sugars (chocolate is better than sugar!)")
    chocolate = input("How many chocobars would you like?")
    sugar -= int(chocolate)*50
    
  elif choice == 'WOLF':
    print("10 chocolates + 100 sugars => chocoxplode")
    chocoxplode += int(input("How many chocoxplodes would you like?"))
    chocolate -= 10*int(chocoxplode)
    sugar -= 100*int(chocoxplode)
    
  else:
    print("You take 100 sugars")
    sugar += 100
    bank -= 100
      
  print(f'\nYour sugar balance is {sugar}\n')
  print(f'\nYour chocolate balance is {chocolate}\n')
  print(f'\nYour chocoxplode balance is {chocoxplode}\n')
  s(2)	

  choice = input("Do you want to play again? y/n ")
  s(1)
  if choice == 'y':
    intro(sugar, bank, chocolate, chocoxplode, cost)


intro(sugar, bank, chocolate, chocoxplode, cost)


print("Thanks for playing, game over")

#I had 97093 Sugar on 4/20/2020
