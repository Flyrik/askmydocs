

from sentence_transformers import SentenceTransformer



reference = ["Le chat est assis sur le tapis."]
proche = [
    "Un félin se repose sur la moquette." 
]

loin = ["Le marché boursier s'est effondré."]




# 2. Calculate embeddings by calling model.encode()

def information_model(model_name, text):
    model = SentenceTransformer(f" {model_name}")
    print(f"Max sequence length for {model_name}: {model.max_seq_length}")
    tokens = model.tokenizer.tokenize(text)
    print(len(tokens))
    return model

def compare(model_name, reference, proche, loin):
    # 1. Load a pretrained Sentence Transformer model

    model = SentenceTransformer(f" {model_name}")
    #Transforme les phrases en vecteurs de dimension  N ( 238, 768 etc) depend du modele choisi.
    reference = model.encode(reference)
    proche = model.encode(proche)
    loin = model.encode(loin)

     #calcule la cosine similarity entre chaque vecteur de a et chaque vecteur de b.

    test1 = model.similarity(reference, proche)
    test2 = model.similarity(reference, loin)

    return test1, test2


    
    ...




print("Similarity between reference and candidates:", proche)
print("Similarity between reference and bourse:", loin)
#convert_to_tensor=True permet de renvoyer un tensor pytorch plutot qu'un tableau numpy.
# print(embeddings.shape)


if __name__ == "__main__":
    print("Embedding initialized.")