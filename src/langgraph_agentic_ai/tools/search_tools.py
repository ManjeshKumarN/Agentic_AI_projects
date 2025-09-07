from langchain_tavily import TavilySearch
from langgraph.prebuilt.tool_node import ToolNode

def get_tools():
    """
    Returns a list of tools for web searching
    """
    # Initialize the TavilySearch tool with default parameters
    tools = [TavilySearch(max_results=2, topic="general")]
    return tools

def create_tool_node(tools):
    """
    Creates a ToolNode with the TavilySearch tool
    """
    return ToolNode(tools=tools)