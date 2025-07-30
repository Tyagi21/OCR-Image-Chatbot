from ocr_utils import extract_text_from_image
from vector_utils import chunk_text, store_chunks
from chat_utils import ask_ai21
import uuid

# Path to your sample image
image_path = "final_project_igt/sample_inputs/Screenshot (199).png"


# Step 1: OCR - Extract text from the image
text = extract_text_from_image(image_path)

if text:
    # Step 2: Vector DB - Chunk and store embeddings
    chunks = chunk_text(text)
    if chunks:
        store_chunks(chunks)

        # Step 3: Chat interaction
        print("\nChatbot is ready. Ask me anything based on the uploaded image!\n")
        session_id = str(uuid.uuid4())

        while True:
            user_question = input("Ask a question (or type 'exit' to quit): ")
            if user_question.lower() == "exit":
                print("Exiting. Thank you!")
                break

            answer = ask_ai21(user_question, session_id)
            print("Answer:", answer)
    else:
        print("No chunks created. Please check the extracted text.")
else:
    print("OCR failed or returned no text.")
