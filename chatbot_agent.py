import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

# Load your Groq API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq Chat LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=400,
    timeout=None,
    max_retries=2,
)

# Prompt template
prompt_temp = PromptTemplate(
    input_variables=["input", "history"],
    template="""
You are a helpful AI assistant.
Conversation so far:
{history}
Human: {input}
AI:
"""
)

# Memory to keep conversation context
memory = ConversationBufferMemory(memory_key="history")

# Create chain
chain = LLMChain(llm=llm, prompt=prompt_temp, memory=memory)

def get_chatbot_response(user_input):
    try:
        return chain.run({"input": user_input})
    except Exception as e:
        return f"Error: {str(e)}"


