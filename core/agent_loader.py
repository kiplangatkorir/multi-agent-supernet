import importlib
import os
import inspect
import sys
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
    agent_dir = os.path.abspath(agent_dir)  # Normalize path

    # Ensure the directory is in the Python path
    if agent_dir not in sys.path:
        sys.path.append(agent_dir)

    for file in os.listdir(agent_dir):
        if file.endswith(".py") and file not in ["__init__.py", "base_agent.py"]:
            module_name = f"{agent_dir.replace(os.sep, '.')}.{file[:-3]}"

            try:
                module = importlib.import_module(module_name)

                # Reload in case of updates
                importlib.reload(module)

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, BaseAgent) and obj is not BaseAgent:
                        agents.append(obj())  # Instantiate the agent

            except Exception as e:
                print(f"⚠ Error loading agent {file}: {e}")  # Prevent crashes and show error

    return agents
