from langgraph.graph import START, END, StateGraph
from src.langgraph_agentic_ai.state.graph_state import State
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotnode
from src.langgraph_agentic_ai.nodes.chatbot_with_web_search import ChatbotWithWebNode
from src.langgraph_agentic_ai.tools.search_tools import get_tools, create_tool_node

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(state_schema=State)
        
    def basic_chatbot_build_graph(self):
        self.agent = BasicChatbotnode(model=self.llm)
        self.graph_builder.add_node(node="agent", action=self.agent.process)

        self.graph_builder.add_edge(start_key=START, end_key="agent")
        self.graph_builder.add_edge(start_key="agent", end_key=END)
        return self.graph_builder.compile()
    
    def chatbot_with_web_build_graph(self):
        tools = get_tools()
        tool_node = create_tool_node(tools=tools)

        self.web_agent = ChatbotWithWebNode(model=self.llm, tools=tools)

        self.graph_builder.add_node(node="agent_with_web_search", action=self.web_agent.process)
        self.graph_builder.add_node(node="tools", action=tool_node)
        
        self.graph_builder.add_edge(start_key=START, end_key="agent_with_web_search")
        self.graph_builder.add_conditional_edges(source="agent_with_web_search", path=tools_condition)
        self.graph_builder.add_edge(start_key="tools", end_key="agent_with_web_search")
        self.graph_builder.add_edge(start_key="agent_with_web_search", end_key=END)
        
        return self.graph_builder.compile()

    def setup_graph(self, usecase):
        """
        Setup the graph based on the selected use case.
        This method can be extended to handle different use cases.
        """
        # Basic_Chatbot, Chatbot with Tool, AI News, Blog Generator

        if usecase == "Basic_Chatbot":
            return self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Web":
            return self.chatbot_with_web_build_graph()
        elif usecase == "AI News":
            return self.basic_chatbot_build_graph()
        elif usecase == "Blog Generator":
            return self.basic_chatbot_build_graph()
        else:
            raise ValueError(f"Unknown use case: {usecase}")




    