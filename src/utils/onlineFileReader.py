import requests
from io import BytesIO
from PIL import Image
import PyPDF2
import pytesseract


def readFileFromWeb(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content

        if any(url.lower().endswith(ext) for ext in [".pdf", ".PDF"]):
            pdf_reader = PyPDF2.PdfReader(BytesIO(content))
            # Extract text from the PDF
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            print(text)
            return text

        if any(url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".PNG", ".JPG", ".JPEG"]):
            image = Image.open(BytesIO(content))
            text = pytesseract.image_to_string(image)

            print(text)
            return text

        print("Invalid file formate")
        return None

    else:
        print("Failed to retrieve the file. Status code:", response.status_code)
        return None
