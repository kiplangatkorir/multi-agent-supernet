import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import json
import os
from utils.logger import log_event  # Import logging utility

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
            print(f"⚠ Task '{name}' is already registered.")
            return  # Prevent duplicate entries
        self.tasks[name] = {"name": name, "complexity": complexity}
        self.save_tasks()
        log_event(f"✅ Task '{name}' registered with complexity {complexity}.")
        print(f"✅ Task '{name}' registered with complexity {complexity}.")

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
            print(f"🗑 Task '{name}' removed.")  # Only print once
        else:
            print(f"⚠ Task '{name}' not found.")

    def clear_tasks(self):
        """
        Clears all registered tasks and resets the storage file.
        """
        if not self.tasks:  # Prevent unnecessary clear message
            print("⚠ No tasks to clear.")
            return
        
        self.tasks.clear()
        self.save_tasks()
        log_event("🗑 All tasks have been cleared.")
        print("🗑 All tasks have been cleared.")  # Only print once

    def save_tasks(self):
        """
        Saves tasks to a JSON file.
        """
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

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
