import customtkinter as ctk

from history.chat_history import load_chats
from projects.project_manager import load_projects

from gui.file_tree import FileTree


class ExplorerPanel:

    def __init__(
        self,
        parent,
        open_chat,
        new_chat,
        delete_chat,
        open_file
    ):

        self.parent = parent
        self.open_chat = open_chat
        self.new_chat = new_chat
        self.delete_chat = delete_chat
        self.open_file = open_file

        self.frame = ctk.CTkFrame(
            parent,
            width=300,
            corner_radius=0
        )

        self.frame.pack(
            side="left",
            fill="y"
        )

        self.frame.pack_propagate(False)

        self.refresh()

    def refresh(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        # -------------------------
        # Title
        # -------------------------

        ctk.CTkLabel(
            self.frame,
            text="🤖 Future AI",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(20, 10)
        )

        ctk.CTkButton(
            self.frame,
            text="+ New Chat",
            command=self.new_chat
        ).pack(
            fill="x",
            padx=12,
            pady=(0, 15)
        )

        # -------------------------
        # Chats
        # -------------------------

        ctk.CTkLabel(
            self.frame,
            text="💬 Chats",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=12
        )

        chats = load_chats()

        for i, chat in enumerate(chats):

            row = ctk.CTkFrame(
                self.frame,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=8,
                pady=2
            )

            title = chat["title"]

            if len(title) > 22:
                title = title[:22] + "..."

            ctk.CTkButton(
                row,
                text="💬 " + title,
                anchor="w",
                command=lambda i=i: self.open_chat(i)
            ).pack(
                side="left",
                fill="x",
                expand=True
            )

            ctk.CTkButton(
                row,
                text="🗑",
                width=34,
                fg_color="#8B1E1E",
                hover_color="#B22222",
                command=lambda i=i: self.delete_chat(i)
            ).pack(
                side="right",
                padx=(4, 0)
            )

        # -------------------------
        # Projects
        # -------------------------

        ctk.CTkLabel(
            self.frame,
            text="📁 Projects",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=12,
            pady=(20, 8)
        )

        projects = load_projects()

        if not projects:

            ctk.CTkLabel(
                self.frame,
                text="No projects imported",
                text_color="gray"
            ).pack(
                anchor="w",
                padx=15
            )

            return

        self.tree = FileTree(
            self.frame,
            self.open_file
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 8)
        )

        # Show the first project for now
        self.tree.load_project(
            projects[0]
        )
