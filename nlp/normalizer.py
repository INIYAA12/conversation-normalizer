import json

# load slang dictionary
with open("nlp/slang_dictionary.json") as f:
    slang_dict = json.load(f)

def normalize_text(text):

    words = text.lower().split()

    normalized_words = []

    for word in words:
        if word in slang_dict:
            normalized_words.append(slang_dict[word])
        else:
            normalized_words.append(word)

    result = " ".join(normalized_words)

    return result


if __name__ == "__main__":

    sentence = input("Enter sentence: ")

    output = normalize_text(sentence)

    print("Normalized:", output)