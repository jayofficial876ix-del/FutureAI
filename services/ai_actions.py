from ai.prompts import PROMPTS
from projects.project_manager import load_projects
from services.project_context import ProjectContext


class AIActions:

    def __init__(self, ai):
        self.ai = ai
        self.project_context = ProjectContext()

    # -----------------------------
    # Improve Code
    # -----------------------------

    def improve_code(self, code):

        conversation = [

            {
                "role": "system",
                "content":
                    (
                        "You are an expert software engineer.\n"
                        "Improve the user's code while preserving functionality.\n"
                        "Return only the improved code."
                    )
            },

            {
                "role": "user",
                "content": code
            }

        ]

        return self.ai.chat(conversation)

    # -----------------------------
    # Inline AI Editing
    # -----------------------------

    def inline_edit(self, code, instruction):

        conversation = [

            {
                "role": "system",
                "content":
                    (
                        "You are an expert programmer.\n"
                        "Modify ONLY the supplied code.\n"
                        "Follow the user's instruction exactly.\n"
                        "Return ONLY the modified code.\n"
                        "Do not explain your changes."
                    )
            },

            {
                "role": "user",
                "content":
                    f"Instruction:\n{instruction}\n\nCode:\n{code}"
            }

        ]

        return self.ai.chat(conversation)

    # -----------------------------
    # Command Palette Actions
    # -----------------------------

    def run_action(self, action, code):

        if action not in PROMPTS:
            return None

        conversation = [

            {
                "role": "system",
                "content": PROMPTS[action]
            },

            {
                "role": "user",
                "content": code
            }

        ]

        return self.ai.chat(conversation)

    # -----------------------------
    # Error Assistant
    # -----------------------------

    def explain_error(self, error):

        conversation = [

            {
                "role": "system",
                "content":
                    (
                        "You are an expert Python debugging assistant.\n"
                        "Explain the traceback.\n"
                        "Identify the root cause.\n"
                        "Suggest the most likely fix.\n"
                        "If possible include corrected code."
                    )
            },

            {
                "role": "user",
                "content": error
            }

        ]

        return self.ai.chat(conversation)

    # -----------------------------
    # Project AI
    # -----------------------------

    def ask_project(self, question):

        projects = load_projects()

        if not projects:
            return "No project has been imported."

        project = projects[0]

        self.project_context.load_project(project)

        conversation = self.project_context.build_prompt(
            question
        )

        reply = self.ai.chat(conversation)

        if not reply:
            return "I couldn't answer that."

        return reply
