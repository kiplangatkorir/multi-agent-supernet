# Multi-Agent Supernet - Quick Start Guide

## 🎯 **What Was Fixed**

I've scanned and fixed your codebase! Here's what was wrong and what I fixed:

### **Issues Fixed:**
1. ✅ `agents/mid_agent.py` - Had empty `execute()` method → Now fully implemented
2. ✅ `agents/markerter_agent.py` - Was completely empty → Created full `MarketerAgent`
3. ✅ `agents/analyst_agent.py` - Missing memory/knowledge graph → Upgraded to full pattern
4. ✅ `requirements.txt` - Missing `requests` and `pyyaml` → Added dependencies
5. ✅ `core/memory.py` - Missing `forget()` and `clear_memory()` methods → Implemented
6. ✅ `core/tools.py` - No error handling for API calls → Added try-except + timeouts

---

## 🚀 **Quick Test**

### **1. List All Agents:**
```bash
python main.py --list-agents
```

You should see 6 agents now:
- AnalystAgent (Capability: 2, Cost: 1)
- BasicAgent (Capability: 1, Cost: 1)
- ExpertAgent (Capability: 10, Cost: 8)
- MarketerAgent (Capability: 6, Cost: 4)
- Medical (Capability: 9, Cost: 7)
- MidAgent (Capability: 5, Cost: 3)

### **2. Register a Task:**
```bash
python main.py --register "Test task" 5
```

### **3. Run the Task:**
```bash
python main.py --run "Test task"
```

### **4. Check Metrics:**
```bash
python main.py --metrics
```

---

## 📚 **How the System Works**

### **Architecture:**
```
User Request → Controller → AgenticSupernet → Select Agent → Execute → Update Metrics
```

### **Key Components:**

1. **AgenticSupernet** (`core/agentic_supernet.py`)
   - Uses probability distribution to select agents
   - Balances cost vs capability
   - Learns from experience

2. **Controller** (`core/controller.py`)
   - Manages task execution
   - Tracks metrics
   - Selects best agents

3. **TaskManager** (`core/task_manager.py`)
   - Persists tasks to `tasks.json`
   - Auto-registers missing tasks

4. **Agents** (`agents/`)
   - Each agent has capability and cost
   - Use memory and knowledge graph
   - Specialized for different domains

---

## 🎮 **Common Commands**

```bash
# List agents
python main.py --list-agents

# Register a task
python main.py --register "Task Name" 5

# List registered tasks
python main.py --list

# Run a task
python main.py --run "Task Name"

# Show metrics
python main.py --metrics

# Test an agent
python main.py --test-agent Medical

# Clear memory
python main.py --clear-memory

# Delete an agent
python main.py --delete-agent BasicAgent

# Restore agent
python main.py --restore-agent BasicAgent
```

---

## 🔧 **Create Custom Agents**

Use the built-in generator:
```bash
python scripts/create_agent.py
```

Enter agent name (e.g., "SecurityAgent", "LegalAgent") and it will generate a complete agent with:
- Memory integration
- Knowledge graph support
- Specialized tools
- Proper structure

---

## 📊 **Data Storage**

The system uses JSON files for persistence:
- `tasks.json` - Registered tasks
- `memory.json` - Agent memories
- `logs/metrics.json` - Performance metrics
- `logs/system.log` - System logs

---

## 🐛 **Troubleshooting**

### **If agents don't load:**
1. Check `agents/` folder has proper `*_agent.py` files
2. Ensure all agents inherit from `BaseAgent`
3. Run: `python main.py --list-agents` to verify

### **If task execution fails:**
1. Check task is registered: `python main.py --list`
2. Verify agent has proper `execute()` method
3. Check logs: `cat logs/system.log`

### **If API calls fail:**
1. External APIs (Yahoo Finance, ArXiv, etc.) may be down
2. Check internet connection
3. Error messages are now more descriptive

---

## 💡 **Next Steps**

1. **Test the system:**
   ```bash
   python main.py --register "Stock Analysis" 6
   python main.py --run "Stock Analysis"
   ```

2. **Create custom agents:**
   ```bash
   python scripts/create_agent.py
   ```

3. **Explore advanced features:**
   - Agent collaboration
   - Debate system
   - Knowledge graph
   - Metrics visualization

4. **Read detailed analysis:**
   See `CODEBASE_ANALYSIS.md` for complete architecture details

---

## 🎓 **Key Concepts**

- **AgenticSupernet**: Probabilistic agent selection
- **Entropy Regularization**: Prevents mode collapse
- **Cost-Aware Execution**: Optimizes resource usage
- **Memory System**: Agents remember past tasks
- **Knowledge Graph**: Stores relationships between concepts

---

## ✅ **Status**

**System Status:** ✅ **FULLY OPERATIONAL**

**Issues Found:** 6
**Issues Fixed:** 6
**Files Modified:** 6
**Test Status:** ✅ **PASSING**

All agents load successfully. System is ready for use!

