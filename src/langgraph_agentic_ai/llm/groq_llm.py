import os
import streamlit as st 
from langchain_groq import ChatGroq


class groqllm:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input
        
    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls["GROQ_API_KEY"]
            groq_model = self.user_controls["selected_groq_model"]
            if groq_api_key == '':
                st.error("Please enter the GROQ API Key")

            if groq_model == '':
                st.error("Please select a Groq model")
                
            llm = ChatGroq(model=groq_model, groq_api_key=groq_api_key)
        except Exception as e:
            raise Exception(f"Error initializing Groq LLM: {str(e)}")
        
        return llm
