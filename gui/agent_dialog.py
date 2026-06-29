import customtkinter as ctk


class AgentDialog(ctk.CTkToplevel):

    def __init__(self, parent, callback):

        super().__init__(parent)

        self.callback = callback

        self.title("🤖 AI Agent")
        self.geometry("550x320")

        self.transient(parent)
        self.grab_set()

        ctk.CTkLabel(
            self,
            text="AI Agent Task",
            font=("Segoe UI", 22, "bold")
        ).pack(pady=(15, 10))

        ctk.CTkLabel(
            self,
            text="Describe what you want Future AI to do:"
        ).pack(anchor="w", padx=20)

        self.text = ctk.CTkTextbox(
            self,
            height=120
        )

        self.text.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.text.insert(
            "1.0",
            "Example:\n\nAdd logging to every route."
        )

        ctk.CTkButton(
            self,
            text="🚀 Run Agent",
            height=40,
            command=self.run
        ).pack(
            fill="x",
            padx=20,
            pady=15
        )

    def run(self):

        task = self.text.get(
            "1.0",
            "end-1c"
        ).strip()

        if task:
            self.callback(task)

        self.destroy()
