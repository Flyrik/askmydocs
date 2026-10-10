
from sentence_transformers import SentenceTransformer

from compare_model import compare_nbr_token_by_chunk
from extract import extract_all
from chunk import chunk_fill

def main():
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    pages = extract_all("data/*.pdf")    # étape 1
    chunks = chunk_fill(pages,model)     
    print(f"Nombre de chunks générés: {len(chunks)}")       # étape 2
    # compare_nbr_token_by_chunk("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", chunks)
   

if __name__ == "__main__":
    main()