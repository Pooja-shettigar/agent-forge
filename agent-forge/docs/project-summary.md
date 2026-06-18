### Agent Forge

### Project Overview
Agent Forge is a multi-agent AI startup factory designed to transform a startup idea into a structured business plan through autonomous AI collaboration.

Instead of relying on a single chatbot, Agent Forge uses a CEO Agent that orchestrates multiple specialized agents responsible for market research, go-to-market strategy, investment analysis, and security assessment. The system demonstrates modern agentic engineering concepts including orchestration, skills, memory, evaluation, and context engineering.

### Problem Statement
Many AI applications are limited to simple question-answer interactions and lack the ability to perform coordinated, multi-step reasoning across specialized domains.

Entrepreneurs and innovators often need assistance across multiple business functions such as market validation, marketing strategy, funding analysis, and risk assessment. Performing these tasks manually can be time-consuming and fragmented.

### Solution
Agent Forge creates an autonomous startup advisory workflow powered by AI agents.

A user provides a startup idea, and the CEO Agent coordinates a team of specialized agents to generate:
        - Market research and opportunity analysis
        - Go-to-market strategy recommendations
        - Investor and funding insights
        - Security and risk assessments

The outputs are consolidated into a single startup report, evaluated for quality and feasibility, and stored for future retrieval.

### Architecture Summary
The system follows a multi-agent architecture powered by Gemini 2.5 Flash.

### Core Components
    * Streamlit Boardroom UI (A2UI) – User interaction layer
    * CEO Agent – Central orchestrator
    * Research Agent – Market analysis and validation
    * Marketing Agent – Go-to-market planning
    * Investor Agent – Funding and investment analysis
    * Security Agent – Risk and security review
    * Evaluation Engine – Startup assessment and scoring
    * SQLite Memory Layer – Startup history and report storage

### Agent Workflow
    * User submits a startup idea.
    * CEO Agent orchestrates specialized agents using A2A communication.
    * Each agent executes domain-specific skills.
    * Agent outputs are consolidated into a startup report.
    * The Evaluation Engine measures:
            - Intent Satisfaction
            - Feasibility
            - Risk Score
            - Confidence Score
    * Reports and evaluations are stored in SQLite memory.


### Key Concepts Demonstrated
This project demonstrates concepts covered in the Google + Kaggle AI Agents course:

    Vibe Coding
    Agentic Engineering
    Context Engineering
    Harness Engineering
    Agent-to-Agent Communication (A2A)
    Agent-to-User Interface (A2UI)
    Skills and Procedural Memory
    Evaluation Frameworks
    Multi-Agent Orchestration
    Memory Systems

---
### Technology Stack
| Component  | Technology                   |
|------------|------------------------------|
| LLM        | Gemini 2.5 Flash             |
| Frontend   | Streamlit                    |
| Database   | SQLite                       |
| Language   | Python                       |
| Memory     | SQLite                       |
| Evaluation | Rule-Based Evaluation Engine |

---
### Future Enhancements
    MCP (Model Context Protocol) Integration
    Advanced Memory Retrieval
    Real-Time Web Research
    Cloud Run Deployment
    Enhanced Evaluation Models
    Multi-Turn Startup Refinement


### Outcome
Agent Forge demonstrates how multiple AI agents can collaborate to perform complex business analysis tasks while maintaining memory, evaluation, and orchestration layers. The project serves as both a portfolio-quality application and a practical implementation of modern agentic AI system design.