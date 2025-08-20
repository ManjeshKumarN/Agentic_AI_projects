from pydantic import BaseModel
from typing import Annotated
from typing_extensions import List
from langgraph.graph.message import add_messages


class State(BaseModel):
    """
    Represents the state of the graph.
    This state is used to manage the conversation and the flow of the graph.
    """
    messages: Annotated[List, add_messages]