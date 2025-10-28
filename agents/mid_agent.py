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
        # 🧠 Step 1: Check Memory for Past Results
        past_result = self.memory.retrieve(self.name, task)
        if past_result:
            return f"🔄 Recall: {self.name} remembers '{task}': {past_result}"

        # 📚 Step 2: Check Knowledge Graph for Related Facts
        related_facts = self.knowledge_graph.get_relations(task)
        if related_facts:
            return f"📚 Knowledge Found: {task} is related to {related_facts}"

        # 🛠 Step 3: Execute Task
        result = f"MidAgent executing: {task}"

        # 🔄 Step 4: Store the Result in Memory & Knowledge Graph
        self.memory.store(self.name, task, result)  # Store in memory
        self.knowledge_graph.add_fact(task, "performed_by", "MidAgent")
        self.knowledge_graph.add_fact(task, "resulted_in", result)

        return result
