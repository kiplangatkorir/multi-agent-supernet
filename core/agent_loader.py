import importlib
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import inspect
from agents.base_agent import BaseAgent  

def load_agents():
    """
    Dynamically loads all agent classes from the agents directory.

    Returns:
        list: A list of instantiated agent objects.
    """
    agents = []
    agent_dir = os.path.abspath("agents")  

    if agent_dir not in sys.path:
        sys.path.append(agent_dir)

    for file in os.listdir(agent_dir):
        if file.endswith("_agent.py") and file != "base_agent.py":
            module_name = f"agents.{file[:-3]}" 

            try:
                module = importlib.import_module(module_name)

                importlib.reload(module)

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, BaseAgent) and obj is not BaseAgent:
                        agents.append(obj())  

            except ModuleNotFoundError as e:
                print(f"⚠ Error loading agent {file}: {e}")  
    return agents
