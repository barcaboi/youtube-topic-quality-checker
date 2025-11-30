# agents/trend_agent.py

from agents.base_agent import BaseAgent
from services.google_trends import GoogleTrendsTool

class TrendAgent(BaseAgent):
    """
    Analyzes trending score (0-20) using Google Trends data.
    """

    def analyze(self, topic: str) -> dict:
        # fetch Google Trends score from custom tool
        trends_score = GoogleTrendsTool().get_interest(topic)

        prompt = f"""
You are a Trend Analysis Agent.

Topic: {topic}
Google Trends score: {trends_score}

Rate the trending potential on a scale of 0 to 20.
Explain reasoning in 2–3 lines.

Return JSON with:
{{
  "trend_score": <number>,
  "explanation": "<text>"
}}
"""

        llm_output = self.call_llm(prompt)
        return {
            "trend_score": trends_score,
            "llm_reasoning": llm_output
        }
