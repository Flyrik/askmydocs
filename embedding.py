

from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

reference = ["Le chat est assis sur le tapis."]
proche = [
    "Un félin se repose sur la moquette." 
]

loin = ["Le marché boursier s'est effondré."]
 #calcule la cosine similarity entre chaque vecteur de a et chaque vecteur de b.




# 2. Calculate embeddings by calling model.encode()




def compare(model, reference, proche, loin):
    model = SentenceTransformer(f" {model}")
    reference = model.encode(reference)
    proche = model.encode(proche)
    loin = model.encode(loin)

    # charger le modèle, encoder, afficher les 2 scores
    ...


proche = model.similarity(embeddings2, embeddings3)
loin = model.similarity(embeddings2, embeddings4)

print("Similarity between reference and candidates:", proche)
print("Similarity between reference and bourse:", loin)
#convert_to_tensor=True permet de renvoyer un tensor pytorch plutot qu'un tableau numpy.
# print(embeddings.shape)
print(model.max_seq_length)

if __name__ == "__main__":
    print("Embedding initialized.")