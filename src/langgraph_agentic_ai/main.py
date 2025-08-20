import streamlit as st
from src.langgraph_agentic_ai.ui.loadui import LoadStrealitui
from src.langgraph_agentic_ai.llm.groq_llm import groqllm
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.display_output import DisplayOutput


# main function links the streamlit ui 
def load_langgraph_agentic_app():
    """
    Loads and runs the langgraph agentic ai application with streamlit
    This function initialises the UI, captures users input, configures LLM Model,
    setup the graph based on the selected usecase, and displays the output while implementing
    exception handling
    """
    # Load UI
    straemlitui = LoadStrealitui()
    user_input = straemlitui.load_streamlit_ui()  # load side bar
    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return

    user_message = st.chat_input("Enter your message:")

    if not user_message:
        st.warning("Please enter a message to proceed")

    # load llm model
    if user_message:
        if user_input.get("selected_llm") == "Groq":
            groq_instance = groqllm(user_controls_input=user_input)
            model = groq_instance.get_llm_model()
        elif user_input.get("selected_llm") == "OpenAI":
            groq_instance = groqllm(user_controls_input=user_input)
            model = groq_instance.get_llm_model()
        else:
            groq_instance = groqllm(user_controls_input=user_input)
            model = groq_instance.get_llm_model()
        if not model:
            st.error("Error: Failed to load the Groq model. Please check your API key and model selection.")
            return
        
        selected_usecase = user_input.get("selected_usecase")
        if not selected_usecase:
            st.error("Error: No use case selected. Please select a use case to proceed.")
            return
        
        # load the graphs
        graph_builder_instance = GraphBuilder(model=model)
        graph_instance = graph_builder_instance.setup_graph(usecase=selected_usecase)

        # display the output
        display_ui = DisplayOutput(usecase=selected_usecase,graph=graph_instance,user_input=user_message)
        display_ui.display_output()

