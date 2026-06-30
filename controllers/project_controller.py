from tkinter import messagebox

from projects.project_manager import (
    import_project,
    load_projects
)


class ProjectController:

    def __init__(
        self,
        app,
        chat,
        add_ai_bubble,
        project_context=None
    ):

        self.app = app
        self.chat = chat
        self.add_ai_bubble = add_ai_bubble
        self.project_context = project_context

    # --------------------------------

    def import_project(self):

        project = import_project()

        if not project:
            return

        if self.project_context:
            self.project_context.load_project(
                project
            )

        self.add_ai_bubble(

            self.chat,

            (
                f"✅ Imported project:\n\n"
                f"{project['name']}\n\n"
                f"Files: {len(project['files'])}"
            )

        )

    # --------------------------------

    def list_projects(self):

        projects = load_projects()

        if not projects:

            self.add_ai_bubble(

                self.chat,

                "No projects have been imported."

            )

            return

        text = "Projects\n\n"

        for project in projects:

            text += (

                f"• {project['name']}\n"

            )

        self.add_ai_bubble(

            self.chat,

            text

        )

    # --------------------------------

    def current_project(self):

        projects = load_projects()

        if not projects:

            self.add_ai_bubble(

                self.chat,

                "No active project."

            )

            return

        project = projects[0]

        text = (

            f"Current Project\n\n"

            f"Name: {project['name']}\n"

            f"Files: {len(project['files'])}"
        )

        self.add_ai_bubble(

            self.chat,

            text

        )

    # --------------------------------

    def reload_index(self):

        if not self.project_context:

            return

        projects = load_projects()

        if not projects:

            return

        self.project_context.load_project(

            projects[0]

        )

        self.add_ai_bubble(

            self.chat,

            "✅ Project index rebuilt."

        )
