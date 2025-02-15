import matplotlib.pyplot as plt
import numpy as np

def plot_agent_distribution(agent_supernet):
    """
    Plots the current agent selection probability distribution.

    Args:
        agent_supernet (AgenticSupernet): The multi-agent selection model.
    """
    agents = [agent.name for agent in agent_supernet.agents]
    probabilities = agent_supernet.get_distribution()

    plt.figure(figsize=(8, 5))
    plt.bar(agents, probabilities, color="skyblue")
    plt.xlabel("Agents")
    plt.ylabel("Selection Probability")
    plt.title("Agent Selection Probability Distribution")
    plt.ylim(0, 1)
    
    for i, prob in enumerate(probabilities):
        plt.text(i, prob + 0.02, f"{prob:.2f}", ha="center", fontsize=10)

    plt.show()
