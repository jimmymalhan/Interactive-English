import json
import os
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    while True:
        w = w.lower()
        if w in data:
            return data[w]
        elif w.title() in data:  # if user entered "texas" this will check
            return data[w.title()]
        elif w.upper() in data:  # id case user enters words like USA
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
            if yn == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "The system didn't understand your entry. Please try again!"
        else:
            return "The word doesn't exist in the dictionary."


word = input("Enter word: ")


def main():
    os.system('cls')
    output = translate(word)

    if type(output) == list:
        for item in output:  # change lines if the output is more than two lines
            print(item)
    else:
        print(output)


if __name__ == '__main__':
    main()
