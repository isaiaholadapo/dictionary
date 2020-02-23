import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return word[data.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s: " %get_close_matches(word, data.keys()) [0])
        decide = input("press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word , data.keys()) [0]]
        elif decide == "n":
            return("word not availble, kindly check your spelling")
        else:
            return("you have entered wrong input, please enter y or n")

    else:
        print("you have entered the wrong word")

word = input("Type the word you to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)