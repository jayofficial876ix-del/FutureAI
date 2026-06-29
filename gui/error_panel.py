import customtkinter as ctk


class ErrorPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text="🐞 Error Assistant",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=12,
            pady=(12, 5)
        )

        self.output = ctk.CTkTextbox(
            self,
            height=180,
            font=("Consolas", 12)
        )

        self.output.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def clear(self):

        self.output.delete(
            "1.0",
            "end"
        )

    def set_error(self, text):

        self.clear()

        self.output.insert(
            "1.0",
            text
        )

    def get_error(self):

        return self.output.get(
            "1.0",
            "end-1c"
        )
