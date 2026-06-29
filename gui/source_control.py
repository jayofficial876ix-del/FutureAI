import customtkinter as ctk

from services.git_service import GitService


class SourceControl(ctk.CTkFrame):

    def __init__(self, parent, project_path=None):

        super().__init__(parent)

        self.git = GitService(project_path)

        # --------------------------------
        # Header
        # --------------------------------

        ctk.CTkLabel(
            self,
            text="🌿 Source Control",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # --------------------------------
        # Branch
        # --------------------------------

        branch = ctk.CTkFrame(self)
        branch.pack(fill="x", padx=15, pady=5)

        ctk.CTkLabel(
            branch,
            text="Current Branch",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=12, pady=(10, 4))

        self.branch_name = ctk.CTkLabel(branch, text="")
        self.branch_name.pack(anchor="w", padx=12, pady=(0, 10))

        # --------------------------------
        # Changed Files
        # --------------------------------

        changes = ctk.CTkFrame(self)
        changes.pack(fill="both", expand=True, padx=15, pady=10)

        ctk.CTkLabel(
            changes,
            text="Changes",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", padx=12, pady=(10, 8))

        self.change_list = ctk.CTkScrollableFrame(changes)

        self.change_list.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # --------------------------------
        # Commit Message
        # --------------------------------

        commit = ctk.CTkFrame(self)

        commit.pack(
            fill="x",
            padx=15,
            pady=10
        )

        ctk.CTkLabel(
            commit,
            text="Commit Message",
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w", padx=12, pady=(10, 5))

        self.message = ctk.CTkTextbox(
            commit,
            height=80
        )

        self.message.pack(
            fill="x",
            padx=12,
            pady=(0, 10)
        )

        ctk.CTkButton(
            commit,
            text="Commit",
            command=self.commit
        ).pack(
            fill="x",
            padx=12,
            pady=(0, 12)
        )

        # --------------------------------
        # Git Buttons
        # --------------------------------

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        ctk.CTkButton(
            buttons,
            text="↑ Push",
            command=self.push
        ).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(
            buttons,
            text="↓ Pull",
            command=self.pull
        ).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(
            buttons,
            text="⇄ Refresh",
            command=self.refresh
        ).pack(fill="x", padx=10, pady=2)

        self.refresh()

    # --------------------------------

    def refresh(self):

        self.branch_name.configure(
            text=f"🌿 {self.git.current_branch()}"
        )

        for widget in self.change_list.winfo_children():
            widget.destroy()

        for status, filename in self.git.changed_files():

            ctk.CTkLabel(
                self.change_list,
                text=f"{status}   {filename}",
                anchor="w"
            ).pack(
                fill="x",
                padx=5,
                pady=2
            )

    # --------------------------------

    def commit(self):

        message = self.message.get(
            "1.0",
            "end-1c"
        )

        self.git.commit(message)

        self.message.delete(
            "1.0",
            "end"
        )

        self.refresh()

    # --------------------------------

    def push(self):

        self.git.push()

        self.refresh()

    # --------------------------------

    def pull(self):

        self.git.pull()

        self.refresh()
