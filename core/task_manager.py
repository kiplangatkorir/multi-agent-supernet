import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import json
import os
from utils.logger import log_event  # 🆕 Import logging utility

TASKS_FILE = "tasks.json"

class TaskManager:
    """ 
    A flexible task manager that allows developers to define, register, and retrieve tasks dynamically.
    """

    def __init__(self):
        """
        Initializes the task manager and loads existing tasks.
        """
        self.tasks = {}
        self.load_tasks()

    def register_task(self, name, complexity):
        """
        Registers a new task dynamically and saves it persistently.

        Args:
            name (str): Task name.
            complexity (int): Task complexity level.
        """
        if name in self.tasks:
            raise ValueError(f"⚠ Task '{name}' is already registered.")
        self.tasks[name] = {"name": name, "complexity": complexity}
        self.save_tasks()
        log_event(f"✅ Task '{name}' registered with complexity {complexity}.")

    def get_task(self, name):
        """
        Retrieves a task by name.

        Args:
            name (str): The task name.

        Returns:
            dict or None: Task details if found, otherwise None.
        """
        return self.tasks.get(name)

    def list_tasks(self):
        """
        Returns a list of all registered tasks.

        Returns:
            list: A list of task dictionaries.
        """
        return list(self.tasks.values())

    def remove_task(self, name):
        """
        Removes a task by name and updates storage.

        Args:
            name (str): The task name to remove.
        """
        if name in self.tasks:
            del self.tasks[name]
            self.save_tasks()
            log_event(f"🗑 Task '{name}' removed.")
        else:
            print(f"⚠ Task '{name}' not found.")

    def clear_tasks(self):
        """
        Clears all registered tasks and resets the storage file.
        """
        confirm = input("⚠ Are you sure you want to delete ALL tasks? (yes/no): ")
        if confirm.lower() == "yes":
            self.tasks.clear()
            self.save_tasks()
            log_event("🗑 All tasks have been cleared.")
            print("✅ Task list cleared.")
        else:
            print("❌ Task clearing aborted.")

    def save_tasks(self):
        """
        Saves tasks to a JSON file.
        """
        try:
            with open(TASKS_FILE, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except Exception as e:
            log_event(f"❌ Error saving tasks: {e}")
            print(f"⚠ Could not save tasks: {e}")

    def load_tasks(self):
        """
        Loads tasks from a JSON file if it exists.
        """
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r") as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                log_event("⚠ Error loading tasks: Corrupted file. Resetting...")
                print("⚠ Error loading tasks: Corrupted file. Resetting...")
                self.tasks = {}
                self.save_tasks()
