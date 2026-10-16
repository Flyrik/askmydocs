import chromadb
from sentence_transformers import SentenceTransformer
import ollama
from ollama import chat
def search(question, model, k):

    client = chromadb.PersistentClient(path="chroma_db")
    vecteor_chunk = client.get_collection(name="vecteor_chunk")

    
    question_embedding = model.encode(question)

    results = vecteor_chunk.query(
    query_embeddings=[question_embedding],
    n_results=k
    #k, c’est le nombre de chunks que tu veux récupérer : les k plus proches de la question
)
    return results["documents"][0], results["metadatas"][0], results["distances"][0]


def ask_llm(question, model, k):
  response = chat(
    model="mistral",
    messages=[{"role": "user", "content": "Explique une API REST en 3 phrases simples"},
              {"role": "system", "content": "Tu es un expert science, tu reçois une question et également le contenue des k chunks les plus proches de la question. Tu dois répondre à la question en utilisant uniquement le contenue des k chunks. Si tu ne trouves pas la réponse dans les k chunks, tu réponds que tu ne sais pas."}]
)

  
print(response["message"]["content"])