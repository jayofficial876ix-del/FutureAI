import customtkinter as ctk


class PlaceholderPage(ctk.CTkFrame):

    def __init__(self, parent, title):

        super().__init__(parent)

        ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 28, "bold")
        ).pack(
            pady=50
        )

        ctk.CTkLabel(
            self,
            text="Coming Soon",
            text_color="gray"
        ).pack()
