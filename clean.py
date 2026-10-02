import unicodedata

def lagature_cleaning(text):
    text = unicodedata.normalize("NFKC", text)


mot = "spéciﬁque"
print(len(mot))
print(len(unicodedata.normalize("NFKD", mot)))
print(len(unicodedata.normalize("NFKC", mot)))  