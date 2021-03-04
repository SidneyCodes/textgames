import urllib.request
import json

while True:
	
	bird = input("Please enter a word ")
	
	url = 'https://api.datamuse.com/words?rel_rhy=' + bird
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	rhyme = result[0]
	word = rhyme['word']
	
	print(f'The wise old man says {bird}! You mean {word}!')

