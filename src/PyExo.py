import os
from DocumentTextDetection import ExtractData
import fitz
import docx2txt
from DocumentObject import CaptureData

class PyExo():
    def __init__(self):
        pass

    def Extract_From_Doc(wordFile):

        if str(wordFile).endswith(".docx"):
            text = docx2txt.process(wordFile, r"src\\wordtoimg")
            
            folder_path = 'src/wordtoimg'
            arr = []
            paths = os.listdir(folder_path)
            for path in paths:
                fpath = folder_path+'/'+path
                arr.append(fpath)
            if len(arr) == len(paths):
                return arr
        else:
            print("Provide Word document")
            return []

    def Extract_From_Pdf(pdfFile):
        print(pdfFile)
        if str(pdfFile).endswith(".pdf"):
            doc = fitz.open(pdfFile)
            for page_number in range(doc.page_count):
                page = doc[page_number]
                pix = page.get_pixmap()
                if (os.path.exists(os.path.join(os.getcwd()+'\\src', 'pdftoimg'))):
                    pass
                else:
                    os.mkdir(os.path.join(os.getcwd()+'\\src', 'pdftoimg'))
                filePath = os.getcwd()+f'\\src\\pdftoimg\\{page_number}.png'
                pix.save(filePath)
                folder_path = 'src/pdftoimg'
                arr = []
                paths = os.listdir(folder_path)
                for path in paths:
                    fpath = folder_path+'/'+path
                    arr.append(fpath)
                if len(arr) == doc.page_count:
                    return arr
        else:
            print("Provide pdf document")
            return []

    def ExtractDocumentsData(filePaths):
        if len(filePaths) > 0:
            for x in range(0,len(filePaths)):
                ExtractData(filePaths[x])

                if x == len(filePaths)-1:
                    
                    try:
                        CaptureData()
                    except:
                        print("Error")

    def Extract_From_Images(folderPath):

        

        if str(folderPath).endswith('.pdf') or str(folderPath).endswith('.docx'):
            pass
        else:
            folder_path = 'src/test'
            arr = []
            paths = os.listdir(folder_path)
            for path in paths:
                fpath = folder_path+'/'+path
                arr.append(fpath)
            return arr
      


# files = PyExo()
# files.ExtractDocumentsData()
