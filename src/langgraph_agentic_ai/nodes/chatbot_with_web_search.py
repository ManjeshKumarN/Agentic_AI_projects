from src.langgraph_agentic_ai.state.graph_state import State


class ChatbotWithWebNode:
    """
    Chatbot with Web Search Node for LangGraph Agentic AI
    """
    def __init__(self, model, tools):
        self.tools = tools
        self.llm = model.bind_tools(self.tools)

    def process(self, state: State):
        """
        Process the input message using the LLM and web search, then return the response.
        """

        # Get the response from the LLM
        response = self.llm.invoke(state.messages)
        
        return {"messages": [response]}
    
    