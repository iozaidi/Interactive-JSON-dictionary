import json
import difflib

from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))


def GrabKeyValuePair(word):
    if word in data:
        print(data[word])
    elif len(get_close_matches(word,data.keys())) > 0:
        correctwordmatch = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if correctwordmatch == "Y":
            word = get_close_matches(word,data.keys())[0]
            word = word.lower()
            print(data[word])
        else:
            return "Restart!"
    else:
        print("No data found!")

word = ''
searchyn = ''

while(word != '1'):
    word = input("Enter word: ")
    if word == 'Exit':
        searchyn = input('Do you want to search "Exit" as word? press "1" to Contiune or "2" to Exit: ')
        if searchyn == "1":
            print(GrabKeyValuePair(word))
        else:
            print('Bye!')
            break
    else: print(GrabKeyValuePair(word))

    