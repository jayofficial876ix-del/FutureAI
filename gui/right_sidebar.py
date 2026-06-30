import customtkinter as ctk

from gui.ai_tasks import AITasks
from gui.source_control import SourceControl


class RightSidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=320,
            corner_radius=0,
            fg_color="#1E1E1E"
        )

        self.pack_propagate(False)

        # --------------------------------
        # Header
        # --------------------------------

        ctk.CTkLabel(
            self,
            text="AI Workspace",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # --------------------------------
        # AI Tasks
        # --------------------------------

        self.tasks = AITasks(self)

        self.tasks.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        # --------------------------------
        # Source Control
        # --------------------------------

        self.git = SourceControl(self)

        self.git.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # --------------------------------
        # Bottom Status
        # --------------------------------

        bottom = ctk.CTkFrame(
            self,
            height=90
        )

        bottom.pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=15
        )

        bottom.pack_propagate(False)

        ctk.CTkLabel(
            bottom,
            text="Future AI",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 2)
        )

        self.status = ctk.CTkLabel(
            bottom,
            text="🟢 Ready",
            text_color="#3CB371"
        )

        self.status.pack(
            anchor="w",
            padx=15
        )

    # --------------------------------

    def set_status(self, text):

        self.status.configure(
            text=text
        )

    # --------------------------------
    # AI Tasks API
    # --------------------------------

    def start_task(self, text):

        return self.tasks.add_task(text)

    def update_task(self, task, progress):

        self.tasks.update_task(
            task,
            progress
        )

    def finish_task(self, task):

        self.tasks.finish_task(task)
