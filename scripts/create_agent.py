import os

TEMPLATE = '''from agents.base_agent import BaseAgent

class {class_name}(BaseAgent):
    """
    Custom AI agent for specialized tasks.
    """

    def __init__(self):
        super().__init__(name="{class_name}", capability=2, cost=1)

    def execute(self, task):
        """
        Executes the assigned task.

        Args:
            task (str): The task to be performed.

        Returns:
            str: The result of the execution.
        """
        return f"{class_name} executing: {{task}}"
'''

def create_agent(agent_name):
    """ Creates a new agent file from a template. """
    filename = f"agents/{agent_name.lower()}_agent.py"

    if os.path.exists(filename):
        print(f"⚠ Agent '{agent_name}' already exists!")
        return

    with open(filename, "w") as f:
        f.write(TEMPLATE.format(class_name=agent_name))

    print(f"✅ Agent '{agent_name}' created successfully at {filename}")

if __name__ == "__main__":
    agent_name = input("Enter agent class name: ")
    create_agent(agent_name)
