from utils.skill_loader import load_skill
from utils.gemini_client import ask_gemini

class SecurityAgent:

    def run(self, startup_idea):
        print("🛡️ Security Agent Started")
        skill = load_skill(
            "security_review.md"
        )

        prompt = f"""
        {skill}

        Startup Idea:
        {startup_idea}
        """
        print("🛡️ Security Agent Finished")
        return ask_gemini(prompt)