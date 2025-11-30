
# agents/competition_agent.py

from agents.base_agent import BaseAgent
from services.youtube_api import YouTubeTool

class CompetitionAgent(BaseAgent):
    """
    Measures how hard it is to rank for a topic.
    """

    def analyze(self, topic: str) -> dict:
        videos = YouTubeTool().search_videos(topic)

        prompt = f"""
You are a Competition Analysis Agent.

Topic: {topic}
Top video results: {videos}

Rate competition difficulty on a scale of 0 to 20.
Higher difficulty = LOWER score.

Return JSON:
{{
  "competition_score": <number>,
  "explanation": "<text>"
}}
"""

        llm_output = self.call_llm(prompt)
        return {
            "videos": videos,
            "analysis": llm_output
        }
