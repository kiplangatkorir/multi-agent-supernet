import sys
import os
import argparse
import yaml
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.agent_loader import load_agents  # Dynamically loads all agents
from core.agentic_supernet import AgenticSupernet
from core.controller import Controller
from core.task_manager import TaskManager
from core.memory import AgentMemory
from core.knowledge_graph import KnowledgeGraph
from core.debate import DebateManager
from core.collaboration import AgentTeam
from utils.metrics import MetricsTracker
from utils.visualization import plot_task_success_rates, plot_agent_selection_counts
from utils.logger import log_event

def load_config(config_path="configs/settings.yaml"):
    """Loads configuration from a YAML file."""
    try:
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"⚠ Warning: Config file {config_path} not found. Using default settings.")
        return {}

def run_task(controller, task_name, metrics_tracker):
    """Executes a registered task and tracks performance metrics."""
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
    memory = AgentMemory()
    knowledge_graph = KnowledgeGraph()
    agents = load_agents()  # Load all agents dynamically
    supernet = AgenticSupernet(agents, entropy_weight=config.get("entropy_weight", 0.1))
    controller = Controller(supernet)
    debate_manager = DebateManager(agents)
    team = AgentTeam(agents)

    parser = argparse.ArgumentParser(description="Multi-Agent Supernet AI Kit")

    # Task Management
    parser.add_argument("--register", nargs=2, metavar=("TASK_NAME", "COMPLEXITY"), help="Register a new task")
    parser.add_argument("--remove", metavar="TASK_NAME", help="Remove a registered task")
    parser.add_argument("--clear", action="store_true", help="Remove all tasks")
    parser.add_argument("--list", action="store_true", help="List all registered tasks")
    parser.add_argument("--run", metavar="TASK_NAME", help="Run a registered task")
    parser.add_argument("--metrics", action="store_true", help="Show task success rates and agent selection frequencies")

    # Agent Management
    parser.add_argument("--list-agents", action="store_true", help="List all available agents")
    parser.add_argument("--test-agent", metavar="AGENT_NAME", help="Test an agent on a sample task")

    # Memory Management
    parser.add_argument("--forget", nargs=2, metavar=("AGENT", "TASK"), help="Forget a specific task from memory")
    parser.add_argument("--clear-memory", metavar="AGENT", nargs="?", help="Clear memory for an agent (or all agents)")
    parser.add_argument("--query-memory", metavar="AGENT", nargs="?", help="Query an agent's memory")

    # Knowledge Graph
    parser.add_argument("--add-fact", nargs=3, metavar=("SUBJECT", "RELATION", "OBJECT"), help="Add a fact to the knowledge graph")
    parser.add_argument("--query-facts", metavar="SUBJECT", help="Retrieve knowledge about a subject")
    parser.add_argument("--reason", nargs=2, metavar=("START", "END"), help="Find reasoning path between two concepts")

    # Agent Debate & Collaboration
    parser.add_argument("--debate", metavar="TASK_NAME", help="Run a debate on a task result")
    parser.add_argument("--collaborate", metavar="TASK_NAME", help="Execute a task with multiple agents")

    args = parser.parse_args()

    # Task Management
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
        print("📋 Registered Tasks:" if tasks else "⚠ No tasks registered.")
        for task in tasks:
            print(f" - {task['name']} (Complexity: {task['complexity']})")

    if args.run:
        run_task(controller, args.run, metrics_tracker)

    if args.metrics:
        print("📊 Visualizing Task Success Rates & Agent Selection Frequency...")
        plot_task_success_rates()
        plot_agent_selection_counts()

    # Agent Management
    if args.list_agents:
        print("📋 Available Agents:")
        for agent in agents:
            print(f" - {agent.name} (Capability: {agent.capability}, Cost: {agent.cost})")

    if args.test_agent:
        agent = next((a for a in agents if a.name.lower() == args.test_agent.lower()), None)
        if agent:
            sample_task = "Sample Task"
            result = agent.execute(sample_task)
            print(f"✅ {agent.name} executed task: {result}")
        else:
            print(f"⚠ Agent '{args.test_agent}' not found.")

    # Memory Management
    if args.forget:
        agent, task = args.forget
        memory.forget(agent, task)
        print(f"🗑 Memory cleared for task '{task}' under agent '{agent}'.")

    if args.clear_memory:
        agent = args.clear_memory
        memory.clear_memory(agent)
        print(f"🔄 Memory cleared for {'all agents' if not agent else f'agent {agent}'}.")

    if args.query_memory:
        agent = args.query_memory
        memories = memory.memory.get(agent, {})
        print(f"📋 Memory for '{agent}': {memories}" if memories else f"⚠ No memory found for '{agent}'.")

    # Knowledge Graph
    if args.add_fact:
        subject, relation, obj = args.add_fact
        knowledge_graph.add_fact(subject, relation, obj)
        print(f"✅ Fact added: {subject} → ({relation}) → {obj}")

    if args.query_facts:
        subject = args.query_facts
        facts = knowledge_graph.get_relations(subject)
        print(f"📚 Knowledge about '{subject}': {facts}" if facts else f"⚠ No knowledge found for '{subject}'.")

    if args.reason:
        start, end = args.reason
        path = knowledge_graph.find_path(start, end)
        print(f"🧠 Reasoning Path: {' → '.join(path)}" if path else f"⚠ No reasoning path found between '{start}' and '{end}'.")

    # Agent Collaboration & Debate
    if args.debate:
        task = args.debate
        initial_result = controller.execute_task(task)
        final_result = debate_manager.debate(task, initial_result)
        print(final_result)

if args.collaborate:
    task = args.collaborate
    result = team.execute_task(task)  # ✅ FIXED: Call execute_task() instead
    print(f"🤝 Collaboration Result: {result}")

