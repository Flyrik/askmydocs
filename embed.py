import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.errors import NotFoundError



#Enconde les chunks en vecteurs et les stocke dans une collection ChromaDB. Chaque chunk est associé à son texte, son embedding, et des métadonnées (page et chemin du fichier).
def encoding_text(model, chunks):
    #Créer une table/ collection
    client = chromadb.PersistentClient(path="chroma_db")
    try :
        client.delete_collection(name="vecteor_chunk")

    except NotFoundError:
        pass

    vecteor_chunk = client.get_or_create_collection(
    name="vecteor_chunk",
    configuration={"hnsw": {"space": "cosine"}},)
# "space": "cosine" -> les chunks sont comparés par l'ANGLE entre leurs
# vecteurs (= leur sens), pas par la distance entre leurs bouts.
# Ce réglage se fait à la création, car ChromaDB s'en sert pour construire
# son index HNSW : un réseau qui relie chaque chunk à ses voisins les plus
# proches, pour chercher vite sans tout comparer.
# Attention : ChromaDB renvoie une DISTANCE (= 1 - similarité cosine),
# donc plus elle est petite, plus le chunk est proche.

    
    for i, chunk in enumerate(chunks):
        text = chunk["text"]
        chunk_embedding = model.encode(text)

        #model.encode(texte)
#    1. tokenisation      → découpe le texte en tokens (avec model.tokenizer)
#    2. troncature        → garde au maximum 128 tokens
#    3. passage dans le modèle → un vecteur par token
#    4. pooling           → un seul vecteur de 384 nombres

        vecteor_chunk.upsert(
            documents=[text],

            embeddings = chunk_embedding,
            metadatas=[{"page": chunk["page"], "path": chunk["path"]}],
            ids = [str(i)]
        )
    # print(client.list_collections()) #list les collections existantes dans la base de données
    # print(vecteor_chunk.peek())    # aperçu des premiers éléments
    # print(vecteor_chunk.count())   # nombre total d'éléments dans la collection
    

