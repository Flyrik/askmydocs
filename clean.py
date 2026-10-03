
import unicodedata
import re


MIN_PAGES = 3
#Enleve les ligatures :ex: "ﬁ" devient "fi", "ﬂ" devient "fl", etc.
def lagature_cleaning(text):
    text = unicodedata.normalize("NFKC", text)

    return text

#Retire les pages animées, c'est à dire les pages qui sont des sous-ensembles de la page suivante. (ex: page 1 = page 2 maisl page 2 a une info de plus etc..)
def remove_page_animated(pages):
    list_gard = []
    for i in range(len(pages)-1):
        

        current_lignes = page_lines_set(pages[i]["text"])
        next_lignes = page_lines_set(pages[i+1]["text"])
        
        if current_lignes.issubset(next_lignes):
            continue
        else:
            list_gard.append(pages[i])
    list_gard.append(pages[-1])  # Ajoute la dernière page
        
    return list_gard

def page_lines_set(page):
    lignes = line_cleaning(page)   # texte → liste de lignes
    lignes_transformees = []
    for ligne in lignes:
        lignes_transformees.append(line_without_number(ligne)) # transforme les chiffres en #
    return set(lignes_transformees)  


#Permets de transformer chaque page en une liste de plusieurs lignes Et de supprimer les lignes vides.
def line_cleaning(text):
    list_gard = []
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line == "":  
            continue
        else :
            list_gard.append(line)



    return list_gard



#Transforme les chiffres en # d'une ligne, pour regler les problemes comme 2/90, 3/90 = #/# , #/# ... ( puis on fait le set seulement apres pour en compter que 1 par page)
def line_without_number(ligne):
    ligne = re.sub(r'\d+', '#', ligne) #le d+ permets de tranformer tous les chiffres / nombres en # : 2/94 = #/# alors que avec juste d : #/##
    return ligne


#Donne le nombre de repétitions de chaque ligne dans le PDF. (enleve les doublons pour qu'on compte que 1 par page)
def check_repetion(pages):
    dico = {}
   
    for page in pages:
        lignes = line_cleaning(page["text"])
        lignes_with_hide_number = []
        #Transforme les chiffres en #, pour regler les problemes comme 2/90, 3/90 = #/# , #/# ... ( puis on fait le set seulement apres pour en compter que 1 par page)
        for ligne in lignes:
            ligne = line_without_number(ligne)
            lignes_with_hide_number.append(ligne)

        set_lignes = set(lignes_with_hide_number)  
        



        for ligne in set_lignes:
            
            if ligne in dico:
                dico[ligne] += 1
            else:
                dico[ligne] = 1

        
        
    return dico




#Enleve les pieds de page du PDF, en se basant sur le nombre de répétitions de chaque ligne dans le PDF.
def remove_footer(pages):
    
    
    #Si le PDF contient moins de 3 pages, on ne supprime pas les pieds de page, car il n'y a pas assez de pages pour déterminer ce qui est un pied de page.
    if len(pages) < MIN_PAGES:
        return pages
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
            # on transforme les chiffres en # pour comparer car "a_supprimer contient des lignes avec # à la place des chiffres"
            version_comparative =  line_without_number(ligne)
            if version_comparative not in a_supprimer :     
                    
                lignes_gardees.append(ligne)
        page["text"] = "\n".join(lignes_gardees)  # recolle les lignes gardées en un seul texte

    return pages
    

