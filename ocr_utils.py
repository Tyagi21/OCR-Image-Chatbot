import os
from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        return "Image not found."

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error processing image: {str(e)}"

# === Test Run (Optional) ===
if __name__ == "__main__":
    image_path = "sample_inputs/example_image.png"
    text = extract_text_from_image(image_path)
    print("Extracted text:\n", text)
