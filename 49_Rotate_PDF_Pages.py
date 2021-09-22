import PyPDF2

pdf_r = PyPDF2.PdfFileReader("pdf1.pdf")
pdf_w = PyPDF2.PdfFileWriter()

pdf_r2 = PyPDF2.PdfFileReader("pdf2.pdf")
pdf_w2 = PyPDF2.PdfFileWriter()

print(pdf_r.getPage(0))
# print(pdf_r.getPage(1))      # ==> Out of Range

page = pdf_r.getPage(0).rotateClockwise(90)
pdf_w.addPage(page)

with open("Change1.pdf", "wb") as f:
    pdf_w.write(f)

page2 = pdf_r2.getPage(0).rotateCounterClockwise(90)
pdf_w2.addPage(page2)

with open("Change2.pdf", "wb") as f2:
    pdf_w2.write(f2)