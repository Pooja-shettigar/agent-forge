from concurrent.futures import ThreadPoolExecutor
import time
from agents.research_agent import ResearchAgent
from agents.marketing_agent import MarketingAgent
from agents.investor_agent import InvestorAgent
from agents.security_agent import SecurityAgent


def safe_run(agent, startup_idea):
    try:
        return agent.run(startup_idea)

    except Exception as e:
        return f"Agent failed: {e}"


class CEOAgent:

    def run(self, startup_idea):
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=4) as executor:

            research_future = executor.submit(
                safe_run,
                ResearchAgent(),
                startup_idea
            )

            marketing_future = executor.submit(
                safe_run,
                MarketingAgent(),
                startup_idea
            )

            investor_future = executor.submit(
                safe_run,
                InvestorAgent(),
                startup_idea
            )

            security_future = executor.submit(
                safe_run,
                SecurityAgent(),
                startup_idea
            )

            research = research_future.result()
            marketing = marketing_future.result()
            investor = investor_future.result()
            security = security_future.result()

            final_report = f"""
# Agent Forge Report

## 🔍 Research Agent
{research}

---

## 📈 Marketing Agent
{marketing}

---

## 💰 Investor Agent
{investor}

---

## 🛡️ Security Agent
{security}
"""
        elapsed = round(time.time() - start_time,2)

        print(
            f"CEO completed in {elapsed}s"
        )
        return {
        "research": research,
        "marketing": marketing,
        "investor": investor,
        "security": security,
        "report": final_report
    }