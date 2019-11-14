import json 

from difflib import get_close_matches
data= json.load(open("data.json"))
# data = json.load(open("data.json"))






def getWord(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len( get_close_matches(word, data.keys())) >0:
        yn=input(f'did you mean this insted {get_close_matches(word, data.keys())}')
        if yn=="Y" or yn=="y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    



# print(len( get_close_matches("word", data.keys())))
# print(get_close_matches("word", data.keys()))

word = input("Enter word: ")
output = getWord(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



