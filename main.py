
from sentence_transformers import SentenceTransformer

from compare_model import compare_nbr_token_by_chunk
from extract import extract_all
from chunk import chunk_fill
from embed import encoding_text
from search import search, ask_llm

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def main():
    
    exit_bool = False
    x = Start_option()

    if x == 1:
        while not exit_bool:
            try :
                text = input("Entrez votre question que vous voulez poser au LLM : ")    
        
                print(ask_llm(text, model, 3)) 
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")

            print("\n") 
            y = int(input("Voulez-vous poser une autre question ?\n1. Oui\n2. Non\n\n"))
            if y == 2:
                print("Merci d'avoir utilisé le programme. Au revoir !")
                
                exit_bool = True
 
def Start_option():    
    x = 0

    while x != 1:
        try :
            x = int(input("Choisissez une option :\n1. Poser une question\n\n"))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")
            continue
        
    return x



def initialisation():
    

    pages = extract_all("data/*.pdf")    # étape 1
    chunks = chunk_fill(pages,model)     
    # print(f"Nombre de chunks générés: {len(chunks)}")       # étape 2
    # compare_nbr_token_by_chunk("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", chunks)
    
    encoding_text(model, chunks)
    

   

if __name__ == "__main__":
    initialisation()
    main()
    