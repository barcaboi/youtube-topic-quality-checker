# agents/seo_agent.py
from langchain_openai import ChatOpenAI

class SEOAnalysisAgent:
    def _init_(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")

    def evaluate(self, topic: str, keywords: str):
        prompt = f"""
        Evaluate this YouTube Topic: "{topic}"
        With these keywords: {keywords}

        Give a score from 1-10 for:
        - Searchability
        - Trend potential
        - Engagement
        - Clarity

        Then provide an overall rating and improvement tips.
        """

        response = self.llm.invoke(prompt)
        return response.content.strip()
