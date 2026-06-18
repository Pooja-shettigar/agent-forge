from utils.skill_loader import load_skill
from utils.gemini_client import ask_gemini

class InvestorAgent:

    def run(self, startup_idea):
        print("💰 Investor Agent Started")
        skill = load_skill(
            "investor_analysis.md"
        )

        prompt = f"""
        {skill}

        Startup Idea:
        {startup_idea}
        """
        print("💰 Investor Agent Finished")
        return ask_gemini(prompt)