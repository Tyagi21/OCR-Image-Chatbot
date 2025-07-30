from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["ocr_chatbot"]  # Make sure this matches with app.py and chat_utils.py
collection = db["document_chunks"]  # This is the collection for storing chunks

# Load sentence-transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to split long text into smaller chunks
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    chunk_id = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append({"chunk_id": chunk_id, "text": chunk})
        start += chunk_size - overlap
        chunk_id += 1
    return chunks

# Function to store chunks and their embeddings in MongoDB
def store_chunks(chunks):
    from sentence_transformers import SentenceTransformer
    import numpy as np
    from mongodb import get_collection

    model = SentenceTransformer("all-MiniLM-L6-v2")
    collection = get_collection()

    collection.delete_many({})  # clear old entries

    for chunk in chunks:
        text = chunk["text"]  #  Extract the actual text
        embedding = model.encode(text).tolist()

        doc = {
            "chunk_id": chunk["chunk_id"],
            "text": text,
            "embedding": embedding
        }
        collection.insert_one(doc)

    print(f"Stored {len(chunks)} chunks in MongoDB.")