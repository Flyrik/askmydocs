import chromadb
from sentence_transformers import SentenceTransformer




def encoding_text(model_name, chunks):
    client = chromadb.PersistentClient(path="chroma_db")
    vecteor_chunk = client.get_or_create_collection(name="vecteor_chunk")
    model = SentenceTransformer(model_name)

    for i, chunk in enumerate(chunks):
        text = chunk["text"]
        chunk_embedding = model.encode(text)

        #model.encode(texte)
#    1. tokenisation      → découpe le texte en tokens (avec model.tokenizer)
#    2. troncature        → garde au maximum 128 tokens
#    3. passage dans le modèle → un vecteur par token
#    4. pooling           → un seul vecteur de 384 nombres

        vecteor_chunk.add(
            documents=[text],
            embeddings = chunk_embedding,
            metadatas=[{"page": chunk["page"], "path": chunk["path"]}],
            ids = [str(i)]
        )
    print(vecteor_chunk.peek())    # aperçu des premiers éléments
    print(vecteor_chunk.count())   # nombre total d'éléments dans la collection
    

