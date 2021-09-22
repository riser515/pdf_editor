import PyPDF2


def set_password(path, out, password):
    pdf_r = PyPDF2.PdfFileReader(path)
    pdf_w = PyPDF2.PdfFileWriter()

    for page in range(pdf_r.getNumPages()):
        pdf_w.addPage(pdf_r.getPage(page))

    pdf_w.encrypt(user_pwd=password, owner_pwd="Khushi", use_128bit=True)

    with open(out, "wb") as o:
        pdf_w.write(o)


set_password("Change3.pdf", "Change6.pdf", "file password")