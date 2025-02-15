
import numpy as np
import random

class AgenticSupernet:
    """ 
    Probabilistic model for selecting the best agentic architecture dynamically. 
    Uses Monte Carlo sampling and entropy regularization to balance performance and cost.
    """

    def __init__(self, agents, entropy_weight=0.1):
        """
        Initializes the agentic supernet with a set of agents.

        Args:
            agents (list): List of available agents.
            entropy_weight (float): Weight for entropy regularization to encourage diversity.
        """
        self.agents = agents
        self.architecture_distribution = np.ones(len(agents)) / len(agents)  
        self.entropy_weight = entropy_weight  

    def update_distribution(self, agent_idx, reward):
        """
        Updates the probability distribution based on task success or failure.

        Args:
            agent_idx (int): Index of the agent in the supernet.
            reward (float): Reward for the agent (positive for success, negative for failure).
        """
        self.architecture_distribution[agent_idx] += reward
        self.architecture_distribution /= self.architecture_distribution.sum()  

        entropy = -np.sum(self.architecture_distribution * np.log(self.architecture_distribution + 1e-8))
        self.architecture_distribution += self.entropy_weight * entropy
        self.architecture_distribution /= self.architecture_distribution.sum()  

    def sample_architecture(self, task, num_samples=3):
        """
        Dynamically selects agents based on task complexity and cost constraints.

        Args:
            task (dict): Task details including complexity.
            num_samples (int): Number of agents to sample.

        Returns:
            list: Selected agents for the given task.
        """
        sampled_agents = np.random.choice(
            self.agents, size=num_samples, p=self.architecture_distribution, replace=True
        )

        selected_agents = []
        for agent in sampled_agents:
            if agent.capability >= task["complexity"] * random.uniform(0.5, 1.5):
                selected_agents.append(agent)

        if task["complexity"] <= 3:
            selected_agents = [agent for agent in selected_agents if agent.cost < 5]

        return selected_agents if selected_agents else [random.choice(self.agents)]

    def get_distribution(self):
        """
        Returns the current probability distribution of agent selection.

        Returns:
            np.array: Probability distribution of agents.
        """
        return self.architecture_distribution
