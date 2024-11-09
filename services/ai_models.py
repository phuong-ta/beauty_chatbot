import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


def openai_embedding():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = ""

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
    )
    return embeddings


def openai_llm():
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = ""

    llm = ChatOpenAI(model="gpt-4o",
                     temperature=0,
                     max_tokens=None,
                     timeout=None,
                     max_retries=2,
                     )
    return llm


def google_genai_embedding():
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = ""

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings


def google_genai_llm():
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = ""
    llm = GoogleGenerativeAI(model="gemini-pro",
                             google_api_key=os.getenv("GOOGLE_API_KEY"),
                             temperature=0,
                             max_tokens=None,
                             timeout=None,
                             max_retries=2,
                             )
    return llm
