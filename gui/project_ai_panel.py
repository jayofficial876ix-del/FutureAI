import customtkinter as ctk


class ProjectAIPanel:

    def __init__(self, parent, ask_callback):

        self.ask_callback = ask_callback

        self.frame = ctk.CTkFrame(
            parent,
            width=320
        )

        self.frame.pack(
            side="right",
            fill="y"
        )

        ctk.CTkLabel(
            self.frame,
            text="🤖 Project AI",
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(15, 10)
        )

        self.history = ctk.CTkTextbox(
            self.frame,
            width=320
        )

        self.history.pack(
            fill="both",
            expand=True,
            padx=10
        )

        self.question = ctk.CTkEntry(
            self.frame,
            placeholder_text="Ask about your project..."
        )

        self.question.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.question.bind(
            "<Return>",
            lambda e: self.ask()
        )

    def ask(self):

        text = self.question.get().strip()

        if not text:
            return

        self.history.insert(
            "end",
            f"\n🧑 {text}\n"
        )

        reply = self.ask_callback(text)

        if reply:

            self.history.insert(
                "end",
                f"\n🤖 {reply}\n"
            )

        self.history.see("end")

        self.question.delete(0, "end")
