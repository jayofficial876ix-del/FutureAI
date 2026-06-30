from ai.prompts import PROMPTS

from projects.project_manager import load_projects
from services.project_context import ProjectContext


class AIActions:

    def __init__(self, ai):

        self.ai = ai

        self.project_context = ProjectContext()

    # --------------------------------
    # Generic AI Action
    # --------------------------------

    def run_prompt(self, system_prompt, user_prompt):

        conversation = [

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ]

        return self.ai.chat(conversation)

    # --------------------------------
    # Improve Code
    # --------------------------------

    def improve_code(self, code):

        return self.run_prompt(

            (
                "You are Future AI.\n"
                "Improve the user's code.\n"
                "Preserve functionality.\n"
                "Return ONLY the improved code.\n"
                "No markdown."
            ),

            code

        )

    # --------------------------------
    # Inline AI Editing
    # --------------------------------

    def inline_edit(self, code, instruction):

        return self.run_prompt(

            (
                "You are Future AI.\n"
                "Modify ONLY the supplied code.\n"
                "Follow the instruction exactly.\n"
                "Return ONLY the updated code.\n"
                "No markdown.\n"
                "No explanation."
            ),

            f"Instruction:\n{instruction}\n\nCode:\n{code}"

        )

    # --------------------------------
    # Command Palette
    # --------------------------------

    def run_action(self, action, code):

        if action not in PROMPTS:
            return None

        return self.run_prompt(

            PROMPTS[action],

            code

        )

    # --------------------------------
    # Explain Error
    # --------------------------------

    def explain_error(self, error):

        return self.run_prompt(

            (
                "You are Future AI.\n"
                "Explain the traceback.\n"
                "Find the root cause.\n"
                "Suggest the best fix.\n"
                "Include corrected code if appropriate."
            ),

            error

        )

    # --------------------------------
    # Explain Code
    # --------------------------------

    def explain_code(self, code):

        return self.run_prompt(

            (
                "You are Future AI.\n"
                "Explain the supplied code clearly.\n"
                "Describe what it does.\n"
                "Mention any problems or improvements."
            ),

            code

        )

    # --------------------------------
    # Generate Tests
    # --------------------------------

    def generate_tests(self, code):

        return self.run_prompt(

            (
                "You are Future AI.\n"
                "Generate unit tests for the supplied code.\n"
                "Return ONLY the test file."
            ),

            code

        )

    # --------------------------------
    # Add Documentation
    # --------------------------------

    def add_docstrings(self, code):

        return self.run_prompt(

            (
                "You are Future AI.\n"
                "Add professional Python docstrings.\n"
                "Return ONLY the updated code."
            ),

            code

        )

    # --------------------------------
    # Project AI
    # --------------------------------

    def ask_project(self, question):

        projects = load_projects()

        if not projects:

            return "No project has been imported."

        project = projects[0]

        self.project_context.load_project(
            project
        )

        conversation = self.project_context.build_prompt(
            question
        )

        reply = self.ai.chat(
            conversation
        )

        if not reply:

            return "I couldn't answer that."

        return reply
