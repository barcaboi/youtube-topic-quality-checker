# agents/keyword_agent.py
from langchain_openai import ChatOpenAI

class KeywordAgent:
    def _init_(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")

    def extract_keywords(self, topic: str):
        prompt = f"""
        Extract 5-8 important keywords from the YouTube topic below.
        Topic: "{topic}"
        Return keywords as a simple comma-separated list.
        """

        response = self.llm.invoke(prompt)
        return response.content.strip()
