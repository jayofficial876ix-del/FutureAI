import customtkinter as ctk

from gui.ai_tasks import AITasks
from gui.task_timeline import TaskTimeline


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
        # AI Tools
        # --------------------------------

        self.section(
            "🤖 AI Tools",
            [
                "AI Agent",
                "Command Palette",
                "Explain Error",
                "Improve Code"
            ]
        )

        # --------------------------------
        # Project
        # --------------------------------

        self.section(
            "📁 Project",
            [
                "Explorer",
                "Quick Open",
                "Global Search"
            ]
        )

        # --------------------------------
        # Memory
        # --------------------------------

        self.section(
            "🧠 Memory",
            [
                "Recent Chats",
                "Recent Files",
                "Bookmarks"
            ]
        )

        # --------------------------------
        # AI Timeline
        # --------------------------------

        self.timeline = TaskTimeline(self)

        self.timeline.pack(
            fill="x",
            padx=15,
            pady=(10, 5)
        )

        # --------------------------------
        # AI Tasks
        # --------------------------------

        self.tasks = AITasks(self)

        self.tasks.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(5, 10)
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
    # Section Builder
    # --------------------------------

    def section(self, title, items):

        frame = ctk.CTkFrame(self)

        frame.pack(
            fill="x",
            padx=15,
            pady=8
        )

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=12,
            pady=(10, 5)
        )

        for item in items:

            ctk.CTkButton(
                frame,
                text=item,
                anchor="w",
                fg_color="transparent",
                hover_color="#2A2A2A"
            ).pack(
                fill="x",
                padx=8,
                pady=2
            )

    # --------------------------------
    # Status
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

    # --------------------------------
    # Timeline API
    # --------------------------------

    def add_timeline_step(self, text):

        return self.timeline.add_step(text)

    def start_timeline_step(self, step):

        self.timeline.running(step)

    def finish_timeline_step(self, step):

        self.timeline.finish(step)
