from transformers import Conversation, ConversationChain
from transformers_openai import ChatOpenAI
from transformers_core.prompts import ChatPromptTemplate
from transformers_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LLAMA2_API_KEY"] = os.getenv("LLAMA2_API_KEY")  # Replace with appropriate key for LLaMA2

# Prompt template setup
prompt = ChatPromptTemplate(
    messages=[
        ("system", "you are a helpful assistant. please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit setup
st.title('LLaMA2 with OpenAI API')
input_text = st.text_input("Ask a question")

# Initialize the model (assuming LLaMA2 model setup)
llm = ChatOpenAI(model='gpt-3.5-turbo')  # Adjust model initialization as per LLaMA2 setup
output_parser = StrOutputParser()  # Ensure output parsing setup

# Create the conversation chain
conversation = ConversationChain.from_template(prompt, llm, output_parser)

# Processing input text
if input_text:
    response = conversation.invoke({"question": input_text})
    st.write(response)
