import customtkinter as ctk


class AITasks(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="🤖 AI Tasks",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(15, 10)
        )

        self.tasks = ctk.CTkScrollableFrame(self)

        self.tasks.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # ------------------------------------

    def add_task(self, text):

        card = ctk.CTkFrame(
            self.tasks,
            corner_radius=10
        )

        card.pack(
            fill="x",
            pady=5,
            padx=5
        )

        label = ctk.CTkLabel(
            card,
            text=text,
            anchor="w"
        )

        label.pack(
            fill="x",
            padx=10,
            pady=(8, 4)
        )

        bar = ctk.CTkProgressBar(card)

        bar.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        bar.set(0)

        return {
            "frame": card,
            "label": label,
            "bar": bar
        }

    # ------------------------------------

    def update_task(self, task, progress):

        task["bar"].set(progress)

    # ------------------------------------

    def finish_task(self, task):

        task["bar"].set(1)

        task["label"].configure(
            text="✅ " + task["label"].cget("text")
        )
