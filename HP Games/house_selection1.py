name = input("Hello student, what is your name? ")

gryffindor = 0
ravenclaw = 0
slytherin = 0 
hufflepuff = 0 




q9 = input(f" {name}, do you belong in Hogwarts? y/n ")

if q9 == "y":
	print("Weclcome to the sorting hat! ")
else:
	print("You should not be here, you are a muggle!")	
	
qg = input(f'{name}, do you have an account at Gringotts? ')

if qg == 'y':
	print("Welcome to another magical year! ")
else:
	print("Are you a muggle?\n")			


print(f"{name.title()}, here are the houses: [G]ryffindor, [R]avenclaw, [S]lytherin, or [H]ufflepuff")

q1 = input('Which house to you like more? ')

if q1 == "G":
	gryffindor += 1
elif q1 == "R":
	ravenclaw += 1
elif q1 == "S":
	slytherin += 1
else:
	hufflepuff += 1
	
	
q2 = input(f"{name.title()}, are you He Who Shall Not be Named? y/n ")

if q2 == 'y':
	slytherin += 20
	print("Uh, we know who you are now...")	
	
q3 = input(f"{name.title()}, which color do you prefer? [R]ed, [Y]ellow, [B]lue, [Green] ")	

if q3 == "R":
	gryffindor += 1
elif q3 == "B":
	ravenclaw += 1
elif q3 == "G":
	slytherin += 1
else:
	hufflepuff += 1

q4 = input(f"{name.title()}, are you brave? y/n ")

if q4 == "y":
	gryffindor += 1
	hufflepuff += 1

q5 = input(f"{name.title()}, do you like eating breakfast with dementors? y/n ")

if q5 == "y":
	slytherin += 2
else:
	gryffindor += 1
	hufflepuff += 1
	ravenclaw += 1
		
q6 = input(f'What is your favourite animal? [L]ion, [S]nake, [B]adger, [E]agle ')

if q6 == "L":
	gryffindor += 1
elif q6 == "E":
	ravenclaw += 1
elif q6 == "S":
	slytherin += 1
else:
	hufflepuff += 1
	
q7 = input(f'In the movies, who is your favourite character? Hermonie, Harry, Draco, Ron ')

if q7 == 'Draco':
	slytherin += 1
else:
	gryffindor += 1
	
q8 = input("When you go on vacation, is it to Azkahban? y/n ")

if q8 == 'y':
	slytherin += 1
else:
	gryffindor += 1
	hufflepuff += 1
	ravenclaw += 1	

q10 = input("Are you scared of Dumbledore? y/n ")

if q10 == 'y':
	slytherin += 1
else:
	gryffindor += 1
	hufflepuff += 1
	ravenclaw += 1	

q11 = input("Do you like using unforgiveable curses?")

if q11 == 'y':
	slytherin += 1
else:
	gryffindor += 1
	hufflepuff += 1
	ravenclaw += 1	
	
q12 = input("Do you want to work at the ministry of magic? ")

if q12 == 'y':
	ravenclaw += 1	
else:
	gryffindor += 1
	hufflepuff += 1
	slytherin += 1	

q13 = input("What pet would you choose? [O]wl, [R]at, [C]at, [T]oad")

if q13 == "O":
	gryffindor += 1
elif q13 == "C":
	ravenclaw += 1
elif q13 == "R":
	slytherin += 1
else:
	hufflepuff += 1	
	
q14 = input("Are you a fan of flying cars? y/n ")

if q14 == "y":
	gryffindor += 1
else:	
	hufflepuff += 1
	ravenclaw += 1
	
q15 = input("What is your favourite Hogwarts treat? [C]hocolate frogs, [B]utter beer ")

if q15 == 'C':
	gryffindor += 1
	slytherin += 1
else:
	hufflepuff += 1
	ravenclaw += 1	
	
q16 = input("If you were really hungry, could you eat a chocolate bludger to win an edible quiddich match?")			

q18 = input("Do you live under the stairs?")

q20 = input("If you eat a chocolate frog, does it jump around inside your stomach?")

q21 = input(f'Is your name {name}?') 

q22 = input('Would you eat patronus pancakes?')

	
print("Gryffindor",gryffindor)
print("Ravenclaw",ravenclaw)
print("Slytherin",slytherin)
print("Hufflepuff",hufflepuff)			
