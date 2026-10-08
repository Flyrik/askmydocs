

from sentence_transformers import SentenceTransformer

from chunk import chunk_fill

from extract import extract_all



reference = ["Le chat est assis sur le tapis."]
proche = [
    "Un félin se repose sur la moquette." ]

loin = ["Le marché boursier s'est effondré."]




# 2. Calculate embeddings by calling model.encode()

def information_model(model_name, text):
    model = SentenceTransformer(model_name)
    print(f"Max sequence length for {model_name}: {model.max_seq_length}") #Par chunk, il regarde jusqu'à combien de token ce modele peut gérer. Si on dépasse cette limite, il va tronquer le texte et ne garder que les premiers tokens.
    tokens = model.tokenizer.tokenize(text)
    print("Nombre de tokens:", len(tokens))
    print(f"Tokens: {tokens}")
    return model

def compare(model_name, reference, proche, loin):
    # 1. Load a pretrained Sentence Transformer model

    model = SentenceTransformer(model_name)
    #Transforme les phrases en vecteurs de dimension  N ( 238, 768 etc) depend du modele choisi.
    reference = model.encode(reference)
    proche = model.encode(proche)
    loin = model.encode(loin)

     #calcule la cosine similarity entre chaque vecteur de a et chaque vecteur de b.

    test1 = model.similarity(reference, proche)
    test2 = model.similarity(reference, loin)

    return test1, test2


if __name__ == "__main__":
    pages = extract_all("data/*AlgoChap1_Sem1.pdf")
    chunks = chunk_fill(pages)
    information_model("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", chunks[10]["text"])
    