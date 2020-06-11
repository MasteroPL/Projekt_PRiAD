import string

unhandled_punctuation_characters = "—«»"

def strip_punctuation(text):
    global unhandled_punctuation_characters
    result = text.translate(str.maketrans('', '', string.punctuation))

    for c in unhandled_punctuation_characters:
        result = result.replace(c, '')

    return result

def clear_for_rhymes_detection(text):
    return strip_punctuation(text).replace("\n", "").replace("\r", "").strip()