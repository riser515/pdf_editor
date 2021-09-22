import PyPDF2


def merge_pdf(paths, out):
    pdf_w = PyPDF2.PdfFileWriter()
    for path in paths:
        pdf = PyPDF2.PdfFileReader(path)
        for page in range(pdf.getNumPages()):
            pdf_w.addPage(pdf.getPage(page))

    with open(out, "wb") as o:
        pdf_w.write(o)


# merge_pdf(["pdf1.pdf", "pdf2.pdf"], "Change3.pdf")
merge_pdf(["Mainpage.pdf", "abstractandacknowledgement.pdf", "index.pdf", "Content-Modified.pdf"], "DE.pdf")