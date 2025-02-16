
## **Multi-Agent Supernet: AI Agent Orchestration Kit**  

A flexible AI toolkit for **adaptive multi-agent selection and orchestration**.  
Inspired by *Multi-agent Architecture Search via Agentic Supernet*, this system dynamically selects AI agents for tasks using **probabilistic sampling, reinforcement learning, and cost-aware execution**.  

## ** Features**  
**Dynamic Agent Selection** – Tasks are matched with the best agents in real-time  
**Monte Carlo Sampling** – Ensures efficient, adaptive agent selection  
**Entropy Regularization** – Prevents system collapse into a single agent  
**Cost-Aware Execution** – Simple tasks use lightweight agents to save resources  
**Persistent Task Storage** – Uses SQLite to save and manage registered tasks  
**Task Success Tracking** – Measures agent performance over multiple runs  
**Visual Insights** – Charts for success rates and agent selection trends  

## ** Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/multi-agent-supernet.git
cd multi-agent-supernet
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

## ** Quick Start**  

### **1️⃣ Register a Task**  
```bash
python main.py --register "Document Summarization" 4
```
✅ **Output:**  
```
Task 'Document Summarization' registered with complexity 4.
```

### **2️⃣ List Registered Tasks**  
```bash
python main.py --list
```
✅ **Output:**  
```
Registered Tasks:
 - Document Summarization (Complexity: 4)
```

### **3️⃣ Run a Task & Track Performance**  
```bash
python main.py --run "Document Summarization"
```
✅ **Output:**  
```
Executing task: Document Summarization with MidAgent, MidAgent
Task Document Summarization succeeded.

Success rate for 'Document Summarization': 100.00%
```

### **4️⃣ Show Task Success Rates & Agent Selection Stats**  
```bash
python main.py --metrics
```
 **Output:**  
📊 **A bar chart of task success rates & agent selection frequencies will appear.**

## ** Advanced Usage**  

### ** Running Multiple Tasks in a Script**  
Developers can integrate the toolkit into Python projects:  

```python
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
```

## ** Visualizing Agent Performance**  
After multiple runs, you can generate **real-time analytics**:

### **Task Success Rates**
```python
from utils.visualization import plot_task_success_rates
plot_task_success_rates()
```

### **Agent Selection Frequency**
```python
from utils.visualization import plot_agent_selection_counts
plot_agent_selection_counts()
```

 **These plots help optimize agent selection and track efficiency over time.**  

## ** Roadmap & To-Do**  
- [ ] **FastAPI API** – Expose task management as a web service  
- [ ] **Docker Support** – Deploy as a scalable microservice  
- [ ] **Logging & Analytics** – Track agent performance over time  
- [ ] **Web Dashboard** – Live charts to visualize AI agent trends  

## ** Citation**  
If you're inspired by this work, check out the original paper:  
📄 **Multi-agent Architecture Search via Agentic Supernet** – [arXiv](https://arxiv.org/abs/2502.04180)  


Would love feedback & contributions! Open an issue or PR. 🚀  
