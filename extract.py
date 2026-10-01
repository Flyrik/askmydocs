import pymupdf
import pathlib 
import glob




def extract_pdf(path):

    list_text = []
    doc = pymupdf.open(path)
    # out = open("output.txt", "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text()
        page_num = page.number + 1

        list_text.append({ "text": text, "page": page_num , "path": pathlib.Path(path).name})
    # out.close()
    doc.close()
    return list_text

def extract_all(folder):
    resultat = []
    allpdf = glob.glob(folder)
    print(allpdf)
    for pdf in allpdf:
        resultat.extend(extract_pdf(pdf))
    
    return resultat


    


if __name__ == "__main__":
    
    pdfs_extrait_all_pagess= extract_all("data/*.pdf")
    print(len(pdfs_extrait_all_pagess))
    print(pdfs_extrait_all_pagess[0]["text"])
    
    # for texte, num in pages[1:12]:      # pages 2 à 7 du PDF
    #     print(f"===== PAGE {num} =====")
    #     print(texte)