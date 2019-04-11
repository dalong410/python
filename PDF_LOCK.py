import PyPDF2

pdfFile = open('d:/python/meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('apple')
resultPdf = open('d:/python/apple.pdf', 'wb')

pdfWriter.write(resultPdf)
resultPdf.close()

print("작업이 완료되었습니다")
