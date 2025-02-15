import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# experiments/run_experiment.py

import sys
import os
import json
import random
from core.task_manager import TaskManager
from core.controller import Controller
from core.agentic_supernet import AgenticSupernet
from agents.basic_agent import BasicAgent
from agents.mid_agent import MidAgent
from agents.expert_agent import ExpertAgent
from utils.metrics import MetricsTracker
from utils.visualization import plot_task_success_rates, plot_agent_selection_counts
from utils.logger import log_event

EXPERIMENT_RESULTS_FILE = "experiments/results/experiment_results.json"

# Ensure Python finds the correct module paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def run_experiment(num_runs=10):
    """
    Runs an experiment by executing multiple tasks and tracking results.

    Args:
        num_runs (int): Number of iterations for the experiment.
    """
    os.makedirs("experiments/results", exist_ok=True)
    
    print("🔍 Initializing experiment...")

    task_manager = TaskManager()
    metrics_tracker = MetricsTracker()
    agents = [BasicAgent(), MidAgent(), ExpertAgent()]
    supernet = AgenticSupernet(agents)
    controller = Controller(supernet)

    # Register example tasks
    print("📌 Registering tasks...")
    task_manager.register_task("Simple Arithmetic", complexity=1)
    task_manager.register_task("Web Navigation", complexity=5)
    task_manager.register_task("Advanced Code Generation", complexity=10)

    results = {"tasks": {}, "agents": {}}

    print(f"🚀 Running {num_runs} experiment iterations...\n")
    
    for i in range(num_runs):
        print(f"▶ Iteration {i+1}/{num_runs}...")
        tasks = task_manager.list_tasks()
        for task in tasks:
            task_name = task["name"]
            success = controller.execute_task(task)
            
            # Update metrics
            metrics_tracker.update_task_metrics(task_name, success)
            for agent in agents:
                metrics_tracker.update_agent_metrics(agent.name)

    # Collect final results
    for task in task_manager.list_tasks():
        results["tasks"][task["name"]] = {
            "success_rate": metrics_tracker.get_task_success_rate(task["name"])
        }

    for agent in agents:
        results["agents"][agent.name] = metrics_tracker.get_agent_selection_count(agent.name)

    # Save results to JSON
    with open(EXPERIMENT_RESULTS_FILE, "w") as file:
        json.dump(results, file, indent=4)

    print(f"\n✅ Experiment completed. Results saved to `{EXPERIMENT_RESULTS_FILE}`")
    log_event(f"Experiment completed. Results saved to {EXPERIMENT_RESULTS_FILE}")

    # Show metrics visualization
    print("📊 Generating visualizations...")
    plot_task_success_rates()
    plot_agent_selection_counts()

if __name__ == "__main__":
    run_experiment(num_runs=20)
