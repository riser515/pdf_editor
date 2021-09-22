import PyPDF2


def watermark_pdf(path, out, watermark):
    watermark_r = PyPDF2.PdfFileReader(watermark)
    water_page = watermark_r.getPage(0)

    pdf_r = PyPDF2.PdfFileReader(path)
    pdf_w = PyPDF2.PdfFileWriter()

    for page in range(pdf_r.getNumPages()):
        p = pdf_r.getPage(page)
        p.mergePage(water_page)
        pdf_w.addPage(p)

    with open(out, "wb") as o:
        pdf_w.write(o)


watermark_pdf("Change3.pdf", "Change5.pdf", "Logo_2.pdf")

# Optional (Fixed the Watermarked File) :-

# import PyPDF2
#
#
# def watermark_pdf(path, out):
#     watermark = "logo_2.pdf"
#     watermark_r = PyPDF2.PdfFileReader(watermark)
#     water_page = watermark_r.getPage(0)
#
#     pdf_r = PyPDF2.PdfFileReader(path)
#     pdf_w = PyPDF2.PdfFileWriter()
#
#     for page in range(pdf_r.getNumPages()):
#         p = pdf_r.getPage(page)
#         p.mergePage(water_page)
#         pdf_w.addPage(p)
#
#     with open(out, "wb") as o:
#         pdf_w.write(o)
#
#
# watermark_pdf("Change3.pdf", "Change5.pdf")