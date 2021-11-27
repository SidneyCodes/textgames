import random

muggle = 0
wizard = 0

houses = ['gryffindor', 'ravenclaw', 'slytherin', 'hufflepuff']
while True:
	if len(houses) > 0:
		random.shuffle(houses)
		print('You should be in ',houses[0].title())
		print("But should you? Its time for you to take the quiz!")
		choice = input("Do you accept this choice? y/n ")
		if choice == 'y':
			break
		else:
			del houses[0]
	else:
		print("Welcome to Muggle Madness!")	
		houses.append('Squib Station')
		break	
		
print(f'You are now in house {houses[0].title()}')

q1 = input("Do you like boring muggle things? y/n ")
if q1 == 'y':
	muggle += 1
else:
	wizard += 1
	
q2 = input("Would you battle a death eater y/n ")
if q2 == 'n':
	muggle += 1
else:
	wizard += 1
		
q3 = input("Are you a wizard? y/n ")
if q3 == 'n':
	muggle += 1
else:
	wizard += 1
			
q4 = input("Do you know someone who works for the Ministry of Magic? y/n ")
if q4 == 'n':
	muggle += 1
else:
	wizard += 1

q5 = input("Do you like magical celery? y/n ")
if q5 == 'n':
	muggle += 1
else:
	wizard += 1

q6 = input("Do you like your chocolate frogs jumping? y/n ")
if q6 == 'n':
	muggle += 1
else:
	wizard += 1

q7 = input("Do you live on Privet drive? y/n ")
if q7 == 'y':
	muggle += 1
else:
	wizard += 1
	
q8 = input("Have you ever made something unexplained happen? y/n ")
if q8 == 'n':
	muggle += 1
else:
	wizard += 1
	
q9 = input("Do you know how to play wizard chess? y/n ")
if q9 == 'n':
	muggle += 1
else:
	wizard += 1

q10 = input("Do you know what a basalisk is? y/n ")
if q10 == 'n':
	muggle += 1
else:
	wizard += 1

q11 = input("Do you think magicians do magic? y/n ")
if q11 == 'y':
	muggle += 1
else:
	wizard += 1

q12 = input("Do you know what an unforgiveable curse is? y/n ")
if q12 == 'n':
	muggle += 1
else:
	wizard += 1

q13 = input("Would you drink a tea called Muggle Madness? y/n ")
if q13 == 'n':
	muggle += 1
else:
	wizard += 1

if muggle > wizard:
	print("You have been tested, and found to be a Muggle!")
	print("muggle",muggle,"wizard",wizard)
	print(f"You are {muggle/13*100} percent muggle")
elif muggle == wizard:
	print("The score is equal, and you are a squib!")
else:
	print("We checked and it seems you are a wizard")
	print(f'You are {wizard/13*100} percent wizard!')
	print("wizard",wizard,"muggle",muggle)	
