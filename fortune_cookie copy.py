import time


item = []
money = 0

print("One upon a time, a girl is exploring an enchanted forest.")
time.sleep(2)
print("She sees a key on the ground. Should she pick it up?")
time.sleep(2)
choice = input("yes or no? ")

if choice == 'yes':
	print("She picks up the key and puts it in her pocket")
	item.append("a key")
	time.sleep(2)
else:
	print("She does not pick up the key and keeps on walking")
	item.append("nothing")
	time.sleep(2)

print("Suddenly, a gate guarded by gargoyles comes into view!")
time.sleep(2)
print("What is in your pockets? the gargoyles shout.")
time.sleep(2)
print(f"She opens her pockets to show she has {item[0]}!")
time.sleep(2)
if item[0] == 'a key':
	print("She takes out the key and unlocks the gate.")
	time.sleep(2)
else:
	print("She has nothing and climbs the gate.")
	time.sleep(2)

print("A strange travelling peddler offers to buy the contents of her pocket.")
time.sleep(2)

if item[0] == 'a key':
	print("she takes out the key and sells it to the stranger.")
	money += 100

else:
	print("She has nothing and keeps on walking")
	time.sleep(2)

print(f'She checks her pockets and now has {item[0]} and {money} galleons')
time.sleep(2)
print("Next, a griffin stops her.")
time.sleep(2)
print("What is in your pockets? the griffin shouts.")
time.sleep(2)
print(f"She opens her pockets to show she has {money} galleons.")
time.sleep(2)
print("He steals the contents of her pockets!")
time.sleep(2)
print("The girl continues on sadly, with empty pockets.")
time.sleep(2)

print("A soldier on a horse rides by and stops to ask where the griffin went.")
time.sleep(2)
print("Should she tell hime where it went?")
time.sleep(2)

choice = input("yes or no? ")

if choice == 'yes':
	print("She she tells him where it went")
	print("the soldier gives her a dagger as a thank you.")
	item.append("a dagger")
	time.sleep(2)
else:
	print("She does not tell him, and runs away.")
	item.append("nothing")
	time.sleep

	print("Soon, she comes across a village.")
	print("She finds a lock smith near the fountain.")

if item[0] == 'a dagger':
    print("She could sell the dagger and get money!")

else:
    print("She keeps on walking.")

if item[0] == 'a dagger':
    print("Should she sell the dagger?")
    choice = input("yes or no? ")

	if choice =='yes':
		print("She sells her dagger to a warrior maiden.")
		money += 100
	else:
		print("she keeps on walking.")


print("As she heads home, she passes the lock smith again.")

if money == 100:
    print("She buys a key and goes home happily, shows her mother, and lives happily ever safely inside the gates.")
else:
    print("She goes home sadly, but is cheered up with apple pie for dessert.")

choice = int(input("Pick a number from 1-100 "))
if choice >= 50:
  print("Your number is 50 or above")
else:
  print("Your number is less than 50")      
