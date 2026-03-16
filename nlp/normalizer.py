import json
import string

with open("nlp/slang_dictionary.json") as f:
    slang_dict = json.load(f)


def normalize_text(text):

    words = text.lower().split()

    normalized_words = []

    for word in words:

        word = word.strip(string.punctuation)

        if word in slang_dict:
            replacement = slang_dict[word]

            if replacement != "":
                normalized_words.append(replacement)
        else:
            normalized_words.append(word)

    sentence = " ".join(normalized_words)

    # Capitalize first letter
    sentence = sentence.capitalize()

    # Add punctuation if missing
    if not sentence.endswith("."):
        sentence += "."

    return sentence

if __name__ == "__main__":
    sentence = input("Enter sentence: ")
    result = normalize_text(sentence)
    print("Normalized:", result)