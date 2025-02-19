import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from agents.base_agent import BaseAgent
from core.memory import AgentMemory  # 🆕 Import memory module
from core.knowledge_graph import KnowledgeGraph  # 🆕 Import knowledge graph

class MidAgent(BaseAgent):
    """ 
    A mid-tier agent that balances capability and cost.
    Suitable for moderately complex tasks that require some reasoning.
    """

    def __init__(self):
        """
        Initializes the MidAgent with medium capability and cost.
        """
        super().__init__(name="MidAgent", capability=5, cost=3)
        self.memory = AgentMemory()  # 🆕 Initialize memory
        self.knowledge_graph = KnowledgeGraph()  # 🆕 Initialize KG

    def execute(self, task):
        """
        Executes the given task, using memory and the knowledge graph for reasoning.

        Args:
            task (str): The task description.

        Returns:
            str: The result of task execution.
        """
     
