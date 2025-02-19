import os
import random

# Mapping agent types to their capabilities, cost, and specialized tools
AGENT_TYPE_MAPPING = {
    "Basic": (1, 1, ["Basic Reasoning"]),
    "Mid": (5, 3, ["Intermediate Analysis"]),
    "Expert": (10, 8, ["Advanced AI Processing"]),
    "Research": (7, 5, ["Knowledge Graph", "ArXiv API"]),
    "Financial": (8, 6, ["Yahoo Finance API", "Stock Trend Analysis"]),
    "Marketing": (6, 7, ["Sentiment Analysis", "Consumer Behavior AI"]),
    "Medical": (9, 7, ["PubMed API", "Medical Diagnosis Database"]),
    "Data": (8, 5, ["Big Data Processing", "Predictive Analytics"]),
    "Legal": (7, 6, ["Case Law Database", "Legal Document Analysis"]),
    "Security": (9, 9, ["Threat Intelligence API", "Cybersecurity Monitor"])
}

# Template for agent generation
AGENT_TEMPLATE = '''import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph
from core.tools import Tools  # ✅ Import tools

class {class_name}(BaseAgent):
    """
    A dynamically created agent specialized for {agent_type} tasks.
    Uses tools: {tools}
    """

    def __init__(self):
        super().__init__(name="{class_name}", capability={capability}, cost={cost})
        self.memory = AgentMemory()
        self.knowledge_graph = KnowledgeGraph()
        self.tools = Tools()  # ✅ Load tools

    def execute(self, task):
        """
        Executes the given task using specialized tools.

        Args:
            task (str): The task description.

        Returns:
            str: The result of execution.
        """
        past_result = self.memory.retrieve(self.name, task)
        if past_result:
            return f"🔄 Recall: {{self.name}} remembers '{{task}}': {{past_result}}"

        # Query Knowledge Graph
        knowledge = self.knowledge_graph.get_relations(task)
        if knowledge:
            return f"📚 Found in Knowledge Graph: {{task}} is related to {{knowledge}}"

        # Specialized Execution
        result = self.specialized_task(task)

        self.memory.store(self.name, task, result)
        self.knowledge_graph.add_fact(task, "processed_by", self.name)

        return result

    def specialized_task(self, task):
        """
        Uses specialized tools to process the task.

        Args:
            task (str): The task description.

        Returns:
            str: The processed output.
        """
        {specialization_logic}
        return f"{class_name} executing: {{task}}"
'''

def assign_capability_and_tools(agent_name):
    """
    Assigns capability, cost, and tools based on agent type.

    Args:
        agent_name (str): The name of the agent class.

    Returns:
        tuple: (capability, cost, tools)
    """
    for keyword, (capability, cost, tools) in AGENT_TYPE_MAPPING.items():
        if keyword.lower() in agent_name.lower():
            return capability, cost, tools

    # Default for unknown agent types
    return random.randint(3, 7), random.randint(2, 6), ["Basic AI Processing"]

def generate_specialized_logic(agent_type):
    """
    Generates specialized execution logic based on agent type.

    Args:
        agent_type (str): The type of agent.

    Returns:
        str: Specialized task execution logic as a string.
    """
    logic_map = {
        "Financial": '''
        if "stock" in task.lower() or "price" in task.lower():
            ticker = task.split()[-1]  # Extracts ticker from task
            return self.tools.fetch_stock_price(ticker)
        ''',
        "Research": '''
        if "paper" in task.lower() or "study" in task.lower():
            return self.tools.fetch_academic_papers(task)
        ''',
        "Marketing": '''
        if "sentiment" in task.lower() or "feedback" in task.lower():
            return self.tools.analyze_sentiment(task)
        ''',
        "Security": '''
        if "threat" in task.lower() or "log" in task.lower():
            return self.tools.detect_threats([task])
        ''',
        "Medical": '''
        if "symptom" in task.lower() or "diagnose" in task.lower():
            return self.tools.fetch_medical_info(task)
        ''',
    }
    return logic_map.get(agent_type, "return f'{class_name} executing: {task}'")

def create_agent(agent_name):
    """
    Generates a new agent Python file dynamically.

    Args:
        agent_name (str): Name of the new agent class.
    """
    agents_dir = "agents"
    filename = f"{agents_dir}/{agent_name.lower()}_agent.py"

    if not os.path.exists(agents_dir):
        os.makedirs(agents_dir)

    # Assign specialization, tools, and capability dynamically
    capability, cost, tools = assign_capability_and_tools(agent_name)

    # Detect agent type based on keyword
    agent_type = "General Purpose"
    for keyword in AGENT_TYPE_MAPPING.keys():
        if keyword.lower() in agent_name.lower():
            agent_type = keyword
            break

    # Auto-generate specialized execution logic
    specialization_logic = generate_specialized_logic(agent_type)

    # Write the new agent file with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        f.write(AGENT_TEMPLATE.format(
            class_name=agent_name,
            agent_type=agent_type,
            capability=capability,
            cost=cost,
            tools=", ".join(tools),
            specialization_logic=specialization_logic
        ))

    print(f"✅ Specialized Agent '{agent_name}' created successfully at {filename} (Field: {agent_type}, Tools: {tools})")

# CLI Interface
if __name__ == "__main__":
    agent_name = input("Enter agent class name: ").strip().replace(" ", "")
    create_agent(agent_name)
