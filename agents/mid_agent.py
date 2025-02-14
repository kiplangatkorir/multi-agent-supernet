import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from agents.base_agent import BaseAgent

class MidAgent(BaseAgent):
    """ 
    A mid-tier agent that balances capability and cost.
    Suitable for moderately complex tasks that require some reasoning.
    """

    def __init__(self):
        """
        Initializes the MidAgent with medium capability and cost.
        """
        super().__init__(name="MidAgent", capability=5, cost=3)
