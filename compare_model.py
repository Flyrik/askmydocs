

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
    nbr_token = len(tokens)
    print("Nombre de tokens:", nbr_token)
    print(f"Tokens: {tokens}")
    #Caractère par token = nombre de caractères / nombre de tokens. Si on a 1000 caractères et 200 tokens, on a 5 caractères par token.
    print(len(text)/nbr_token, "caractères par token")
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

#Cette fonction permet de comparer le nombre de tokens par chunk pour un modèle donné. Cela permet de vérifier si les chunks sont en dessous de la limite maximale de tokens que le modèle peut gérer.
def compare_nbr_token_by_chunk(model_name, chunks):
    list_nbr_token = []
    model = SentenceTransformer(model_name)
    for i, chunk in enumerate(chunks):
        tokens = model.tokenizer.tokenize(chunk["text"])
        nbr_token = len(tokens)
        list_nbr_token.append(nbr_token)
        print(f"Chunk {i} - Nombre de tokens: {nbr_token}")
        print(f"Chunk {i} - Tokens: {tokens}")
        print(f"Chunk {i} - Caractères par token: {len(chunk['text'])/nbr_token}")
    print(f"Maximum number of tokens in a chunk: {max(list_nbr_token)}")
    print(f"Minimum number of tokens in a chunk: {min(list_nbr_token)}")
    print(f"Average number of tokens in a chunk: {sum(list_nbr_token)/len(list_nbr_token)}")


if __name__ == "__main__":
    pages = extract_all("data/*.pdf")
    chunks = chunk_fill(pages, SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"))
    # information_model("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", chunks[10]["text"])
    compare_nbr_token_by_chunk("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", chunks)