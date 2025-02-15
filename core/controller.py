import random

class Controller:
    """ 
    Manages task execution, selects agents dynamically, and updates the supernet based on feedback.
    """

    def __init__(self, supernet):
        """
        Initializes the controller with an agentic supernet.

        Args:
            supernet (AgenticSupernet): The probabilistic agent selection system.
        """
        self.supernet = supernet

    def allocate_agents(self, task):
        """
        Selects the best agentic configuration based on task complexity.

        Args:
            task (dict): Task details including complexity.

        Returns:
            list: Selected agents for task execution.
        """
        return self.supernet.sample_architecture(task)

    def execute_task(self, task):
        """
        Executes a task using selected agents and updates agent probabilities based on success or failure.

        Args:
            task (dict): Task details including complexity.

        Returns:
            bool: True if the task succeeded, False otherwise.
        """
        agents = self.allocate_agents(task)
        print(f"Executing task: {task['name']} with {', '.join(a.name for a in agents)}")

        success = any(agent.execute(task) for agent in agents)  

        for agent in agents:
            agent_idx = self.supernet.agents.index(agent)
            reward = 0.1 if success else -0.05  
            self.supernet.update_distribution(agent_idx, reward)

        print(f"Task {task['name']} {'succeeded' if success else 'failed'}.\n")
        return success
