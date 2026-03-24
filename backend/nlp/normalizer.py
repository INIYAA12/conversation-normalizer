import spacy

nlp = spacy.load("en_core_web_sm")

slang_dict = {
    "bro": "brother",
    "idk": "I don't know",
    "u": "you",
    "r": "are",
    "rn": "right now",
    "gonna": "going to",
    "lol": ""
}

def normalize_text(text):

    doc = nlp(text.lower())

    words = []
    changes = []

    for token in doc:
        word = token.text

        if word in slang_dict:
            replacement = slang_dict[word]

            if replacement != "":
                words.append(replacement)

                changes.append({
                    "from": word,
                    "to": replacement
                })
        else:
            words.append(word)

    sentence = " ".join(words).capitalize()

    if not sentence.endswith((".", "!", "?")):
        sentence += "."

    return sentence, changes