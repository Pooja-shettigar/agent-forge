from utils.skill_loader import load_skill
from utils.gemini_client import ask_gemini

class ResearchAgent:

    def run(self, startup_idea):
        print("🔍 Research Agent Started")
        skill = load_skill(
            "market_research.md"
        )

        prompt = f"""
        {skill}

        Startup Idea:
        {startup_idea}
        """
        print("🔍 Research Agent Finished")
        return ask_gemini(prompt)