from evaluations.evaluator import Evaluator


def test_evaluator_returns_scores():

    evaluator = Evaluator()

    result = evaluator.evaluate(
        "AI SaaS for Dentists",
        "Sample Report"
    )

    assert "intent_satisfaction" in result
    assert "feasibility" in result
    assert "risk_score" in result
    assert "confidence" in result