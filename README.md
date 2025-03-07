     
# **Multi-Agent Supernet: AI Agent Orchestration Kit**   

A flexible AI toolkit for **adaptive multi-agent selection and orchestration**.  
Inspired by *Multi-agent Architecture Search via Agentic Supernet*, this system dynamically selects AI agents for tasks using **probabilistic sampling, reinforcement learning, and cost-aware execution**.  

## **🔥 Features**  
✅ **Dynamic Agent Selection** – Tasks are matched with the best agents in real-time  
✅ **Monte Carlo Sampling** – Ensures efficient, adaptive agent selection  
✅ **Entropy Regularization** – Prevents system collapse into a single agent  
✅ **Cost-Aware Execution** – Simple tasks use lightweight agents to save resources  
✅ **Agent Specialization** – Each agent has unique capabilities and tools  
✅ **Real-World APIs** – Agents use **Finance, Research, Security, and Medical APIs**  
✅ **Persistent Task Storage** – Uses SQLite to save and manage registered tasks  
✅ **Task Auto-Registration** – Missing tasks are automatically registered  
✅ **Task Success Tracking** – Measures agent performance over multiple runs  
✅ **Agent Memory & Knowledge Graph** – Agents learn from past tasks  
✅ **Visual Insights** – Charts for success rates and agent selection trends  

## **🛠 Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/multi-agent-supernet.git
cd multi-agent-supernet
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

## **🚀 Quick Start**  

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

### **4️⃣ Auto-Register Tasks**  
If a task isn’t found, it is **automatically registered**.  

```bash
python main.py --run "Analyze stock trends"
```
✅ **Output:**  
```
⚠ Task 'Analyze stock trends' not found. Auto-registering...
✅ Task 'Analyze stock trends' registered with complexity 5.
📈 AAPL current price: 182.50
```

### **5️⃣ Show Task Success Rates & Agent Selection Stats**  
```bash
python main.py --metrics
```
✅ **Output:**  
📊 **A bar chart of task success rates & agent selection frequencies will appear.**

## **🤖 Creating Custom Agents**  
You can create new agents dynamically using the built-in CLI.

### **1️⃣ Create a Medical Agent**  
```bash
python scripts/create_agent.py
```
✅ **Example Input:**  
```
Enter agent class name: MedicalAgent
```
✅ **Expected Output:**  
```
✅ Specialized Agent 'MedicalAgent' created successfully at agents/medical_agent.py (Field: Medical, Tools: ['PubMed API', 'Medical Diagnosis Database'])
```

### **2️⃣ List Available Agents**  
```bash
python main.py --list-agents
```
✅ **Output:**  
```
📋 Available Agents:
 - BasicAgent (Capability: 1, Cost: 1)
 - MidAgent (Capability: 5, Cost: 3)
 - ExpertAgent (Capability: 10, Cost: 8)
 - FinancialAgent (Capability: 8, Cost: 6)
 - MedicalAgent (Capability: 9, Cost: 7)
```

### **3️⃣ Test an Agent**
```bash
python main.py --test-agent MedicalAgent
```
✅ **Expected Output:**  
```
✅ MedicalAgent executed task: MedicalAgent using PubMed API to analyze: Diagnose fever symptoms
```
## **📌 Advanced Usage**  

### **🔄 Running Multiple Tasks in a Script**  
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

## **🛠 Tools Available for Agents**
Each agent type has **access to specialized tools** for real-world execution.

| **Agent Type**       | **Specialization**                         | **Tools** |
|----------------------|------------------------------------------|----------------------|
| **ResearchAgent**    | Analyzing academic papers, summarizing | Uses **ArXiv API, GPT Summarization** 📚 |
| **FinancialAgent**   | Stock analysis, economic trends        | Uses **Yahoo Finance API** 💰 |
| **MarketingAgent**   | Ad optimization, consumer insights     | Uses **Sentiment Analysis API** 📊 |
| **SecurityAgent**    | Detecting threats, cybersecurity       | Uses **Threat Intelligence APIs** 🔐 |
| **MedicalAgent**     | Diagnosing symptoms, medical insights  | Uses **PubMed API, Medical Databases** 🏥 |
| **LegalAgent**       | Analyzing contracts, compliance        | Uses **Case Law Database** ⚖️ |

✅ **Agents now interact with real-world APIs to process their tasks!**

## **📊 Visualizing Agent Performance**  
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

✅ **These plots help optimize agent selection and track efficiency over time.**  

## **📖 Roadmap & To-Do**  
- [ ] **FastAPI API** – Expose task management as a web service  
- [ ] **Docker Support** – Deploy as a scalable microservice  
- [ ] **Logging & Analytics** – Track agent performance over time  
- [ ] **Web Dashboard** – Live charts to visualize AI agent trends  
- [ ] **Agent Collaboration** – Allow multiple agents to work on tasks together  
- [ ] **Reinforcement Learning** – Improve agent decision-making with experience  

## **📝 Citation**  
If you're inspired by this work, check out the original paper:  
📄 **Multi-agent Architecture Search via Agentic Supernet** – [arXiv](https://arxiv.org/abs/2502.04180)  

## **🚀 Contribute & Get Involved**
We welcome contributions from developers and AI enthusiasts!  
🔹 **Open an issue or PR** to suggest improvements  
🔹 **Fork the repo** and build custom agents  
🔹 **Join the discussion** in the community  

Would love feedback & contributions! Open an issue or PR. 🚀  
