class Evaluator:

    def evaluate(
        self,
        startup_idea,
        report
    ):

        report_lower = report.lower()

        intent_satisfaction = 5
        feasibility = 5
        risk_score = 5
        confidence = 5

        # Intent Satisfaction

        if startup_idea.lower()[:10] in report_lower:
            intent_satisfaction += 2

        # Feasibility

        if "revenue" in report_lower:
            feasibility += 1

        if "market" in report_lower:
            feasibility += 1

        if "customer" in report_lower:
            feasibility += 1

        # Risk

        if "risk" in report_lower:
            risk_score += 2

        if "compliance" in report_lower:
            risk_score += 1

        # Confidence

        sections = 0

        keywords = [
            "market",
            "revenue",
            "customer",
            "pricing",
            "risk"
        ]

        for keyword in keywords:

            if keyword in report_lower:
                sections += 1

        confidence += min(sections, 5)

        return {
            "intent_satisfaction":
                min(intent_satisfaction, 10),

            "feasibility":
                min(feasibility, 10),

            "risk_score":
                min(risk_score, 10),

            "confidence":
                min(confidence, 10)
        }