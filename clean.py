import unicodedata

#Enleve les ligatures :ex: "ﬁ" devient "fi", "ﬂ" devient "fl", etc.
def lagature_cleaning(text):
    text = unicodedata.normalize("NFKC", text)

    return text

#Permets de transformer chaque page en une liste de plusieurs lignes
def line_cleaning(text):
    
    lines = text.splitlines()
    return lines
    
def check_repetion(pages):
    dico = {}
    for page in pages:
        lignes = line_cleaning(page["text"])
        
        for ligne in lignes:
            if ligne in dico:
                dico[ligne] += 1
            else:
                dico[ligne] = 1
    return dico

def remove_footer(pages):
    seuil = len(pages)/2