class AgentTeam:
    """
    Manages multi-agent collaboration for solving complex tasks.
    """

    def __init__(self, agents):
        """
        Initializes the collaboration module.

        Args:
            agents (list): List of agents available for collaboration.
        """
        self.agents = agents

    def assign_subtasks(self, task):
        """ 
        Splits a task into subtasks and assigns them to agents.
        
        Args:
            task (str): The main task to be divided.
        
        Returns:
            str: The final combined result from all agents.
        """
        subtasks = self._split_task(task)
        results = []

        for agent, subtask in zip(self.agents, subtasks):
            result = agent.execute(subtask)
            results.append(f"{agent.name}: {result}")

        return self._combine_results(results)

    def _split_task(self, task):
        """
        Splits a task into smaller subtasks.

        Args:
            task (str): The main task.

        Returns:
            list: List of subtasks.
        """
        # 🚀 Simple heuristic: Repeat the main task for all agents (can be improved)
        return [f"{task} (Part {i+1})" for i in range(len(self.agents))]

    def _combine_results(self, results):
        """
        Combines the results from different agents.

        Args:
            results (list): List of results from agents.

        Returns:
            str: The final combined result.
        """
        return " | ".join(results)
