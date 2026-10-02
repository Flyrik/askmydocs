import unicodedata

def lagature_cleaning(text):
    text = unicodedata.normalize("NFKC", text)

    return text


