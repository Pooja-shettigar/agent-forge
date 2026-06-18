# 🚀 Agent Forge

> **AI Startup Factory — Build a startup and watch an AI company operate autonomously.**

Agent Forge is a multi-agent AI system that transforms a startup idea into a structured business strategy through autonomous collaboration between specialized AI agents.

Built as a capstone project for the **Google + Kaggle 5-Day AI Agents Intensive Vibe Coding Course**, Agent Forge demonstrates modern agentic engineering concepts including orchestration, skills, memory, evaluation, and context engineering.

---

# 📌 Problem Statement

Most AI applications are limited to chatbot-style interactions and lack the ability to coordinate multiple specialized reasoning processes.

Entrepreneurs often need support across several business domains:

- Market validation
- Go-to-market strategy
- Funding analysis
- Risk assessment

Performing these tasks manually is time-consuming and fragmented.

---

# 💡 Solution

Agent Forge acts as an AI Startup Factory.

A user provides a startup idea such as:

> "Build an AI SaaS for dentists."

The system creates a virtual startup team consisting of specialized AI agents that collaborate to:

- Research the market
- Define positioning and strategy
- Evaluate investment opportunities
- Analyze risks and security concerns
- Generate a consolidated startup report

---

# 🏗️ Architecture
> ![Architecture](assets/agent_architecture.png)
---

# 🤖 Agent Design

## CEO Agent
- Task delegation
- Agent coordination
- Report consolidation
- Workflow management

## Research Agent
**Skill:** Market Research

- Market analysis
- Industry trends
- Customer validation
- Opportunity assessment

## Marketing Agent
**Skill:** GTM Strategy

- Go-to-market planning
- Positioning strategy
- Customer acquisition

## Investor Agent
**Skill:** Investor Analysis

- Funding analysis
- Investment attractiveness
- Revenue opportunity evaluation

## Security Agent
**Skill:** Security Review

- Risk assessment
- Compliance considerations
- Security review

---

# 🧠 Context Engineering

Agent Forge applies context engineering principles through:

- Instructions
- Memory
- Skills
- Tools
- Guardrails

---

# 🔄 A2A (Agent-to-Agent Communication)

The CEO Agent orchestrates specialized agents using an A2A workflow.

```text
CEO Agent
 ├── Research Agent
 ├── Marketing Agent
 ├── Investor Agent
 └── Security Agent
```

---

# 🎯 A2UI (Agent-to-User Interface)

Users interact with the system through a Streamlit Boardroom interface that provides:

- Startup idea input
- Agent outputs
- Evaluation dashboard
- Startup history

---

# 🧩 Skills & Procedural Memory

Each specialized agent uses dedicated skills:

- Market Research Skill
- GTM Strategy Skill
- Investor Analysis Skill
- Security Review Skill

Skills represent procedural memory and domain expertise.

---

# 📊 Evaluation Engine

The Evaluation Engine measures:

- Intent Satisfaction
- Feasibility
- Risk Score
- Confidence Score

> Generation is becoming commoditized. Verification is the differentiator.

---

# 🗄️ Memory Layer

SQLite is used as persistent memory.

### Stored Data

- Startup ideas
- Generated reports
- Historical records

### Capabilities

- Startup history
- Report retrieval
- Persistent storage

---

# 🖥️ Features

- ✅ Multi-Agent Architecture
- ✅ CEO Agent Orchestration
- ✅ Agent Skills
- ✅ Context Engineering
- ✅ Evaluation Dashboard
- ✅ SQLite Memory
- ✅ Startup History
- ✅ Boardroom Interface

---

# ⚙️ Technology Stack

| Component  | Technology                   |
|------------|------------------------------|
| LLM        | Gemini 2.5 Flash             |
| Frontend   | Streamlit                    |
| Database   | SQLite                       |
| Language   | Python                       |
| Memory     | SQLite                       |
| Evaluation | Rule-Based Evaluation Engine |

---

# 🚀 Getting Started

```bash
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# 📈 Future Enhancements

- MCP Integration
- Advanced Memory Retrieval
- Multi-Turn Startup Refinement
- Google Cloud Run Deployment
- Real-Time Web Research
- Advanced Evaluation Models

---

# 🎓 Course Concepts Demonstrated

- Vibe Coding
- Agentic Engineering
- Context Engineering
- Harness Engineering
- A2A
- A2UI
- Skills
- Procedural Memory
- Evaluation
- Multi-Agent Orchestration
- Memory Systems

---

# 👩‍💻 Author
**Pooja Shettigar**

Agent Forge — AI Startup Factory 🚀
