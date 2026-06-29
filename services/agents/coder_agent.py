from .base_agent import BaseAgent


class CoderAgent(BaseAgent):

    def system_prompt(self):

        return """
You are the Coding Agent.

Write production-quality code.

Modify existing code when appropriate.

Return complete code.
"""
