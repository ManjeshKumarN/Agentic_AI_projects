from langgraph.graph import START, END, StateGraph
from src.langgraph_agentic_ai.state.graph_state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotnode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(state_schema=State)
        self.agent = BasicChatbotnode(model=self.llm)

    def basic_chatbot_build_graph(self):
        self.agent = BasicChatbotnode(model=self.llm)
        self.graph_builder.add_node(node="agent", action=self.agent.process)

        self.graph_builder.add_edge(start_key=START, end_key="agent")
        self.graph_builder.add_edge(start_key="agent", end_key=END)
        return self.graph_builder.compile()
    
    def setup_graph(self, usecase):
        """
        Setup the graph based on the selected use case.
        This method can be extended to handle different use cases.
        """
        # Basic_Chatbot, Chatbot with Tool, AI News, Blog Generator

        if usecase == "Basic_Chatbot":
            return self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Tool":
            return self.basic_chatbot_build_graph()
        elif usecase == "AI News":
            return self.basic_chatbot_build_graph()
        elif usecase == "Blog Generator":
            return self.basic_chatbot_build_graph()
        else:
            raise ValueError(f"Unknown use case: {usecase}")




    