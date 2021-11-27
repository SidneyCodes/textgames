import urllib.request
import json
import random

counter = 1
points = 0

while True:
    print("You have",points,"points")

    triviaurl = 'https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple'
    response = urllib.request.urlopen(triviaurl)
    result = json.loads(response.read())
    #print(result)

    questions = []
    questions.append(result["results"][0]["correct_answer"])
    for wrong in result["results"][0]["incorrect_answers"]:
        questions.append(wrong)
    random.shuffle(questions)

    print("Question",counter)
    counter += 1
    print(result["results"][0]["question"])
    print("Your options are:")
    for item in questions:
        print(item)

    choice = input("What is your answer?")

    if choice == result["results"][0]["correct_answer"]:
        print("You are right!")
        points += 1
    else:
        print("You are wrong")
        print("The correct answer is:",result["results"][0]["correct_answer"])
        points -= 1

    choice = input("Play again? y/n")

    if choice == 'n':
        break

'''

try:
 print(result["results"][0]["question"])
 #print(result["results"][1])
 #print(result["text"])
 #print(result)

except IndexError:
 pass
else:
 pass
 '''
