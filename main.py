
import argparse
import yaml
from agents.basic_agent import BasicAgent
from agents.mid_agent import MidAgent
from agents.expert_agent import ExpertAgent
from core.agentic_supernet import AgenticSupernet
from core.controller import Controller
from core.task_manager import TaskManager

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
        print(f"Warning: Config file {config_path} not found. Using default settings.")
        return {}

def initialize_agents():
    """
    Initializes available agents.
    
    Returns:
        list: A list of instantiated agent objects.
    """
    return [BasicAgent(), MidAgent(), ExpertAgent()]

def run_task(controller, task_name):
    """
    Executes a registered task.

    Args:
        controller (Controller): The controller managing agent execution.
        task_name (str): Name of the task to execute.
    """
    task = task_manager.get_task(task_name)
    if task:
        controller.execute_task(task)
    else:
        print(f"Task '{task_name}' not found. Please register it first.")

if __name__ == "__main__":
    config = load_config()

    task_manager = TaskManager()
    agents = initialize_agents()
    supernet = AgenticSupernet(agents, entropy_weight=config.get("entropy_weight", 0.1))
    controller = Controller(supernet)

    parser = argparse.ArgumentParser(description="Multi-Agent Supernet AI Kit")
    parser.add_argument("--register", nargs=2, metavar=("TASK_NAME", "COMPLEXITY"), help="Register a new task")
    parser.add_argument("--list", action="store_true", help="List all registered tasks")
    parser.add_argument("--run", metavar="TASK_NAME", help="Run a registered task")
    args = parser.parse_args()

    if args.register:
        task_name, complexity = args.register
        task_manager.register_task(task_name, int(complexity))
        print(f"Task '{task_name}' registered with complexity {complexity}.")

    if args.list:
        tasks = task_manager.list_tasks()
        print("Registered Tasks:")
        for task in tasks:
            print(f" - {task['name']} (Complexity: {task['complexity']})")

    if args.run:
        run_task(controller, args.run)
