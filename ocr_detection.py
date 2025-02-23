import easyocr

def perform_ocr(image_path):
    # Load OCR model for English
    reader = easyocr.Reader(['en'])
    
    # Read text from the image
    results = reader.readtext(image_path)

    # Print extracted text
    for (bbox, text, prob) in results:
        print(f"Detected text: {text} (Confidence: {prob:.2f})")

if __name__ == "__main__":
    image_path = "your_image.jpg"  # Replace with your image path
    perform_ocr(image_path)
