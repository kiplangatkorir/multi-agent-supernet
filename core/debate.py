import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core.knowledge_graph import KnowledgeGraph

class DebateManager:
    """
    Manages debates among agents using knowledge-based reasoning.
    """

    def __init__(self, agents):
        self.agents = agents
        self.knowledge_graph = KnowledgeGraph()  # 🆕 Global KG access

    def debate(self, task, proposed_answer):
        """
        Runs a debate among agents to determine the best answer using knowledge graph reasoning.

        Args:
            task (str): The task being debated.
            proposed_answer (str): The initially proposed answer.

        Returns:
            str: The most agreed-upon answer.
        """
        best_answer = proposed_answer

        # Let agents search the KG for prior knowledge
        for agent in self.agents:
            knowledge = self.knowledge_graph.get_relations(task)
            if knowledge:
                best_answer = f"🔄 Knowledge-Backed Answer: {knowledge}"

        # Store the final debated answer in KG
        self.knowledge_graph.add_fact(task, "final_answer", best_answer)

        return best_answer
