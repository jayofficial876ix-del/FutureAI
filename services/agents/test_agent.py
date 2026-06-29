from .base_agent import BaseAgent


class TestAgent(BaseAgent):

    def system_prompt(self):

        return """
You are the Testing Agent.

Generate unit tests.

Cover edge cases.

Return only the tests.
"""
