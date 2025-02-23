from flask import Flask, request, jsonify, render_template
import easyocr
import os
import base64
import numpy as np
import cv2
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
reader = easyocr.Reader(['en'])  # Load OCR model for English

@app.route('/')
def home():
    return render_template('index.html')  # Serve the index.html file

@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        data = request.get_json()
        image_data = data['image']  # Get the base64 image data
        # Decode the base64 image data
        header, encoded = image_data.split(',', 1)
        image_bytes = base64.b64decode(encoded)
        # Convert bytes to a NumPy array
        np_array = np.frombuffer(image_bytes, np.uint8)
        # Decode the image using OpenCV
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        logging.debug('Image processed for OCR.')  # Log when image is processed
        # Perform OCR
        result = reader.readtext(image)
        logging.debug(f'OCR result: {result}')  # Log the OCR result
        if not result:
            return jsonify({'error': 'No text detected'}), 400
        detected_text = ' '.join([text[1] for text in result])
        return jsonify({'detected_text': detected_text})
    except Exception as e:
        logging.error(f'Error during OCR: {str(e)}')  # Log any errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
