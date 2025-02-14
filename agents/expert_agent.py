import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from agents.base_agent import BaseAgent

class ExpertAgent(BaseAgent):
    """ 
    A high-capability agent for handling complex tasks efficiently.
    Best suited for reasoning-heavy, resource-intensive tasks.
    """

    def __init__(self):
        """
        Initializes the ExpertAgent with high capability and higher cost.
        """
        super().__init__(name="ExpertAgent", capability=10, cost=8)
