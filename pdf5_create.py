import PyPDF2

pdf1File = open('d:/python/meetingminutes.pdf', 'rb')
pdf2File = open('d:/python/lambda.pdf', 'rb')    

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter() # represents a blank PDF

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('d:/combin.pdf', 'wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()

pdf1File.close()
pdf2File.close()

