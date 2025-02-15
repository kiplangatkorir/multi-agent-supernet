import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.metrics import MetricsTracker

metrics_tracker = MetricsTracker()

class Controller:
    """ 
    Manages task execution, selects agents dynamically, and updates metrics.
    """

    def __init__(self, supernet):
        self.supernet = supernet

    def allocate_agents(self, task):
        return self.supernet.sample_architecture(task)

    def execute_task(self, task):
        agents = self.allocate_agents(task)
        print(f"Executing task: {task['name']} with {', '.join(a.name for a in agents)}")

        success = any(agent.execute(task) for agent in agents)

        metrics_tracker.update_task_metrics(task["name"], success)

        for agent in agents:
            metrics_tracker.update_agent_metrics(agent.name)

        print(f"Task {task['name']} {'succeeded' if success else 'failed'}.\n")
        return success
