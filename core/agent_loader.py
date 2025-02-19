# core/agent_loader.py
import importlib
import os

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
            
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and hasattr(obj, "execute"):
                    agents.append(obj())

    return agents
