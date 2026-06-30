import customtkinter as ctk

from services.git_service import GitService


class SourceControl(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.git = GitService()

        # -------------------------

        ctk.CTkLabel(
            self,
            text="🌿 Source Control",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        self.branch = ctk.CTkLabel(
            self,
            text="Branch: ..."
        )

        self.branch.pack(
            anchor="w",
            padx=10
        )

        self.files = ctk.CTkScrollableFrame(
            self,
            height=180
        )

        self.files.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        ctk.CTkButton(
            buttons,
            text="Refresh",
            command=self.refresh
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            buttons,
            text="Commit",
            command=self.commit
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            buttons,
            text="Push",
            command=self.push
        ).pack(
            side="left",
            padx=5
        )

        self.refresh()

    # -------------------------

    def refresh(self):

        self.branch.configure(
            text="Branch: " + self.git.current_branch()
        )

        for widget in self.files.winfo_children():
            widget.destroy()

        changes = self.git.changed_files()

        if not changes:

            ctk.CTkLabel(
                self.files,
                text="✔ Working tree clean"
            ).pack(
                anchor="w",
                padx=5,
                pady=5
            )

            return

        for status, filename in changes:

            ctk.CTkLabel(
                self.files,
                text=f"{status}  {filename}",
                anchor="w"
            ).pack(
                fill="x",
                padx=5,
                pady=2
            )

    # -------------------------

    def commit(self):

        self.git.commit("Future AI Commit")

        self.refresh()

    # -------------------------

    def push(self):

        self.git.push()

        self.refresh()
