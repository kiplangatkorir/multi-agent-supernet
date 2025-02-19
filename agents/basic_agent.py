import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from agents.base_agent import BaseAgent

class BasicAgent(BaseAgent):
    """ 
    A lightweight agent for handling simple tasks efficiently. 
    Suitable for low-complexity problems with minimal resource usage.
    """

    def __init__(self):
        """
        Initializes the BasicAgent with low capability and low cost.
        """
        super().__init__(name="BasicAgent", capability=1, cost=1)

    def execute(self, task):
        """
        Executes the given task.

        Args:
            task (str): The task description.

        Returns:
            str: The result of task execution.
        """
        return f"BasicAgent executing: {task}"  