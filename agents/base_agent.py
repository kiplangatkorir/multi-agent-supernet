# agents/base_agent.py

import numpy as np

class BaseAgent:
    """ 
    Base class for all AI agents in the multi-agent supernet.
    Each agent has a capability level and an execution method.
    """
    
    def __init__(self, name: str, capability: float, cost: float):
        """
        Initializes the agent.
        
        Args:
            name (str): The name of the agent.
            capability (float): The agent's ability to solve complex tasks.
            cost (float): The resource cost (e.g., API calls, computation).
        """
        self.name = name
        self.capability = capability
        self.cost = cost

    def execute(self, task):
        """
        Executes a given task based on the agent's capability.

        Args:
            task (dict): A dictionary with task properties including 'complexity'.

        Returns:
            bool: True if the task succeeds, False otherwise.
        """
        complexity = task.get("complexity", 1)
        success_prob = min(1, self.capability / complexity)  
        return np.random.rand() < success_prob  

    def __repr__(self):
        """ Returns a string representation of the agent. """
        return f"{self.name}(Capability={self.capability}, Cost={self.cost})"
