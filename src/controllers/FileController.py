import os
from src.models.basic import getOpenAIResponse
from src.utils.fileReader import extractTextFromImage, extractTextFromPdf
from src.utils.onlineFileReader import readFileFromWeb


class FileController:

    def __init__(self):
        self.test = "test data"

    async def getBillMetadata(self, url):
        try:
            if url:
                text = readFileFromWeb(url)
            else:
                cwd = os.getcwd()
                jpgInvoicePath = os.path.join(cwd, 'src/invoice.jpg')
                text = extractTextFromImage(jpgInvoicePath)
                # pdfInvoicePath = 'invoice.pdf'
                # print(jpgText)
                # pdfText = extractTextFromPdf(pdfInvoicePath)
                # print("\nText extracted from PDF:")
                # print(pdfText)

            result = getOpenAIResponse(text)
            return result
        except Exception as e:
            print(e)
            return {"error": "Oops! error"}
