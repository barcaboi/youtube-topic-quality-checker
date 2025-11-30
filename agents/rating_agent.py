# agents/rating_agent.py
from langchain_openai import ChatOpenAI

class RatingAgent:
    def _init_(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")

    def combine_scores(self, topic: str, seo_report: str):
        prompt = f"""
        Generate the final 'Topic Quality Score' for YouTube content.

        Topic: {topic}
        SEO Analysis Summary:
        {seo_report}

        Return:
        - A final numeric score (1-100)
        - Color label (Red = Poor, Yellow = Average, Green = Good)
        - Summary in 3 lines
        """

        response = self.llm.invoke(prompt)
        return response.content.strip()
