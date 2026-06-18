### Architecture
### Agent Forge Architecture (Brief Description)

Agent Forge is a multi-agent AI startup factory where a CEO Agent orchestrates specialized agents through A2A (Agent-to-Agent) communication. Users interact through a Streamlit Boardroom UI (A2UI), while Context Engineering provides instructions, memory, tools, and guardrails to guide agent behavior.


The CEO Agent coordinates four domain-specific agents:

    🔍 Research Agent – Market research and validation
    📈 Marketing Agent – Go-to-market strategy
    💰 Investor Agent – Funding and investment analysis
    🛡️ Security Agent – Risk and security review

Each agent uses dedicated Skills (Procedural Memory) to perform its specialized tasks. Their outputs are merged into a Consolidated Report, which is then processed by an Evaluation Engine that measures:

    Intent Satisfaction
    Feasibility
    Risk Score
    Confidence Score

Finally, all reports and evaluations are stored in a SQLite Memory Layer, enabling startup history, report retrieval, and historical context for future interactions. The system is powered by Gemini 2.5 Flash for reasoning and content generation.