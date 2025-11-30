# agents/audience_agent.py

from agents.base_agent import BaseAgent

class AudienceAgent(BaseAgent):
    """
    Predicts how likely viewers will click on the topic.
    """

    def analyze(self, topic: str) -> dict:
        prompt = f"""
You are an Audience Psychology Agent.

Topic: {topic}

Predict viewer interest (0 to 20).
Consider:
- emotional triggers
- novelty
- human curiosity
- entertainment or value factor

Return JSON:
{{
  "interest_score": <number>,
  "explanation": "<text>"
}}
"""

        return self.call_llm(prompt)
