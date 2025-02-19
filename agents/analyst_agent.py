from agents.base_agent import BaseAgent

class Analyst(BaseAgent):
    """
    Custom AI agent for specialized tasks.
    """

    def __init__(self):
        super().__init__(name="Analyst", capability=2, cost=1)

    def execute(self, task):
        """
        Executes the assigned task.

        Args:
            task (str): The task to be performed.

        Returns:
            str: The result of the execution.
        """
        return f"Analyst executing: {task}"
