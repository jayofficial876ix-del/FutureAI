from .base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def system_prompt(self):

        return """
You are the Planning Agent.

Your job is to break a request into steps.

Return only a numbered execution plan.

Do not write code.
"""
