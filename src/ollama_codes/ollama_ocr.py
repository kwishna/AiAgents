import base64
import requests
from PIL import Image

SYSTEM_PROMPT = """You should act as an OCR assistant you is very intelligent at extracting text from an image. Analyze the provided image and:
    1. Recognize all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the text.
    3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
    Provide only the transcription without any additional comments.
"""

def encode_image_to_base64(image_path):
    """Convert an image file to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def perform_ocr(image_path):
    """Perform OCR on the given image using Llama 3.2-Vision."""
    base64_image = encode_image_to_base64(image_path)
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2-vision",
            "messages": [
                {
                    "role": "user",
                    "content": SYSTEM_PROMPT,
                    "images": [base64_image],
                },
            ],
        }
    )
    if response.status_code == 200:
        return response.json().get("message", {}).get("content", "")
    else:
        print("Error:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    image_path = "/Users/krishna/Documents/grocery_receipt.png"
    result = perform_ocr(image_path)
    if result:
        print("OCR Recognition Result:")
        print(result)