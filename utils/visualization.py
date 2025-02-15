# utils/visualization.py

import matplotlib.pyplot as plt
from utils.metrics import MetricsTracker

metrics_tracker = MetricsTracker()

def plot_task_success_rates():
    """
    Plots the success rates of all registered tasks.
    """
    task_names = list(metrics_tracker.metrics["tasks"].keys())
    success_rates = [metrics_tracker.get_task_success_rate(task) for task in task_names]

    plt.figure(figsize=(8, 5))
    plt.bar(task_names, success_rates, color="green")
    plt.xlabel("Tasks")
    plt.ylabel("Success Rate")
    plt.title("Task Success Rates")
    plt.ylim(0, 1)

    for i, rate in enumerate(success_rates):
        plt.text(i, rate + 0.02, f"{rate:.2f}", ha="center", fontsize=10)

    plt.show()


def plot_agent_selection_counts():
    """
    Plots the number of times each agent has been selected.
    """
    agent_names = list(metrics_tracker.metrics["agents"].keys())
    selection_counts = [metrics_tracker.get_agent_selection_count(agent) for agent in agent_names]

    plt.figure(figsize=(8, 5))
    plt.bar(agent_names, selection_counts, color="blue")
    plt.xlabel("Agents")
    plt.ylabel("Selection Count")
    plt.title("Agent Selection Frequency")

    for i, count in enumerate(selection_counts):
        plt.text(i, count + 0.5, str(count), ha="center", fontsize=10)

    plt.show()
