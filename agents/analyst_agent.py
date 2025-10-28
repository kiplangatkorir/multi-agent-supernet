import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph

class AnalystAgent(BaseAgent):
    """
    A specialized agent for data analysis tasks.
    """

    def __init__(self):
        super().__init__(name="AnalystAgent", capability=2, cost=1)
        self.memory = AgentMemory()
        self.knowledge_graph = KnowledgeGraph()

    def execute(self, task):
        """
        Executes data analysis tasks.

        Args:
            task (str): The task description.

        Returns:
            str: The result of execution.
        """
        past_result = self.memory.retrieve(self.name, task)
        if past_result:
            return f"🔄 Recall: {self.name} remembers '{task}': {past_result}"

        knowledge = self.knowledge_graph.get_relations(task)
        if knowledge:
            return f"📚 Found in Knowledge Graph: {task} is related to {knowledge}"

        result = f"AnalystAgent executing: {task}"

        self.memory.store(self.name, task, result)
        self.knowledge_graph.add_fact(task, "processed_by", self.name)

        return result
