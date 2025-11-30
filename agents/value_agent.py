# agents/value_agent.py

from agents.base_agent import BaseAgent

class ValueAgent(BaseAgent):
    """
    Evaluates how valuable, helpful, entertaining, or insightful the topic is.
    """

    def analyze(self, topic: str):
        prompt = f"""
You are a Value Assessment Agent.

Topic: {topic}

Evaluate:
- usefulness
- educational value
- entertainment value
- emotional impact

Give a score from 0–20.

Return JSON:
{{
  "value_score": <number>,
  "explanation": "<text>"
}}
"""
        return self.call_llm(prompt)
