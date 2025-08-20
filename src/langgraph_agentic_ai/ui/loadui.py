import streamlit as st

from src.langgraph_agentic_ai.ui.uiconfigfile import Config

class LoadStrealitui:  # class to load streamlit frontend
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_pagetitle(), layout="wide")
        st.header(self.config.get_pagetitle())

        # adding sidebar
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            use_case_options = self.config.get_usecase_options()

            # adding selectbox in sidebar for llm/model selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select groq model", model_options)

                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
            
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter the GROQ API Key to proceed")

            # adding selectbox in sidebar for usecase
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", use_case_options)
        return self.user_controls
        
            
