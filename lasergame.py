loop = 0
loop2 = 0
howToMove = 5
side1 = 4
side2 = 6
printing = ""

player = ["  :}{:  ", ":-/==\-:"]

lazer = "   ||   "
noLazer = "        "

gap = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

lazer1 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer2 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer3 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer4 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer5 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer6 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer7 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer8 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer9 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer10 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
lazer11 = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

allLazers = [lazer1, lazer2, lazer3, lazer4, lazer5, lazer6, lazer7, lazer8, lazer9, lazer10, lazer11]

playerList = [False, False, False, False, False, True, False, False, False, False, False]
while True:
    while loop2 != 24:
        loop = 0
        printing += "|"
        while loop != 11:
            if loop2 >= 21:
                playerListChecker = playerList[loop]
                if playerListChecker == True:
                    printing = printing + player[loop2]
                else:
                    printing = printing + noLazer
            else:
                while loop != 11:
                    lazerListChecker = allLazers[loop2]
                    if lazerListChecker == True:
                        printing = printing + lazer
                    else:
                        printing = printing + noLazer
            loop += 1
        printing += "|"
        printing += "\n"
        loop2 += 1

    print(gap)
    print(printing)
    printing = ""
    loop2 = 0
    move = input("")
    move = move.upper()
    if move == "D":
        if howToMove == 10:
            continue
        playerList[howToMove] = False
        howToMove += 1
        playerList[howToMove] = True

    elif move == "A":
        if howToMove == 0:
            continue
        playerList[howToMove] = False
        howToMove -= 1
        playerList[howToMove] = True



