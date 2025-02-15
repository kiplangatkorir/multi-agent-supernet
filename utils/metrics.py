import json
import os

METRICS_FILE = "logs/metrics.json"

class MetricsTracker:
    """
    Tracks task success rates, agent selection frequencies, and overall performance.
    """

    def __init__(self):
        """
        Initializes the metrics tracker and loads existing data.
        """
        self.metrics = {
            "tasks": {},  
            "agents": {}  
        }
        self.load_metrics()

    def update_task_metrics(self, task_name, success):
        """
        Updates success/failure counts for a task.

        Args:
            task_name (str): The name of the executed task.
            success (bool): Whether the task execution was successful.
        """
        if task_name not in self.metrics["tasks"]:
            self.metrics["tasks"][task_name] = {"success": 0, "failure": 0}

        if success:
            self.metrics["tasks"][task_name]["success"] += 1
        else:
            self.metrics["tasks"][task_name]["failure"] += 1

        self.save_metrics()

    def update_agent_metrics(self, agent_name):
        """
        Tracks how often an agent is selected.

        Args:
            agent_name (str): The name of the selected agent.
        """
        if agent_name not in self.metrics["agents"]:
            self.metrics["agents"][agent_name] = 0

        self.metrics["agents"][agent_name] += 1
        self.save_metrics()

    def get_task_success_rate(self, task_name):
        """
        Returns the success rate of a given task.

        Args:
            task_name (str): The name of the task.

        Returns:
            float: The success rate (0.0 to 1.0).
        """
        if task_name not in self.metrics["tasks"]:
            return 0.0

        task_data = self.metrics["tasks"][task_name]
        total_attempts = task_data["success"] + task_data["failure"]
        return task_data["success"] / total_attempts if total_attempts > 0 else 0.0

    def get_agent_selection_count(self, agent_name):
        """
        Returns how many times an agent has been selected.

        Args:
            agent_name (str): The name of the agent.

        Returns:
            int: The number of times the agent was chosen.
        """
        return self.metrics["agents"].get(agent_name, 0)

    def save_metrics(self):
        """
        Saves the metrics to a JSON file.
        """
        os.makedirs(os.path.dirname(METRICS_FILE), exist_ok=True)
        with open(METRICS_FILE, "w") as file:
            json.dump(self.metrics, file, indent=4)

    def load_metrics(self):
        """
        Loads metrics from a JSON file if it exists.
        """
        if os.path.exists(METRICS_FILE):
            with open(METRICS_FILE, "r") as file:
                self.metrics = json.load(file)
