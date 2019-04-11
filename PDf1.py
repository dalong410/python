import PyPDF2
import re

pdfFileObj = open('d:/python/meetingminutes.pdf','rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)         

text = str(pageObj.extractText())

quotes = re.findall(r'"[^"]*"',text)

for quote in quotes:
    print (quote)

print (text)
