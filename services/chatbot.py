from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from services.ai_models import openai_llm, google_genai_llm
from services.vector_db import vector_db, add_to_vector
from services.data_processing import data_processing


def init_chat_history():
    ### Contextualize question ###
    contextualize_q_system_prompt = (
        "You are a conversational assistant specializing in beauty products. Given the chat history "
        "and the latest user question, which may reference context in the chat history, "
        "rephrase the question as a clear, standalone query without using previous chat details. "
        "Do not answer the question; only reformulate it to make sense on its own."
    )
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    retriever = vector_db().as_retriever()
    history_aware_retriever = create_history_aware_retriever(
        google_genai_llm(), retriever, contextualize_q_prompt
    )

    ### Answer question ###
    system_prompt = (
        "You are a professional beauty consultant for an online cosmetics shop. Use the following "
        "pieces of retrieved context to answer the user's questions about our beauty products"
        ". Your goal is to give expert, friendly advice tailored to their unique needs and questions."
        "If the answer is not available, politely inform the user. \n\n"
        "{context}"
    )
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(google_genai_llm(), qa_prompt)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    ### Statefully manage chat history ###
    store = {}

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    return conversational_rag_chain


def chatbot(messages: str):
    """
    documents = data_processing()
    vector_store = add_to_vector(documents)
    results = vector_store.similarity_search(
        messages,
        k=2,
    )
    """
    conversational_rag_chain = init_chat_history()
    results = conversational_rag_chain.invoke(
        {"input": messages},
        config={"configurable": {"session_id": "abc123"}},
    )["answer"]

    return results
