from pathlib import Path
from typing import List
import time

from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq


# Load .env
load_dotenv(
    dotenv_path=Path(__file__).resolve().parent.parent / ".env"
)


# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


# Prompt
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


# Chain
chain = prompt | llm | StrOutputParser()


def describe_page(text: str) -> str:
    """
    Generate semantic page summary using Groq LLM.
    """

    clean = " ".join(
        text.replace("\n", " ").split()
    )

    if not clean:
        return "Empty or OCR-unreadable page"

    try:

        summary = chain.invoke({
            "page_text": clean[:4000]
        })

        return summary.strip()

    except Exception as e:

        print(f"Summary Error: {e}")

        return clean[:120]


def add_page_descriptions(
    docs: List[Document],
    limit: int = 10
) -> List[Document]:

    for doc in docs[:limit]:

        doc.metadata["page_description"] = describe_page(
            doc.page_content
        )

        time.sleep(2)

    return docs