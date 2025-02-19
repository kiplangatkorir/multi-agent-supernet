import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import os

# Template for generating new agents
AGENT_TEMPLATE = '''import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph

class {class_name}(BaseAgent):
    """
    A dynamically created agent for handling specialized tasks.
    """

    def __init__(self):
        super().__init__(name="{class_name}", capability={capability}, cost={cost})
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
            return f"🔄 Recall: {self.name} remembers '{task}': {past_result}"

        # Query Knowledge Graph
        knowledge = self.knowledge_graph.get_relations(task)
        if knowledge:
            return f"📚 Found in Knowledge Graph: {task} is related to {knowledge}"

        # Process Task
        result = f"{class_name} executing: {task}"
        
        # Store in Memory & KG
        self.memory.store(self.name, task, result)
        self.knowledge_graph.add_fact(task, "processed_by", "{class_name}")

        return result
'''

def create_agent(agent_name, capability, cost):
    """
    Generates a new agent Python file dynamically.

    Args:
        agent_name (str): Name of the new agent class.
        capability (int): Capability score (1-10).
        cost (int): Cost score (1-10).
    """
    agents_dir = "agents"
    filename = f"{agents_dir}/{agent_name.lower()}_agent.py"

    # Ensure the agents directory exists
    if not os.path.exists(agents_dir):
        os.makedirs(agents_dir)

    # Write the new agent file
    with open(filename, "w") as f:
        f.write(AGENT_TEMPLATE.format(class_name=agent_name, capability=capability, cost=cost))

    print(f"✅ Agent '{agent_name}' created successfully at {filename}")

# CLI Interface
if __name__ == "__main__":
    agent_name = input("Enter agent class name: ").strip().replace(" ", "")
    capability = int(input("Enter capability (1-10): "))
    cost = int(input("Enter cost (1-10): "))

    create_agent(agent_name, capability, cost)
