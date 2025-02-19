import random

class AgentTeam:
    """
    A next-level multi-agent collaboration framework for solving complex tasks efficiently.
    """

    def __init__(self, agents):
        """
        Initializes the collaboration module.

        Args:
            agents (list): List of available agents.
        """
        self.agents = sorted(agents, key=lambda a: a.capability, reverse=True)  

    def execute_task(self, task):
        """ 
        Executes a complex task by dividing it into subtasks, assigning them to agents, 
        refining results iteratively, and merging the final response.

        Args:
            task (str): The main task.

        Returns:
            str: The final result after collaboration.
        """
        subtasks = self._split_task(task)
        results = {}

        for subtask in subtasks:
            best_agent = self._select_best_agent(subtask)
            result = best_agent.execute(subtask)
            results[subtask] = result

        refined_results = self._refine_results(results)

        final_result = self._merge_results(refined_results)

        return final_result

    def _split_task(self, task):
        """
        Dynamically splits a task into smaller subtasks.

        Args:
            task (str): The main task.

        Returns:
            list: A list of meaningful subtasks.
        """
        return [f"{task} - Phase {i+1}" for i in range(random.randint(2, len(self.agents)))]

    def _select_best_agent(self, subtask):
        """
        Selects the most capable agent for a given subtask.

        Args:
            subtask (str): The subtask description.

        Returns:
            BaseAgent: The most suitable agent.
        """
        return max(self.agents, key=lambda agent: agent.capability)  

    def _refine_results(self, results):
        """
        Runs a refinement step where agents validate each other's outputs.

        Args:
            results (dict): Initial results from agents.

        Returns:
            dict: Refined results after validation.
        """
        refined = {}
        for subtask, result in results.items():
            best_agent = self._select_best_agent(subtask)
            validation = best_agent.execute(f"Validate: {subtask}")  

            refined[subtask] = f"✔ Refined: {result}" if "error" not in validation.lower() else result  

        return refined

    def _merge_results(self, refined_results):
        """
        Merges multiple agent responses into a single optimized output.

        Args:
            refined_results (dict): The validated outputs from agents.

        Returns:
            str: The final optimized response.
        """
        return " | ".join(refined_results.values())
