import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

# Load environment variables
load_dotenv()
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'you are a helpful system. Please respond to queries.'),
        ('user', "question: {question}")
    ]
)

# Streamlit UI setup
st.title('Langchain Demo With Ollama3')
user_input = st.text_input('Enter Some Text')

# Setup Ollama LLM
llm = Ollama(model='llama3')
output_parser = StrOutputParser()

# Create LLM chain
chain = LLMChain(prompt=prompt, llm=llm, output_parser=output_parser)

# Invoke the chain if user input is provided
if user_input:
    response = chain.invoke({'question': user_input})
    st.write(response)


