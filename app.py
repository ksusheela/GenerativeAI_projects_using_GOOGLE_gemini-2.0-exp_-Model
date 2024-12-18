# Q&A Chatbot
#from langchain.llms import OpenAI

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#GOOGLE_API_KEY = "AIzaSyA9F698GzPkSWke_GdknKSesZotk5tcg2M"

import os
os.environ["GEMINI_API_KEY"] = 'AIzaSyCjeeQfMzSul5-bD0BzbZbWojkt4vhXzuc'

import google.generativeai as genai
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
