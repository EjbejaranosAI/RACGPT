import pdfquery
import PyPDF2


def reader(pdf_path):

    pdf = pdfquery.PDFQuery(pdf_path)
    pdf.load()
    total_pages = pdf.doc.catalog['Pages'].resolve()['Count']

    return total_pages      

def extract(pdf_path):
    pages = []

    with open(pdf_path,"rb") as file:
        reader = PyPDF2.Pdfreader(file)

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text_content = page.extract_text()
            pages.append(["Page:" + str(page_num + 1), text_content])


    return pages

