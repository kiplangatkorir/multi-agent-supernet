import importlib
import os
import inspect
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agents.base_agent import BaseAgent

def load_agents():
    """
    Dynamically loads all agent classes from the `agents` directory while 
    ignoring deleted agents that have been moved to the Recycle Bin.
    
    Returns:
        list: A list of instantiated agent objects.
    """
    agents = []
    agents_dir = os.path.abspath("agents")
    recycle_bin = os.path.abspath("deleted_agents")

    # Ensure the directory is in the Python path
    if agents_dir not in sys.path:
        sys.path.append(agents_dir)

    for file in os.listdir(agents_dir):
        agent_path = os.path.join(agents_dir, file)

        # Ignore non-Python files and deleted agents
        if not file.endswith("_agent.py") or file == "base_agent.py":
            continue

        if os.path.exists(os.path.join(recycle_bin, file)):  # ✅ Skip if agent is in Recycle Bin
            continue

        module_name = f"agents.{file[:-3]}"  # Remove `.py` extension

        try:
            module = importlib.import_module(module_name)
            importlib.reload(module)  # Ensure fresh reload

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseAgent) and obj is not BaseAgent:
                    agents.append(obj())  # Instantiate the agent

        except ModuleNotFoundError as e:
            print(f"⚠ Error loading agent {file}: {e}")

    return agents
