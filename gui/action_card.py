import customtkinter as ctk


class ActionCard(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        emoji,
        title,
        description,
        command=None
    ):

        super().__init__(
            parent,
            fg_color="#252526",
            corner_radius=12,
            cursor="hand2"
        )

        self.command = command

        self.bind("<Button-1>", self.click)

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            header,
            text=f"{emoji} {title}",
            font=("Segoe UI", 17, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            self,
            text=description,
            justify="left",
            text_color="#B0B0B0",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 15)
        )

    def click(self, event=None):

        if self.command:
            self.command()
