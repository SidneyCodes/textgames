import urllib.request
import json
import time

url = 'https://api.datamuse.com/words?rel_rhy=max'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

rhyme = result[0]

word = rhyme['word']

print(word)