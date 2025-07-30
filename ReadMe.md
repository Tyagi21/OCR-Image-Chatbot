# OCR-Based Image Chatbot with MongoDB & AI21 Integration🤖

This project is an interactive chatbot that extracts text from images using OCR (Tesseract), stores the content in MongoDB as vector embeddings using Sentence Transformers, and lets users query the content through natural language using AI21 Studio’s Jurassic-2 language model.

---

## Features

- OCR (Optical Character Recognition) from uploaded image  
- Chunking of extracted text for vector embedding  
- Storage of embeddings in MongoDB  
- Chatbot interface using AI21 (Jurassic-2 model)  
- Question-answering based on image content  
- Session ID tracking for chatbot memory  
- Resume previous session support

---

## Technologies Used

- Python 3.13+
- Tesseract OCR  
- pytesseract  
- Pillow  
- Sentence Transformers (`all-MiniLM-L6-v2`)  
- MongoDB (local)  
- AI21 Studio (Jurassic-2)

---

## Folder Structure

final_project_igt/
├── app.py # Main script to run OCR and chatbot
├── ocr_utils.py # Handles text extraction from images
├── vector_utils.py # Text chunking and vector embedding storage
├── chat_utils.py # Handles similarity search and AI21 querying
├── sample_inputs/
│ └── Screenshot (199).png # Sample image for OCR
├── requirements.txt # Python dependencies
├── README.md # Project overview


---

## How to Run

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Install Tesseract OCR:**

    Download from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract) and add it to your system path.

3. **Place your image** in `sample_inputs/` (e.g., `Screenshot (199).png`)

4. **Run the app:**

    ```bash
    python app.py
    ```

5. **Ask questions** about the document content!

---

## Example Questions

- What is aviation?
- Who invented the first powered airplane?
- When did jet engines become widely used?

---

## Output

- Extracted text printed in terminal  
- Chunks and embeddings stored in MongoDB (`ocr_chatbot.document_chunks`)  
- Interactive chatbot responses in console  

---

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Sentence Transformers](https://www.sbert.net/)
- [AI21 Labs](https://www.ai21.com/)

---

✅**Project developed as part of internship final submission**  
