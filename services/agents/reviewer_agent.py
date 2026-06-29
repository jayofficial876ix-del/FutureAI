
from .base_agent import BaseAgent


class ReviewerAgent(BaseAgent):

	def system_prompt(self):

		return """
You are the Code Review Agent.

Review code for:

- bugs
- security
- performance
- readability

Return recommendations only.
"""
