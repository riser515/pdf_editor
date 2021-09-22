import PyPDF2


def split_pdf(path, name_of_pdfs):
    pdf_r = PyPDF2.PdfFileReader(path)
    for page in range(pdf_r.getNumPages()):
        pdf_w = PyPDF2.PdfFileWriter()
        pdf_w.addPage(pdf_r.getPage(page))

        out = f"{name_of_pdfs}_Page{page+1}.pdf"
        with open(out, "wb") as o:
            pdf_w.write(o)


split_pdf("Change3.pdf", "Change4.pdf")