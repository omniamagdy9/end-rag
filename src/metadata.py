from typing import List
from langchain_core.documents import Document

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


prompt = ChatPromptTemplate.from_template("""
You are a PDF page summarizer.

Write a short semantic description for the page.

Rules:
- Maximum 1 sentence
- Focus on the page topic
- Ignore OCR garbage
- Keep it concise

Page:
{page_text}
""")

chain = prompt | llm | StrOutputParser()



def describe_page(text: str) -> str:
    clean = " ".join(text.replace("\n", " ").split())

    if not clean:
        return "Empty or OCR-unreadable page"

    try:
        summary = chain.invoke({
            "page_text": clean[:4000]
        })

        return summary.strip()

    except Exception:
        return clean[:120]



def add_page_descriptions(docs: List[Document]) -> List[Document]:
    """
    Adds a short description to every page-level document.
    """
    for doc in docs:
        doc.metadata["page_description"] = describe_page(doc.page_content)
    return docs