import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph
from core.tools import Tools

class MarketerAgent(BaseAgent):
    """
    A specialized agent for marketing tasks including sentiment analysis,
    consumer behavior insights, and ad optimization.
    Uses tools: Sentiment Analysis API, Consumer Behavior AI
    """

    def __init__(self):
        super().__init__(name="MarketerAgent", capability=6, cost=4)
        self.memory = AgentMemory()
        self.knowledge_graph = KnowledgeGraph()
        self.tools = Tools()

    def execute(self, task):
        """
        Executes marketing-related tasks.

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

        result = self.specialized_task(task)

        self.memory.store(self.name, task, result)
        self.knowledge_graph.add_fact(task, "processed_by", self.name)

        return result

    def specialized_task(self, task):
        """
        Uses specialized marketing tools to process the task.

        Args:
            task (str): The task description.

        Returns:
            str: The processed output.
        """
        if "sentiment" in task.lower() or "feedback" in task.lower() or "review" in task.lower():
            return self.tools.analyze_sentiment(task)
        
        return f"MarketerAgent executing: {task}"
