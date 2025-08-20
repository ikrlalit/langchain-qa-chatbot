from langchain.chains import ConversationalRetrievalChain
from .llm import llm
from .memory import memory

def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )

