import spacy

nlp = spacy.load("en_core_web_sm")

# slang dictionary
slang_dict = {
    "bro": "brother",
    "idk": "I don't know",
    "u": "you",
    "r": "are",
    "rn": "right now",
    "gonna": "going to",
    "wanna": "want to",
    "lol": "laughing",
}

def normalize_text(text):

    doc = nlp(text)

    words = []

    for token in doc:
        word = token.text.lower()

        if word in slang_dict:
            words.append(slang_dict[word])
        else:
            words.append(token.text)

    normalized_sentence = " ".join(words)

    return normalized_sentence