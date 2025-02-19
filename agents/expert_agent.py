import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.knowledge_graph import KnowledgeGraph

class ExpertAgent(BaseAgent):
    """
    A high-capability agent that can leverage a knowledge graph for reasoning.
    """

    def __init__(self):
        super().__init__(name="ExpertAgent", capability=10, cost=8)
        self.knowledge_graph = KnowledgeGraph()  

    def execute(self, task):
        """
        Executes the given task, using the knowledge graph for reasoning.

        Args:
            task (str): The task description.

        Returns:
            str: The result of task execution.
        """
        relations = self.knowledge_graph.get_relations(task)
        if relations:
            return f"📚 Knowledge Found: {task} is related to {relations}"

        result = f"ExpertAgent executing: {task}"
        self.knowledge_graph.add_fact(task, "resulted_in", result)   
        return result
