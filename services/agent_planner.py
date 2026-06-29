from projects.project_manager import load_projects


class AgentPlanner:

    def __init__(self, ai):
        self.ai = ai

    def plan(self, request):
        projects = load_projects()

        if not projects:
            return None

        project = projects[0]
        file_list = "\n".join(project["files"])

        conversation = [
            {
                "role": "system",
                "content":
                (
                    "You are an expert software architect.\n"
                    "Your job is to decide which project files "
                    "must be edited to complete the user's request.\n\n"

                    "Return ONLY a numbered list.\n\n"

                    "Example:\n"
                    "1. app.py\n"
                    "2. database.py\n"
                    "3. auth/login.py"
                )
            },
            {
                "role": "system",
                "content":
                    "Project Files:\n\n" + file_list
            },
            {
                "role": "user",
                "content": request
            }
        ]

        return self.ai.chat(conversation)
