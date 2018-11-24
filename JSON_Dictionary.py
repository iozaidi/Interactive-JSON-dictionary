import json

data = json.load(open("data.json"))


def GrabKeyValuePair(word):
    if word in data:
        print(data[word])
    else:
        print("No data found!")

word = ''

while(word != 'exit'):
    word = input("Enter word: ")
    word = word.lower()
    print(GrabKeyValuePair(word))