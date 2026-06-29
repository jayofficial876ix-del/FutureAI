import customtkinter as ctk


class SidebarStack(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pages = {}

    def add(self, name, widget):

        self.pages[name] = widget

        widget.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        widget.lower()

    def show(self, name):

        if name not in self.pages:
            return

        self.pages[name].lift()
