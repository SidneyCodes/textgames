import webbrowser

item = []

print("Cole goes outside and finds an old but magical, newspaper")

choice = input("Pick up newspaper do you choose? y/n ")


if choice == 'y':
	print("Pick up newspaper you do and have magic you are")
	item.append("newspaper")
	webbrowser.open('https://images.unsplash.com/photo-1566378246598-5b11a0d486cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80')
else:
	print("Deciding to not pick up the paper, your adventure is over")
	item.append("nothing")
	
print("You now have:",item[0])

print("You now has:")
for thing in item:
	print(thing)		
