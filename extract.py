import pymupdf

def extract_pdf(path):

    list_text = []
    doc = pymupdf.open(path)
    # out = open("output.txt", "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text()
        page_num = page.number + 1

        list_text.append((text, page_num))
    # out.close()
    doc.close()
    return list_text





if __name__ == "__main__":
    print(extract_pdf("Data/AlgoChap1_Sem1.pdf"))