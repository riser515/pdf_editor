import PyPDF2


with open("pdf1.pdf", 'rb') as f:                    # Not writing rb will give an error.
    pdf = PyPDF2.PdfFileReader(f)
    print(f)
    print(pdf)
    print(pdf.numPages)

    info = pdf.getDocumentInfo()
    np = pdf.getNumPages()

details = f"""
    Author : {info.author}
    Title : {info.title}
    Number of Pages : {np}
"""

print(details)