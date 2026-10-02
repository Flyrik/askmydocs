import pymupdf
import pathlib 
import glob
from clean import lagature_cleaning, line_cleaning, check_repetion, remove_footer



def extract_pdf(path):

    list_text = []
    #Permet de ouvrir le fichier PDF avec pymupdf, et de récupérer le texte de chaque page ensuite stocké dans une liste de dictionnaires, où chaque dictionnaire contient le texte de la page, le numéro de la page et le nom du fichier PDF.
    doc = pymupdf.open(path)
    #Permet de récupérer le nom du fichier PDF à partir du chemin d'accès complet.(Enleve le "\data...")
    path_name = pathlib.Path(path).name
    for page in doc: # iterate the document pages
        text = page.get_text()
        text = lagature_cleaning(text)
        page_num = page.number + 1

        list_text.append({ "text": text, "page": page_num , "path": path_name })
        

    
    doc.close()
    return list_text

def extract_all(folder):
    resultat = []
    #Glob permet de récupérer tous les nom des fichiers PDF dans le dossier spécifié par le paramètre folder.
    allpdf = glob.glob(folder)
    # print(allpdf)
    for pdf in allpdf:
        page = extract_pdf(pdf)
        page = remove_footer(page)
        resultat.extend(page)
        
        
    return resultat


    


if __name__ == "__main__":
    
    pdfs_extrait_all_pages = extract_all("data/*.pdf")
    print((pdfs_extrait_all_pages[6]))
    