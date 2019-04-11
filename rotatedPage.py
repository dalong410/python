import PyPDF2

minutesFile = open('d:/python/meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

resultPdfFile = open('d:/python/rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
minutesFile.close()

print("작업이 완성되었습니다.")
      
