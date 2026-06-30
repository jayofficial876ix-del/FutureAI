from services.local_planner import LocalPlanner

from projects.project_manager import load_projects


class AgentPlanner:

    def __init__(self, ai):

        self.ai = ai
        self.local = LocalPlanner()

    def plan(self, request):

        print("\n============================================================")
        print("FUTURE AI AGENT")
        print("============================================================")
        print("Request:")
        print(request)
        print("============================================================")

        projects = load_projects()

        if not projects:

            print("No projects loaded.")

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

        # -----------------------------
        # Try OpenAI first
        # -----------------------------

        plan = self.ai.chat(conversation)

        if plan:

            print("\nPlanner returned:\n")
            print(plan)

            return plan

        # -----------------------------
        # Local Planner
        # -----------------------------

        print("\nOpenAI unavailable.")
        print("Switching to Local Planner...\n")

        files = self.local.plan(
            request,
            project
        )

        if not files:

            print("Local Planner found no matching files.")

            return None

        result = ""

        for i, file in enumerate(files, start=1):

            result += f"{i}. {file}\n"

        print("Local Planner returned:\n")
        print(result)

        return result
