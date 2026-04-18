import pdfplumber

def extract_pages(file):
    pages = []

    with pdfplumber.open(file.file) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            pages.append({
                "page_number": i + 1,
                "text": text
            })

    return pages