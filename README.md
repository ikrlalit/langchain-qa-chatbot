# 📄 Document Q&A Chatbot (Groq + LangChain + Streamlit)

A **conversational AI chatbot** that lets users **upload documents (PDF/TXT)** and ask questions about them.  
It uses:

- **Groq Cloud LLMs** 🚀 for superfast responses  
- **LangChain** 🔗 for chaining prompts, memory, and retrieval  
- **HuggingFace Embeddings** 🤗 + **FAISS** for local vector search  
- **Streamlit** 🎨 for the interactive UI  

---

## ✨ Features
- 📤 Upload a **PDF/TXT file**
- 🤖 Ask **questions** about the uploaded document
- 🧠 **Conversational memory** to maintain context
- 🔎 **Retrieval-Augmented Generation (RAG)** using FAISS vector search
- ⚡ **Groq-powered LLM** for fast and accurate answers
- 🎛️ Modular backend (`llm.py`, `chains.py`, `vectorstore.py`)  

---

## 🏗️ Project Structure
```
qa_chatbot/
│── app.py                   # Streamlit app (UI)
│── requirements.txt         # Dependencies
│── .env                     # Secrets (API keys)
│
├── backend/
│   ├── config.py            # Load environment variables
│   ├── llm.py               # Groq LLM setup
│   ├── vectorstore.py       # PDF/Text loader + FAISS embeddings
│   ├── memory.py            # Chat memory handler
│   └── chains.py            # Q&A retrieval chain
│
├── data/
│   └── sample.txt           # Example document
│
└── tests/
    └── test_chain.py        # Unit tests
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/qa_chatbot.git
cd qa_chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the project root:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

👉 Get your Groq API key from [Groq Console](https://console.groq.com/).

---

## ▶️ Running the App
Start the Streamlit server:
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser. 🎉

---

## 🖥️ Usage
1. Upload a **PDF** or **TXT** file.  
2. Type your question in the chat box.  
3. The chatbot will:
   - Embed and index the document with **HuggingFace + FAISS**  
   - Retrieve the most relevant chunks  
   - Pass them into a **Groq LLM** via LangChain  
   - Return a natural language answer  

---

## 🔧 Tech Stack
- **LLM**: Groq Cloud (e.g., `llama-3.3-70b-versatile`)
- **Framework**: LangChain
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
- **Vector DB**: FAISS
- **Frontend**: Streamlit
- **Memory**: LangChain ConversationBufferMemory

---

## 📌 Example
Upload a **Company Policy PDF** and ask:

```
Q: What is the annual leave policy?
A: Employees are entitled to 24 paid leaves per year...
```

---

## 🚀 Future Enhancements
- 📑 Support **DOCX/Word uploads**
- 🗄️ Multi-file ingestion
- 💾 Persist vector DB for re-using documents
- 🌐 Add external tools (Web Search, SQL DB)
- 🔒 Authentication for multi-user usage

---

## 🧪 Testing
Run unit tests:
```bash
pytest tests/
```

---

## 🤝 Contributing
Contributions are welcome!  
- Fork the repo  
- Create a new branch  
- Commit changes  
- Open a Pull Request  

---

## 📜 License
This project is licensed under the **MIT License**.  
