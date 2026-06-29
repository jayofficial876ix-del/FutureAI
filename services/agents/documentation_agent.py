from .base_agent import BaseAgent


class DocumentationAgent(BaseAgent):

    def system_prompt(self):

        return """
You are the Documentation Agent.

Generate comments and README updates.

Return markdown.
"""