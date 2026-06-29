import subprocess
import os


class GitService:

    def __init__(self, project=None):

        self.project = project or os.getcwd()

    # --------------------------------

    def run(self, *args):

        try:

            result = subprocess.run(

                ["git", *args],

                cwd=self.project,

                capture_output=True,

                text=True

            )

            return result.stdout.strip()

        except Exception:

            return ""

    # --------------------------------

    def current_branch(self):

        return self.run(
            "branch",
            "--show-current"
        )

    # --------------------------------

    def changed_files(self):

        output = self.run(
            "status",
            "--short"
        )

        changes = []

        for line in output.splitlines():

            if not line.strip():
                continue

            status = line[:2].strip()

            filename = line[3:].strip()

            changes.append(

                (status, filename)

            )

        return changes

    # --------------------------------

    def commit(self, message):

        if not message.strip():
            return

        self.run(
            "add",
            "."
        )

        return self.run(
            "commit",
            "-m",
            message
        )

    # --------------------------------

    def push(self):

        return self.run(
            "push"
        )

    # --------------------------------

    def pull(self):

        return self.run(
            "pull"
        )

    # --------------------------------

    def fetch(self):

        return self.run(
            "fetch"
        )

    # --------------------------------

    def branches(self):

        return self.run(
            "branch"
        ).splitlines()
