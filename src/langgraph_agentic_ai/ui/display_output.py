import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
class DisplayOutput:
    """
    Class to handle the display of output in the Streamlit UI.
    """
    def __init__(self, usecase, graph, user_input):
        self.usecase = usecase
        self.graph = graph
        self.user_input = user_input

    def display_output(self):
        """
        Display the output based on the use case and graph.
        """
        if self.usecase == "Basic_Chatbot":
            for event in self.graph.stream({"messages": [self.user_input]}):
                print("output of stream:", event)  # returns only agent message
                # graph.stream() doesn’t emit the initial input (user message) — it only emits outputs from graph nodes.
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(self.user_input)
                    with st.chat_message("assistant"):
                        st.write(value["messages"][-1].content)

            print("output of invoke:", self.graph.invoke({"messages": [self.user_input]}))

        elif self.usecase == "Chatbot with Web":
            with st.chat_message("user"):
                st.write(self.user_input)
            for event in self.graph.stream({"messages": [self.user_input]}):
                print("output of stream:", event)  # returns only agent message
                # graph.stream() doesn’t emit the initial input (user message) — it only emits outputs from graph nodes.
                for value in event.values():
                    if type(value["messages"][-1]) == AIMessage:
                        if not value["messages"][-1].content:
                            with st.chat_message("assistant"):
                                st.write("Thinking..")   
                        else:
                            with st.chat_message("assistant"):
                                st.write(value["messages"][-1].content)                 
                    # if type(value["messages"][-1]) == ToolMessage:
                    #     with st.chat_message("tool message"):
                    #         st.write(value["messages"][-1].content)
    
        elif self.usecase == "AI News":
            # Implement logic for AI News
            pass
        elif self.usecase == "Blog Generator":
            # Implement logic for Blog Generator
            pass
        else:
            st.error("Unknown use case selected.")

