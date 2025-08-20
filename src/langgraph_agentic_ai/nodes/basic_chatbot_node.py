from src.langgraph_agentic_ai.state.graph_state import State


class BasicChatbotnode:
    """
    Basic Chatbot Node for LangGraph Agentic AI
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State):
        """
        Process the input message using the LLM and return the response.
        """
        response = self.llm.invoke(state.messages)
        return {"messages": [response]}
