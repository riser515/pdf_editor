import PyPDF2

pdf = PyPDF2.PdfFileReader("pdf1.pdf")

print(pdf.getPage(0).extractText())