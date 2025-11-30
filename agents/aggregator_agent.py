# agents/aggregator_agent.py

import json
from agents.base_agent import BaseAgent

class AggregatorAgent(BaseAgent):
    """
    Aggregates all agent results into one final score (0–100).
    """

    def aggregate(self, scores: dict):
        trend = scores.get("trend", 0)
        comp = scores.get("competition", 0)
        interest = scores.get("interest", 0)
        value = scores.get("value", 0)
        difficulty = scores.get("difficulty", 0)

        final_score = trend + (20 - comp) + interest + value + difficulty

        prompt = f"""
Summaries of agent scores:
{json.dumps(scores, indent=2)}

Final Score = {final_score}

Write a short 3-line explanation about whether this topic is good.

Return JSON:
{{
  "final_score": {final_score},
  "overall_summary": "<text>"
}}
"""

        llm_result = self.call_llm(prompt)
        return llm_result
