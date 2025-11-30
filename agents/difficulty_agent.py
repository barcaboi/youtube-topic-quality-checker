# agents/difficulty_agent.py

from agents.base_agent import BaseAgent

class DifficultyAgent(BaseAgent):
    """
    Estimates how hard it is to create this video.
    Lower difficulty = higher score.
    """

    def analyze(self, topic: str):
        prompt = f"""
You are a Difficulty Analysis Agent.

Topic: {topic}

Consider:
- research effort
- recording complexity
- editing difficulty
- resources needed

Give a score from 0–20.

Return JSON:
{{
  "difficulty_score": <number>,
  "explanation": "<text>"
}}
"""
        return self.call_llm(prompt)
