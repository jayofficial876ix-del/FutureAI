import customtkinter as ctk


class TaskTimeline(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.items = {}

    # -------------------------

    def add_step(self, text):

        row = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            pady=2
        )

        icon = ctk.CTkLabel(
            row,
            text="⬜",
            width=30
        )

        icon.pack(
            side="left"
        )

        label = ctk.CTkLabel(
            row,
            text=text,
            anchor="w"
        )

        label.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.items[text] = (icon, label)

        return text

    # -------------------------

    def running(self, step):

        icon, _ = self.items[step]

        icon.configure(
            text="⏳"
        )

        self.update()

    # -------------------------

    def finish(self, step):

        icon, _ = self.items[step]

        icon.configure(
            text="✔"
        )

        self.update()

    # -------------------------

    def error(self, step):

        icon, _ = self.items[step]

        icon.configure(
            text="❌"
        )

        self.update()

    # -------------------------

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.items.clear()
