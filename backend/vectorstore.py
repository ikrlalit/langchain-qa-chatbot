from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader

# Build vector store from a PDF
def create_vectorstore_from_pdf(file_path: str):
    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)

    # Embeddings (local model, no API key needed)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Store in FAISS
    return FAISS.from_documents(split_docs, embeddings)

