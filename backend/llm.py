from langchain_groq import ChatGroq
from .config import GROQ_API_KEY

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile", 
    temperature=0.7,
    api_key=GROQ_API_KEY
)

