from ai.ai_engine import AIEngine

from .planner_agent import PlannerAgent
from .coder_agent import CoderAgent
from .reviewer_agent import ReviewerAgent
from .test_agent import TestAgent
from .documentation_agent import DocumentationAgent


class AgentManager:

    def __init__(self):

        ai = AIEngine()

        self.planner = PlannerAgent(ai)
        self.coder = CoderAgent(ai)
        self.reviewer = ReviewerAgent(ai)
        self.tester = TestAgent(ai)
        self.docs = DocumentationAgent(ai)

    def run(self, request, context=""):

        plan = self.planner.execute(
            request,
            context
        )

        code = self.coder.execute(
            request,
            context
        )

        review = self.reviewer.execute(
            code,
            context
        )

        tests = self.tester.execute(
            code,
            context
        )

        docs = self.docs.execute(
            code,
            context
        )

        return {

            "plan": plan,

            "code": code,

            "review": review,

            "tests": tests,

            "docs": docs

        }