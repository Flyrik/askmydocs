import chromadb
from sentence_transformers import SentenceTransformer




def encoding_text(model_name, chunks):
    client = chromadb.PersistentClient(path="chroma_db")
    vecteor_chunk = client.get_or_create_collection(name="cours")
    model = SentenceTransformer(model_name)

    for chunk in chunks:
        text = chunk["text"]
        embedding = model.encode(text)
        vecteor_chunk.add(
            documents=[text],
            metadatas=[{"page": chunk["page"], "path": chunk["path"]}],
            ids=[f"{chunk['path']}_page_{chunk['page']}"]
        )
    return embedding

if 