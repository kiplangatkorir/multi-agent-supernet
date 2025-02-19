import os
import random

# Corrected Template for Generating New Agents
AGENT_TEMPLATE = '''import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph

class {class_name}(BaseAgent):
    """
    A dynamically created agent specialized for {agent_type} tasks.
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
            return f"Recall: {{self.name}} remembers '{{task}}': {{past_result}}"

        # Query Knowledge Graph
        knowledge = self.knowledge_graph.get_relations(task)
        if knowledge:
            return f"Found in Knowledge Graph: {{task}} is related to {{knowledge}}"

        # Process Task
        result = f"{{self.name}} executing: {{task}}"
        
        # Store in Memory & KG
        self.memory.store(self.name, task, result)
        self.knowledge_graph.add_fact(task, "processed_by", self.name)

        return result
'''

# Predefined agent types with auto-assigned values
AGENT_TYPE_MAPPING = {
    "Basic": (1, 1),
    "Mid": (5, 3),
    "Expert": (10, 8),
    "Research": (7, 5),
    "Financial": (8, 6),
    "Marketing": (6, 7),
    "Medical": (9, 7),
    "Data": (8, 5),
    "Legal": (7, 6),
    "Security": (9, 9)
}

def assign_capability_and_cost(agent_name):
    """
    Assigns capability and cost based on agent type.

    Args:
        agent_name (str): The name of the agent class.

    Returns:
        tuple: (capability, cost)
    """
    for keyword, (capability, cost) in AGENT_TYPE_MAPPING.items():
        if keyword.lower() in agent_name.lower():
            return capability, cost

    # Default for unknown agent types
    return random.randint(3, 7), random.randint(2, 6)

def create_agent(agent_name):
    """
    Generates a new agent Python file dynamically.

    Args:
        agent_name (str): Name of the new agent class.
    """
    agents_dir = "agents"
    filename = f"{agents_dir}/{agent_name.lower()}_agent.py"

    # Ensure the agents directory exists
    if not os.path.exists(agents_dir):
        os.makedirs(agents_dir)

    # Assign capabilities & cost dynamically
    capability, cost = assign_capability_and_cost(agent_name)

    # Detect agent type based on keyword
    agent_type = "General Purpose"
    for keyword in AGENT_TYPE_MAPPING.keys():
        if keyword.lower() in agent_name.lower():
            agent_type = keyword
            break

    # Write the new agent file with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        f.write(AGENT_TEMPLATE.format(class_name=agent_name, agent_type=agent_type, capability=capability, cost=cost))

    print(f"✅ Agent '{agent_name}' created successfully at {filename} (Capability: {capability}, Cost: {cost})")

# CLI Interface
if __name__ == "__main__":
    agent_name = input("Enter agent class name: ").strip().replace(" ", "")
    create_agent(agent_name)
