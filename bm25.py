import re

# Cette fonction transforme le texte de chaque chunk en une liste de mots.
def tokenize_chunks(chunks):
    list_tokens = []
    for chunk in chunks:
        
        tokens = tokenize(chunk["text"])
        list_tokens.append(tokens)


    return list_tokens

#Cette fonction transforme un texte en une liste de mots (minuscules, sans ponctuation). 
def tokenize(text):
    # un texte → une liste de mots (minuscules, sans ponctuation)
    return re.findall(r"\w+", text.lower())
