import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph

class FinancialAnalyst(BaseAgent):
    """
    A dynamically created agent specialized for Financial tasks.
    """

    def __init__(self):
        super().__init__(name="FinancialAnalyst", capability=8, cost=6)
        self.memory = AgentMemory()
        self.knowledge_graph = KnowledgeGraph()

    def execute(self, task):
        """
        Executes the given task.

        Args:
            task (str): The task description.

        Returns:
            str: The result of task execution.
        """
        # Check Memory First
        past_result = self.memory.retrieve(self.name, task)
        if past_result:
            return f"Recall: {self.name} remembers '{task}': {past_result}"

        # Query Knowledge Graph
        knowledge = self.knowledge_graph.get_relations(task)
        if knowledge:
            return f"Found in Knowledge Graph: {task} is related to {knowledge}"

        # Process Task
        result = f"{self.name} executing: {task}"
        
        # Store in Memory & KG
        self.memory.store(self.name, task, result)
        self.knowledge_graph.add_fact(task, "processed_by", self.name)

        return result
