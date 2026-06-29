import customtkinter as ctk


class TaskTimeline(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.items = []

    def add_step(self, text):

        label = ctk.CTkLabel(
            self,
            text="⬜ " + text,
            anchor="w"
        )

        label.pack(
            fill="x",
            padx=8,
            pady=2
        )

        self.items.append(label)

        return len(self.items) - 1

    def running(self, index):

        self.items[index].configure(
            text="⏳ " + self.items[index].cget("text")[2:]
        )

    def finish(self, index):

        self.items[index].configure(
            text="✔ " + self.items[index].cget("text")[2:]
        )
