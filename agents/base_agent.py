from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all AI agents.
    """

    def __init__(self, name, capability=1, cost=1):
        self.name = name
        self.capability = capability  
        self.cost = cost 

    @abstractmethod
    def execute(self, task):
        """
        Executes a task. This method must be implemented by all agents.
        
        Args:
            task (str): The task to perform.
        
        Returns:
            str: The result of the task execution.
        """
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, capability={self.capability}, cost={self.cost})"
