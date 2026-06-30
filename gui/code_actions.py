import customtkinter as ctk


class CodeActions(ctk.CTkToplevel):

    def __init__(self, parent, callback):

        super().__init__(parent)

        self.callback = callback

        self.title("💡 Future AI")
        self.geometry("260x360")

        self.transient(parent)
        self.grab_set()

        ctk.CTkLabel(
            self,
            text="AI Code Actions",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(15, 10))

        actions = [
            "Explain Code",
            "Optimize",
            "Fix Bug",
            "Refactor",
            "Generate Tests",
            "Add Comments",
            "Add Logging",
            "Convert to Async"
        ]

        for action in actions:

            ctk.CTkButton(
                self,
                text=action,
                command=lambda a=action: self.choose(a)
            ).pack(
                fill="x",
                padx=15,
                pady=4
            )

    # ----------------------------

    def choose(self, action):

        self.callback(action)

        self.destroy()
