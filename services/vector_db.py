from uuid import uuid4

from langchain_chroma import Chroma

from services.ai_models import openai_embedding, google_genai_embedding


def vector_db() -> Chroma:
    db_directory = "./db"
    db = Chroma(
        collection_name="product_collection",
        persist_directory=db_directory,  # folder, where vectordb stored.
        embedding_function=google_genai_embedding()  # embedding model
    )
    return db


def add_to_vector(documents):
    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store = vector_db()
    vector_store.add_documents(documents=documents, ids=uuids)
    return vector_store
