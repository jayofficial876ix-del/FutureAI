from tkinter import messagebox


class GitController:

    def __init__(
        self,
        git_service,
        chat,
        add_ai_bubble
    ):

        self.git = git_service
        self.chat = chat
        self.add_ai_bubble = add_ai_bubble

    # --------------------------------

    def status(self):

        branch = self.git.current_branch()

        changes = self.git.changed_files()

        text = f"Branch: {branch}\n\n"

        if not changes:

            text += "Working tree clean."

        else:

            text += "Changed files:\n\n"

            for status, filename in changes:

                text += f"{status}  {filename}\n"

        self.add_ai_bubble(

            self.chat,

            text

        )

    # --------------------------------

    def commit(self):

        message = messagebox.askstring(

            "Commit",

            "Commit message:"

        )

        if not message:

            return

        result = self.git.commit(message)

        self.add_ai_bubble(

            self.chat,

            result or "Commit finished."

        )

    # --------------------------------

    def push(self):

        result = self.git.push()

        self.add_ai_bubble(

            self.chat,

            result or "Push complete."

        )

    # --------------------------------

    def pull(self):

        result = self.git.pull()

        self.add_ai_bubble(

            self.chat,

            result or "Pull complete."

        )

    # --------------------------------

    def fetch(self):

        result = self.git.fetch()

        self.add_ai_bubble(

            self.chat,

            result or "Fetch complete."

        )

    # --------------------------------

    def branches(self):

        branches = self.git.branches()

        self.add_ai_bubble(

            self.chat,

            "\n".join(branches)

        )
