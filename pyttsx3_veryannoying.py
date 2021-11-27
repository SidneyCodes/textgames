import random

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
	print(voice)
	
	engine.setProperty('voice', voice.id)
	engine.say('Luke and Ian own pizza roll simulator')

	words = ['luke','ian','pizza','roll','simulator']

	for loop in range(1,10):
		engine.say(f'{random.choice(words)},{random.choice(words)},{random.choice(words)},{random.choice(words)},{random.choice(words)},{random.choice(words)},{random.choice(words)}')
 


engine.runAndWait()
