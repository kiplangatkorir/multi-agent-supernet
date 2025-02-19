import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from agents.base_agent import BaseAgent
from core.memory import AgentMemory  # 🆕 Import memory module
from core.knowledge_graph import KnowledgeGraph  # 🆕 Import knowledge graph

class BasicAgent(BaseAgent):
    """ 
    A lightweight agent for handling simple tasks efficiently. 
    Suitable for low-complexity problems with minimal resource usage.
    """

    def __init__(self):
        """
        Initializes the BasicAgent with low capability and low cost.
        """
        super().__init__(name="BasicAgent", capability=1, cost=1)
        self.memory = AgentMemory()  # 🆕 Initialize memory
        self.knowledge_graph = KnowledgeGraph()  # 🆕 Initialize KG

    def execute(self, task):
        """
        Executes the given task, using memory and the knowledge graph when available.

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
        result = f"BasicAgent executing: {task}"

        # 🔄 Step 4: Store the Result in Memory & Knowledge Graph
        self.memory.store(self.name, task, result)  # 🆕 Store in memory
        self.knowledge_graph.add_fact(task, "performed_by", "BasicAgent")
        self.knowledge_graph.add_fact(task, "resulted_in", result)

        return result
