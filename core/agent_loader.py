import importlib
import os
import inspect
import sys
from agents.base_agent import BaseAgent  

def load_agents(agent_dir="agents"):
    """
    Dynamically loads all agent classes from the agents directory.

    Args:
        agent_dir (str): Directory containing agent implementations.

    Returns:
        list: A list of instantiated agent objects.
    """
    agents = []
    agent_dir = os.path.abspath(agent_dir)  

    if agent_dir not in sys.path:
        sys.path.append(agent_dir)

    for file in os.listdir(agent_dir):
        if file.endswith(".py") and file not in ["__init__.py", "base_agent.py"]:
            module_name = f"{agent_dir.replace(os.sep, '.')}.{file[:-3]}"

            try:
                module = importlib.import_module(module_name)

                importlib.reload(module)

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, BaseAgent) and obj is not BaseAgent:
                        agents.append(obj()) 

            except Exception as e:
                print(f"⚠ Error loading agent {file}: {e}")  

    return agents
