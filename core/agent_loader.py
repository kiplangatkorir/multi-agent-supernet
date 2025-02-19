import importlib
import os
import inspect
from agents.base_agent import BaseAgent  # Ensure we check for inheritance

def load_agents(agent_dir="agents"):
    """
    Dynamically loads all agent classes from the agents directory.

    Args:
        agent_dir (str): Directory containing agent implementations.

    Returns:
        list: A list of instantiated agent objects.
    """
    agents = []
    for file in os.listdir(agent_dir):
        if file.endswith(".py") and file not in ["__init__.py", "base_agent.py"]:
            module_name = f"{agent_dir}.{file[:-3]}"
            module = importlib.import_module(module_name)
            
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseAgent) and obj is not BaseAgent:  # 🆕 Ensure it’s a subclass but NOT BaseAgent
                    agents.append(obj())  # Instantiate and add to the list

    return agents
