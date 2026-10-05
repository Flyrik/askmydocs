
from extract import extract_all
from chunk import chunk_fill

def main():
    pages = extract_all("data/*.pdf")    # étape 1
    chunks = chunk_fill(pages)            # étape 2
    print(len(pages), "pages →", len(chunks), "chunks")

if __name__ == "__main__":
    main()