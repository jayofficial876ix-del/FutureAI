from services.agent_planner import AgentPlanner
from services.agent_executor import AgentExecutor
from services.project_editor import ProjectEditor
from services.project_context import ProjectContext
from services.agent_brain import AgentBrain
from services.local_coder import LocalCoder

from projects.project_manager import load_projects


class AIAgent:

    def __init__(self, ai):

        self.ai = ai

        self.planner = AgentPlanner(ai)
        self.executor = AgentExecutor(ai, self.planner)

        self.editor = ProjectEditor()
        self.context = ProjectContext()

        self.brain = AgentBrain()
        self.local = LocalCoder()

    # --------------------------------

    def run(self, request):

        self.brain.remember(request)

        projects = load_projects()

        if not projects:
            return None

        project = projects[0]

        self.context.load_project(project)

        files = self.executor.execute(request)

        if not files:
            return None

        results = []

        for filename in files:

            full_path = None

            for project_file in project["files"]:

                if project_file.endswith(filename):

                    full_path = project_file
                    break

            if full_path is None:
                continue

            code = self.editor.read(full_path)

            conversation = [

                {
                    "role": "system",
                    "content":
                    (
                        "You are an expert software engineer.\n"
                        "Modify ONLY this file.\n"
                        "Return ONLY the updated code."
                    )
                },

                {
                    "role": "user",
                    "content":
                        f"Task:\n{request}\n\n"
                        f"Filename:\n{filename}\n\n"
                        f"Code:\n\n{code}"
                }

            ]

            new_code = self.ai.chat(conversation)

            # --------------------------------
            # Local AI Fallback
            # --------------------------------

            if new_code is None:

                print("Using LocalCoder...")

                new_code = self.local.generate(
                    request,
                    filename,
                    code
                )

            results.append({

                "filename": full_path,
                "old": code,
                "new": new_code

            })

        return results