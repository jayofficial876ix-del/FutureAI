import json
import os

WORKSPACE_FILE = "workspace.json"


class WorkspaceManager:

    def __init__(self):
        self.workspace = self.load()

    def load(self):
        if not os.path.exists(WORKSPACE_FILE):
            return {
                "recent_projects": [],
                "active_project": None
            }

        with open(
            WORKSPACE_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    def save(self):
        with open(
            WORKSPACE_FILE,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                self.workspace,
                f,
                indent=4
            )

    def set_active_project(self, project):
        self.workspace["active_project"] = project

        if project not in self.workspace["recent_projects"]:
            self.workspace["recent_projects"].insert(
                0,
                project
            )

        self.workspace["recent_projects"] = \
            self.workspace["recent_projects"][:10]

        self.save()

    def active_project(self):
        return self.workspace["active_project"]

    def recent_projects(self):
        return self.workspace["recent_projects"]
