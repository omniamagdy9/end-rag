from loaders import load_pdf_pages
from ocr import needs_ocr, ocr_pdf_pages
from metadata import add_page_descriptions


PDF_PATH = "../data/raw/andrew-ng-machine-learning-yearning.pdf"


# 1) Load PDF
docs = load_pdf_pages(PDF_PATH)


# 2) OCR if needed
if needs_ocr(docs):

    print("Using OCR...")

    docs = ocr_pdf_pages(PDF_PATH)

else:

    print("Using PyPDFLoader...")


# 3) Add summaries
docs = add_page_descriptions(docs)


# 4) Print first 3 pages
for doc in docs[:10]:

    print("\n" + "=" * 50)

    print("PAGE:", doc.metadata["page_number"])

    print("\nSUMMARY:")
    print(doc.metadata.get("page_description"))

    print("\nCONTENT SAMPLE:")
    print(doc.page_content[:300])



docs = add_page_descriptions(
    docs,
    limit=5
)   