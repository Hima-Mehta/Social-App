import os
import pandas as pd
import pdfplumber    # scope of improvement here some other library
import pytesseract
import cv2
from PIL import Image
#import docx

# Set Tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # change if on Windows

# -------- PDF Extractor --------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

# -------- Image OCR --------
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(image)
    return text.strip()

# -------- Excel Reader --------
def extract_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# -------- Word Doc Parser --------
# def extract_text_from_docx(file_path):
#     doc = docx.Document(file_path)
#     return "\n".join([para.text for para in doc.paragraphs])

# -------- Ingest Dispatcher --------
def ingest_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext in ['.pdf']:
        return extract_text_from_pdf(file_path)
    elif ext in ['.jpg', '.jpeg', '.png']:
        return extract_text_from_image(file_path)
    elif ext in ['.xlsx']:
        return extract_data_from_excel(file_path)
    # elif ext in ['.docx']:
    #     return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")