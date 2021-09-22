import PyPDF2


def pdf_to_text(input_pdf, output_text):
    pdf = PyPDF2.PdfFileReader(input_pdf)

    with open(output_text, "w", encoding='utf-8') as o:
        for page in range(pdf.getNumPages()):
            data = pdf.getPage(page).extractText()
            o.write(data)


pdf_to_text("Change3.pdf", "Change7.txt")
pdf_to_text("Logo.pdf", "Change8.txt")
