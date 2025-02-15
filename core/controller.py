# core/task_manager.py

class TaskManager:
    """ 
    A flexible task manager that allows developers to define, register, and retrieve tasks dynamically.
    """

    def __init__(self):
        """
        Initializes an empty task list.
        """
        self.tasks = {}

    def register_task(self, name, complexity):
        """
        Registers a new task dynamically.

        Args:
            name (str): Task name.
            complexity (int): Task complexity level.
        """
        if name in self.tasks:
            raise ValueError(f"Task '{name}' is already registered.")
        self.tasks[name] = {"name": name, "complexity": complexity}

    def get_task(self, name):
        """
        Retrieves a task by name.

        Args:
            name (str): The task name.

        Returns:
            dict: Task details if found, otherwise None.
        """
        return self.tasks.get(name, None)

    def list_tasks(self):
        """
        Returns a list of all registered tasks.

        Returns:
            list: A list of task dictionaries.
        """
        return list(self.tasks.values())

    def remove_task(self, name):
        """
        Removes a task by name.

        Args:
            name (str): The task name to remove.
        """
        if name in self.tasks:
            del self.tasks[name]

    def clear_tasks(self):
        """
        Clears all registered tasks.
        """
        self.tasks.clear()
