from utils.skill_loader import load_skill
from utils.gemini_client import ask_gemini

class MarketingAgent:

    def run(self, startup_idea):
        print("📈 Marketing Agent Started")
        skill = load_skill(
            "gtm_strategy.md"
        )

        prompt = f"""
        {skill}

        Startup Idea:
        {startup_idea}
        """
        print("📈 Marketing Agent Finished")
        return ask_gemini(prompt)