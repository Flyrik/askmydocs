import chromadb
from sentence_transformers import SentenceTransformer


def search(question, model, k):

    client = chromadb.PersistentClient(path="chroma_db")
    vecteor_chunk = client.get_collection(name="vecteor_chunk")

    
    question_embedding = model.encode(question)

    results = vecteor_chunk.query(
    query_embeddings=[question_embedding],
    n_results=k
    #k, c’est le nombre de chunks que tu veux récupérer : les k plus proches de la question
)


