import json

#Created to parse random words from txt file gotten from https://codebeautify.org/random-word-generator
#Word list currently contains 3000 words, can of course add more
f = open('./wordList.txt', 'r')
listOut = f.read().split(',')
for i, word in enumerate(listOut):
    listOut[i] = word.lower()
with open('words.json', 'w') as output_file:
    json.dump(listOut, output_file)