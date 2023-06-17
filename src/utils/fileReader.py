import pytesseract
import PyPDF2
from PIL import Image


# Extract text from image file
# Using tesseract package
# @param {str} imagePath img path
# @return {str} image text
def extractTextFromImage(imagePath: str):
    image = Image.open(imagePath)
    text = pytesseract.image_to_string(image)
    return text


# Extract text from pdf file
# @param {str} pdfPath pdf path
# @return {str} image text
def extractTextFromPdf(pdfPath):
    text = ""
    with open(pdfPath, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
