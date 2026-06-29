import os


class WorkspaceCache:

    def __init__(self):
        self.files = []
        self.project = None

    # -----------------------------

    def build(self, project):
        self.project = project
        self.files.clear()
        if not project:
            return
        for root, _, filenames in os.walk(project):
            for filename in filenames:
                self.files.append(
                    os.path.join(root, filename)
                )

    # -----------------------------

    def search(self, text):
        text = text.lower()
        return [
            f
            for f in self.files
            if text in os.path.basename(f).lower()
        ]

    # -----------------------------

    def all_files(self):
        return list(self.files)


workspace_cache = WorkspaceCache()
