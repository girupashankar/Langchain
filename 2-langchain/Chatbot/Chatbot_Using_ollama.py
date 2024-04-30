# opean ai
from langchain_openai import ChatOpenAI
# open source model
from langchain_community.llms import ollama
# langchain chat template
from langchain_core.prompts import ChatPromptTemplate
# langchain output parser
from langchain_core.output_parsers import StrOutputParser
# web app-framework
import streamlit as st 
# load env variables    
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

# PROMPT Template
prompt = ChatPromptTemplate.format_messages(
     [
         ("System", "You are a helpfull assistant, Please response to the queries."),
         ("User", "Question:{question}")
     ]
 )
 
# streamlit framework
st.title("Langchain Demo With Ollama llama3")
input_text=st.text_input("Enter your question")

# ollama llama3 LLM
llm=ollama(model="llama-3")
output_parser=StrOutputParser()
chains=prompt|llm|output_parser

if input_text:
    st.write(chains.invoke({'question':input_text}))