from pathlib import Path
from typing import List

import pytesseract
import pypdfium2 as pdfium

from langchain_core.documents import Document


def ocr_pdf_pages(
    file_path: str,
    scale: int = 2
) -> List[Document]:
    """
    OCR scanned PDF pages using pypdfium2 + pytesseract.
    """

    path = Path(file_path)

    pdf = pdfium.PdfDocument(str(path))

    docs: List[Document] = []

    for i, page in enumerate(pdf):

        bitmap = page.render(scale=scale).to_pil()

        text = pytesseract.image_to_string(bitmap)

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "source": path.name,
                    "file_path": str(path),
                    "page_number": i + 1,
                    "loader": "OCR",
                }
            )
        )

    return docs


def needs_ocr(
    docs: List[Document],
    min_chars_per_page: int = 40
) -> bool:
    """
    Detect if PDF extraction quality is weak.
    """

    if not docs:
        return True

    weak_pages = 0

    for doc in docs:

        text = doc.page_content.strip()

        # Very short pages
        if len(text) < min_chars_per_page:
            weak_pages += 1
            continue

        # Broken extraction detection
        weird_ratio = sum(
            c.isupper() for c in text
        ) / max(len(text), 1)

        if weird_ratio > 0.3:
            weak_pages += 1

    return weak_pages / len(docs) > 0.3