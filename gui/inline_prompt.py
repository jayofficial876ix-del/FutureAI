import customtkinter as ctk


class InlinePrompt(ctk.CTkToplevel):

    def __init__(self, parent, callback):

        super().__init__(parent)

        self.callback = callback

        self.title("✨ Edit with AI")

        self.geometry("520x170")

        self.transient(parent)
        self.grab_set()

        self.resizable(False, False)

        ctk.CTkLabel(
            self,
            text="✨ Edit Selection with AI",
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(15, 8)
        )

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Describe how AI should modify the selected code..."
        )

        self.entry.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.entry.focus()

        self.entry.bind(
            "<Return>",
            lambda e: self.submit()
        )

        ctk.CTkButton(
            self,
            text="Generate",
            command=self.submit,
            height=36
        ).pack(
            pady=(0, 15)
        )

    # --------------------------------

    def submit(self):

        prompt = self.entry.get().strip()

        if prompt:

            self.callback(prompt)

        self.destroy()
