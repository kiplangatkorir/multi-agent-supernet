import sys
import os
import argparse
import yaml
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.agent_loader import load_agents  # 🆕 Dynamically loads all agents
from core.agentic_supernet import AgenticSupernet
from core.controller import Controller
from core.task_manager import TaskManager
from utils.metrics import MetricsTracker
from utils.visualization import plot_task_success_rates, plot_agent_selection_counts
from utils.logger import log_event

def load_config(config_path="configs/settings.yaml"):
    """
    Loads configuration from a YAML file.
    
    Args:
        config_path (str): Path to the config file.
    
    Returns:
        dict: Loaded configuration dictionary.
    """
    try:
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"⚠ Warning: Config file {config_path} not found. Using default settings.")
        return {}

def run_task(controller, task_name, metrics_tracker):
    """
    Executes a registered task and tracks performance metrics.

    Args:
        controller (Controller): The controller managing agent execution.
        task_name (str): Name of the task to execute.
        metrics_tracker (MetricsTracker): Tracks task and agent performance.
    """
    task = task_manager.get_task(task_name)
    if task:
        try:
            success = controller.execute_task(task)
            metrics_tracker.update_task_metrics(task_name, success)
            log_event(f"✅ Task '{task_name}' {'succeeded' if success else 'failed'}.")
            success_rate = metrics_tracker.get_task_success_rate(task_name)
            print(f"📊 Success rate for '{task_name}': {success_rate:.2%}")

        except Exception as e:
            print(f"❌ Error executing task '{task_name}': {e}")
            log_event(f"❌ Error executing task '{task_name}': {e}")
    else:
        print(f"⚠ Task '{task_name}' not found. Please register it first.")

if __name__ == "__main__":
    config = load_config()

    task_manager = TaskManager()
    metrics_tracker = MetricsTracker()
    agents = load_agents()  # 🆕 Automatically loads all agents
    supernet = AgenticSupernet(agents, entropy_weight=config.get("entropy_weight", 0.1))
    controller = Controller(supernet)

    parser = argparse.ArgumentParser(description="Multi-Agent Supernet AI Kit")
    parser.add_argument("--register", nargs=2, metavar=("TASK_NAME", "COMPLEXITY"), help="Register a new task")
    parser.add_argument("--remove", metavar="TASK_NAME", help="Remove a registered task")
    parser.add_argument("--clear", action="store_true", help="Remove all tasks")
    parser.add_argument("--list", action="store_true", help="List all registered tasks")
    parser.add_argument("--run", metavar="TASK_NAME", help="Run a registered task")
    parser.add_argument("--metrics", action="store_true", help="Show task success rates and agent selection frequencies")

    # 🆕 New Features
    parser.add_argument("--list-agents", action="store_true", help="List all available agents")
    parser.add_argument("--test-agent", metavar="AGENT_NAME", help="Test an agent on a sample task")
    parser.add_argument("--api-mode", action="store_true", help="Run in API mode (FastAPI)")

    args = parser.parse_args()

    if args.register:
        task_name, complexity = args.register
        try:
            task_manager.register_task(task_name, int(complexity))
            print(f"✅ Task '{task_name}' registered with complexity {complexity}.")
        except ValueError as e:
            print(f"⚠ {e}")

    if args.remove:
        confirmation = input(f"⚠ Are you sure you want to delete task '{args.remove}'? (yes/no): ")
        if confirmation.lower() == "yes":
            task_manager.remove_task(args.remove)
            print(f"🗑 Task '{args.remove}' removed.")
        else:
            print("❌ Task removal canceled.")

    if args.clear:
        confirmation = input("⚠ Are you sure you want to delete ALL tasks? (yes/no): ")
        if confirmation.lower() == "yes":
            task_manager.clear_tasks()
            print("🗑 All tasks have been cleared.")
        else:
            print("❌ Task clearing canceled.")

    if args.list:
        tasks = task_manager.list_tasks()
        if tasks:
            print("📋 Registered Tasks:")
            for task in tasks:
                print(f" - {task['name']} (Complexity: {task['complexity']})")
        else:
            print("⚠ No tasks registered.")

    if args.run:
        run_task(controller, args.run, metrics_tracker)

    if args.metrics:
        print("📊 Visualizing Task Success Rates & Agent Selection Frequency...")
        plot_task_success_rates()
        plot_agent_selection_counts()

    # 🆕 List all detected agents
    if args.list_agents:
        print("📋 Available Agents:")
        for agent in agents:
            print(f" - {agent.name} (Capability: {agent.capability}, Cost: {agent.cost})")

    # 🆕 Test an agent with a sample task
    if args.test_agent:
        agent = next((a for a in agents if a.name.lower() == args.test_agent.lower()), None)
        if agent:
            sample_task = "Sample Task"
            result = agent.execute(sample_task)
            print(f"✅ {agent.name} executed task: {result}")
        else:
            print(f"⚠ Agent '{args.test_agent}' not found.")


