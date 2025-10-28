import json
import os

MEMORY_FILE = "memory.json"

class AgentMemory:
    """
    Memory module that allows agents to store and retrieve past interactions.
    """

    def __init__(self):
        self.memory = self._load_memory()

    def _load_memory(self):
        """ Load memory from file if available. """
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("⚠ Memory file is corrupted. Resetting...")
                return {}
        return {}

    def store(self, agent_name, key, value):
        """ Stores a memory entry for an agent. """
        if agent_name not in self.memory:
            self.memory[agent_name] = {}
        self.memory[agent_name][key] = value
        self._save_memory()

    def retrieve(self, agent_name, key):
        """ Retrieves a stored memory entry. """
        return self.memory.get(agent_name, {}).get(key, None)

    def forget(self, agent_name, task):
        """ Removes a specific task from an agent's memory. """
        if agent_name in self.memory and task in self.memory[agent_name]:
            del self.memory[agent_name][task]
            self._save_memory()

    def clear_memory(self, agent_name=None):
        """ Clears memory for a specific agent or all agents. """
        if agent_name:
            self.memory[agent_name] = {}
        else:
            self.memory = {}
        self._save_memory()

    def _save_memory(self):
        """ Saves memory to a file. """
        with open(MEMORY_FILE, "w") as file:
            json.dump(self.memory, file, indent=4)
