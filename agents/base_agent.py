# agents/base_agent.py

import openai
from services.observability import instrument

class BaseAgent:
    """
    Base class for all agents.
    Provides LLM call + observability wrapper.
    """

    def _init_(self, model="gpt-4o-mini"):
        self.model = model

    @instrument  # logs time, traces, metrics
    def call_llm(self, prompt: str) -> str:
        """
        Calls the LLM with a prompt.
        Returns the model output as text.
        """
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"LLM Error: {e}"
