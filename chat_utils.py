from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util
from datetime import datetime
from ai21 import AI21Client
from ai21.models.chat.chat_message import SystemMessage, UserMessage
import torch

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["ocr_chatbot"]
chunk_collection = db["document_chunks"]
chat_collection = db["chat_history"]

# Embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# AI21 setup
ai21_client = AI21Client(api_key="883b6b4f-3082-4a75-b4c8-189ed7dc7bec")  # Replace with your actual API key

# ---- Function to fetch top relevant chunks ----
def fetch_relevant_chunks(query, top_k=3):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    all_chunks = list(chunk_collection.find({}))

    scored_chunks = []
    for chunk in all_chunks:
        chunk_embedding = torch.tensor(chunk["embedding"])
        similarity = util.cos_sim(query_embedding, chunk_embedding)[0].item()
        scored_chunks.append((chunk, similarity))

    # Sort by similarity descending
    scored_chunks.sort(key=lambda x: x[1], reverse=True)
    return scored_chunks[:top_k]

# ---- Function to log chat history ----
def log_chat(session_id, role, message):
    chat_collection.insert_one({
        "session_id": session_id,
        "role": role,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    })

# ---- Main function to interact with AI21 ----
def ask_ai21(user_query, session_id):
    # Fetch top relevant chunks
    top_matches = fetch_relevant_chunks(user_query, top_k=3)
    print("Top matches and their scores:", [(i+1, score) for i, (chunk, score) in enumerate(top_matches)])

    if top_matches[0][1] < 0.5:
        return "Sorry, I can only answer questions based on the uploaded document."

    # Extract top context
    context = "\n".join([chunk["text"] for chunk, score in top_matches])

    # Build chat messages
    messages = [
        SystemMessage(content="You are an expert assistant. Answer based on the provided document."),
        UserMessage(content=f"Document: {context}"),
        UserMessage(content=user_query)
    ]

    # Call AI21
    response = ai21_client.chat.completions.create(
        model="jamba-large",
        messages=messages,
        max_tokens=250
    )

    answer = response.choices[0].message.content.strip()

    # Log chat
    log_chat(session_id, "user", user_query)
    log_chat(session_id, "assistant", answer)

    return answer