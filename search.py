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

    documents, metadatas, distances = search(question, model, k)
    list_doc_meta = []

    for document, metadata in zip(documents, metadatas):
        list_doc_meta.append(f"Chunk: {document}\nSource: {metadata}")
    list_doc_meta.append(f"\nQuestion: {question}\n")
    resultat = "\n".join(list_doc_meta)
    print(f"Résultat de la recherche: {resultat}")
    

    response = chat(
    model="mistral",
    messages=[{"role": "system", "content": "Tu es un expert science, tu reçois une question et également le contenue des chunks les plus proches de la question. Tu dois répondre à la question en utilisant uniquement le contenue des k chunks. Si tu ne trouves pas la réponse dans les k chunks, tu réponds que tu ne sais pas. Une fois avoir répondu, je voudrais que tu affiches les sources utilisées pour répondre à la question ( elles sont dans se que je te donne). Tu dois répondre en français."},
              {"role": "user", "content": resultat}
              ]
)

  
    return response["message"]["content"]