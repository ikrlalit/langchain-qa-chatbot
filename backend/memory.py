from langchain.memory import ConversationBufferMemory

# Store chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

