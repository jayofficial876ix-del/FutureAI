import customtkinter as ctk


class AgentDashboard(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Future AI Agent")

        self.geometry("520x420")

        self.resizable(False, False)

        self.transient(parent)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="🤖 Future AI Agent",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(20, 15)
        )

        self.rows = {}

        for name in [

            "Planner",

            "Coder",

            "Reviewer",

            "Tester",

            "Documentation"

        ]:

            row = ctk.CTkFrame(self)

            row.pack(
                fill="x",
                padx=20,
                pady=4
            )

            ctk.CTkLabel(
                row,
                text=name,
                width=170,
                anchor="w"
            ).pack(
                side="left",
                padx=10
            )

            status = ctk.CTkLabel(
                row,
                text="⚪ Waiting"
            )

            status.pack(
                side="right",
                padx=10
            )

            self.rows[name] = status

        self.progress = ctk.CTkProgressBar(self)

        self.progress.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.progress.set(0)

    # -----------------------------

    def update_agent(self, name, text):

        self.rows[name].configure(
            text=text
        )

    # -----------------------------

    def set_progress(self, value):

        self.progress.set(value)
