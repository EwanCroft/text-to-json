import json
import os
import string

root = os.path.dirname(os.path.realpath(__file__))

def clean_input(input_str):
    if "\\" not in input_str or ":" not in input_str:
        # Lowercase the input string
        input_str = input_str.lower()

        # Remove quotes
        input_str = input_str.replace('"', '')

        # Remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        input_str = input_str.translate(translator)

    return input_str

user_input = input("Type in the path to the file that you want to sort:\n")
user_input = clean_input(user_input).strip('"')

with open(f"{user_input}", "r") as f:
    lines = f.read().splitlines()

words = [word for line in lines for word in line.split()]
words = [clean_input(word) for word in words]
words = sorted(words, key=str.lower)

sorted_words = {}
for word in words:
    if word.isdigit():
        if "numbers" not in sorted_words:
            sorted_words["numbers"] = []
        sorted_words["numbers"].append(word)
    else:
        initial = word[0].lower()
        if initial not in sorted_words:
            sorted_words[initial] = []
        sorted_words[initial].append(word)

with open(f"{root}\\sorted_words.json", "w") as f:
    json.dump(sorted_words, f, indent = 2)
