
# Multi-Agent Supernet   

An adaptive **multi-agent system** inspired by the paper *Multi-agent Architecture Search via Agentic Supernet*.  
This repository implements a **probabilistic agentic supernet** that dynamically selects AI agents based on task complexity using **Monte Carlo sampling, entropy regularization, and cost-aware selection**.

##  Key Features  
**Dynamic Agent Selection** – Tasks are matched with the best agents in real time  
**Monte Carlo Sampling** – Ensures efficient, adaptive agent selection  
**Entropy Regularization** – Prevents the system from collapsing into a single agent choice  
**Cost-Aware Execution** – Simple tasks use lightweight agents, saving resources  
**Reinforcement Learning** – Agents improve selection probabilities over time  

## 🛠 Installation  

Clone the repository:  
```bash
git clone https://github.com/your-username/multi-agent-supernet.git
cd multi-agent-supernet
```

Install dependencies:  
```bash
pip install numpy
```

## Quick Start  

Run the multi-agent system simulation:  
```bash
python main.py
```

##  Example Output  

```bash
Executing task: Simple Arithmetic with MidAgent, MidAgent
Task Simple Arithmetic succeeded.

Executing task: Web Navigation with ExpertAgent
Task Web Navigation succeeded.

Executing task: Advanced Code Generation with ExpertAgent, ExpertAgent
Task Advanced Code Generation succeeded.

Final Agent Selection Probabilities: [0.259 0.316 0.425]
```

## 📌 To-Do  
- [ ] **Improve agent collaboration** (e.g., debate, reflection)  
- [ ] **Implement neural controller** for agent selection  
- [ ] **Optimize cost-aware penalties**  

## 📝 Citation  
If you're inspired by this work, check out the original paper:  
📄 **Multi-agent Architecture Search via Agentic Supernet** – [arXiv](https://arxiv.org/abs/2502.04180)  


Would love feedback & contributions! Open an issue or PR. 🚀  

