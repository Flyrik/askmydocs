
import clean
from extract import extract_all
from sentence_transformers import SentenceTransformer

CHUNK_SIZE = 350 
#350 ÷ 3 ≈ 116 tokens. donc good car notre model peut gérer 128 tokens max. Donc on est en dessous de la limite. On peut donc faire des chunks de 350 caractères max.
def chunk_fill(pages,model):
    list_chunks = []
    chunks = []
    current_chunk = 0
    for page in pages :
        ligne = clean.line_cleaning(page["text"])
        chunks = []
        current_chunk = 0
        for line in ligne :
            
            if current_chunk + len(line) <= CHUNK_SIZE:
                current_chunk += len(line) +1  #Quand on fait le join, cela rajoute un espace entre chaque lgine qu'on join donc rajoute 1 caractère de plus à la taille du chunk.
                chunks.append(line)
            else:
                if chunks: #SI c'est vide, on le sauvegarde pas, ca prend de la place pour rien.
                    list_chunks.append({"text": " ".join(chunks), "page": page["page"], "path": page["path"]})
                chunks = []
                chunks.append(line)
                current_chunk =len(line) +1
        #Pour sauvegarder le dernier chunk.
        if chunks: 
            list_chunks.append({"text": " ".join(chunks), "page": page["page"], "path": page["path"]})

    
    return list_chunks

# Ex de sortie de chunk_fill(pages) :
# [
#   {"text": "1. Fonctions réciproques\n1.1. Bijection\nDéfinition 1.1.1 : Soit f...",
#    "page": 2, "path": "AnalyseChapitre 1.pdf"},
# 
#   {"text": "1.2. Bijection continue\nThéorème 1.2.1 : Toute fonction continue...",
#    "page": 2, "path": "AnalyseChapitre 1.pdf"},
# 
#   {"text": "Théorème 1.2.2 : Dans un repère orthonormé...",
#    "page": 2, "path": "AnalyseChapitre 1.pdf"}
# ]
        
if __name__ == "__main__":
    pages = extract_all("data/*AlgoChap1_Sem1.pdf")
    chunks = chunk_fill(pages)