import unicodedata

#Enleve les ligatures :ex: "ﬁ" devient "fi", "ﬂ" devient "fl", etc.
def lagature_cleaning(text):
    text = unicodedata.normalize("NFKC", text)

    return text

#Permets de transformer chaque page en une liste de plusieurs lignes
def line_cleaning(text):
    
    lines = text.splitlines()
    return lines

#Donne le nombre de repétitions de chaque ligne dans le PDF.
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

#Enleve les pieds de page du PDF, en se basant sur le nombre de répétitions de chaque ligne dans le PDF.
def remove_footer(pages):
    # Le seuil : une ligne présente sur plus de la moitié des pages = pied de page
    seuil = len(pages) / 2

    # Pour chaque ligne du PDF, sur combien de pages elle apparaît
    repetition = check_repetion(pages)

    # 1. Construire la liste des lignes à supprimer
    a_supprimer = []
    for ligne, count in repetition.items():   # chaque ligne et son nombre d'apparitions
        if count > seuil:                     # elle se répète trop → pied de page
            a_supprimer.append(ligne)

    # 2. Nettoyer chaque page
    for page in pages:
        lignes = line_cleaning(page["text"])  # découpe le texte de la page en lignes
        lignes_gardees = []
        for ligne in lignes:
            if ligne not in a_supprimer:      # pas un pied de page → on la garde
                lignes_gardees.append(ligne)
        page["text"] = "\n".join(lignes_gardees)  # recolle les lignes gardées en un seul texte

    return pages