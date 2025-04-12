# Text-Recognition-Python-EasyOCR

## Project Overview
Text-Recognition-Python-EasyOCR is a web-based application that uses computer vision and Optical Character Recognition (OCR) to detect and extract text from live camera feed in real-time.

## Features
- Live camera text detection
- Web-based interface
- Instant text recognition
- Supports English language text extraction

## Technologies Used
- Python
- Flask
- EasyOCR
- OpenCV
- JavaScript
- HTML5

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Eng-M-Abdrabbou/Text-Recognition-Python-EasyOCR.git
cd Text-Detection-Python-EasyOCR

```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:5000`

## How It Works
1. The web application accesses your device's camera
2. Click the "Detect Text" button
3. The application captures a frame from the camera
4. The frame is sent to the server for text detection
5. Detected text is displayed on the screen

## Screenshot

<img src="\Images\1.png" width="600" height="350" />

## Limitations
- Currently supports only English text
- Requires a modern web browser with camera access
- Performance depends on camera quality and text visibility

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Mahmoud Abdrabbou - mahmoud.f.abdrabbou@gmail.com

## Acknowledgments
- EasyOCR for powerful OCR capabilities
- Flask for web framework
- OpenCV for image processing
