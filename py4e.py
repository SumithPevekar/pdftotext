import sys
import PyPDF2

pdfFileObj = open('C://Users//username//Downloads//Arihant-general_knowledge.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)
for i in range(1,1251):

    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

pdfFileObj.close()