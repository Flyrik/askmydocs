import pymupdf
import pathlib 
import glob




def extract_pdf(path):

    list_text = []
    #Permet de ouvrir le fichier PDF avec pymupdf, et de récupérer le texte de chaque pageensuite stocké dans une liste de dictionnaires, où chaque dictionnaire contient le texte de la page, le numéro de la page et le nom du fichier PDF.
    doc = pymupdf.open(path)
    
    for page in doc: # iterate the document pages
        text = page.get_text()
        page_num = page.number + 1

        list_text.append({ "text": text, "page": page_num , "path": pathlib.Path(path).name})
    # out.close()
    doc.close()
    return list_text

def extract_all(folder):
    resultat = []
    #Glob permet de récupérer tous les nom des fichiers PDF dans le dossier spécifié par le paramètre folder.
    allpdf = glob.glob(folder)
    # print(allpdf)
    for pdf in allpdf:
        resultat.extend(extract_pdf(pdf))
    
    return resultat


    


if __name__ == "__main__":
    
    pdfs_extrait_all_pages = extract_all("data/*.pdf")
    print((pdfs_extrait_all_pages[0]))
    print(pdfs_extrait_all_pages[0]["text"])
    #Affiche le texte de la première page de chaque fichier PDF extrait.
    for page in pdfs_extrait_all_pages:
        if page["page"] == 1:
            
            print(page["text"])