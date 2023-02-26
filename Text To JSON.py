import json
import os
import string

root = os.path.dirname(os.path.realpath(__file__))
sorted_words_file = rf"{root}\sorted_words.json"

def clean_input(input_str):
    if "\\" not in input_str or ":" not in input_str:
        input_str = input_str.lower()
        input_str = input_str.replace('"', '')
        translator = str.maketrans('', '', string.punctuation)
        input_str = input_str.translate(translator)

    return input_str

user_input = input("Type in the path to the file that you want to sort:\n")
user_input = clean_input(user_input).strip('"')

if os.path.exists(user_input):
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

        with open(sorted_words_file, "w") as f:
            json.dump(sorted_words, f, indent = 4)
        
        print(f"Sorted! you can find it at {sorted_words_file}")
else:
    print("file not found")