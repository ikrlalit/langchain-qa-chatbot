import streamlit as st
import tempfile
from backend.vectorstore import create_vectorstore_from_pdf
from backend.chains import build_qa_chain

st.title("📄 PDF Q&A Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Save PDF to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Build vectorstore from PDF
    vectorstore = create_vectorstore_from_pdf(tmp_path)
    qa_chain = build_qa_chain(vectorstore)

    query = st.text_input("Ask a question about the PDF:")
    if query:
        response = qa_chain.run(query)
        st.write(response)

