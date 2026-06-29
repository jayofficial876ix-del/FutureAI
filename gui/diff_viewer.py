import customtkinter as ctk


class DiffViewer(ctk.CTkToplevel):

    def __init__(self, parent, diff, apply_callback):

        super().__init__(parent)

        self.title("AI Code Review")
        self.geometry("900x650")

        self.apply_callback = apply_callback

        ctk.CTkLabel(
            self,
            text="🤖 AI Suggested Changes",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=10
        )

        self.editor = ctk.CTkTextbox(
            self,
            font=("Consolas", 13)
        )

        self.editor.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.editor.insert(
            "1.0",
            diff
        )

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkButton(
            buttons,
            text="✅ Apply",
            command=self.apply
        ).pack(
            side="right",
            padx=5
        )

        ctk.CTkButton(
            buttons,
            text="Cancel",
            command=self.destroy
        ).pack(
            side="right"
        )

    def apply(self):

        self.apply_callback()

        self.destroy()
