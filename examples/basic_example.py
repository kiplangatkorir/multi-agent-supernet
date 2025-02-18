import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core.task_manager import TaskManager
from core.controller import Controller
from core.agentic_supernet import AgenticSupernet
from agents.basic_agent import BasicAgent
from agents.mid_agent import MidAgent
from agents.expert_agent import ExpertAgent

# Initialize system
task_manager = TaskManager()
agents = [BasicAgent(), MidAgent(), ExpertAgent()]
supernet = AgenticSupernet(agents)
controller = Controller(supernet)

# Register tasks
task_manager.register_task("Data Cleaning", complexity=3)
task_manager.register_task("Multi-Step Reasoning", complexity=7)

# Execute tasks
for task in task_manager.list_tasks():
    controller.execute_task(task["name"])