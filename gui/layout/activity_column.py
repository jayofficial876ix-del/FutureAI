import customtkinter as ctk

from gui.activity_bar import ActivityBar


class ActivityColumn(ctk.CTkFrame):

    def __init__(self, parent, sidebar_stack):

        super().__init__(
            parent,
            width=60,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.activity = ActivityBar(self)

        self.activity.pack(
            fill="both",
            expand=True
        )

        self.activity.set_callback(
            sidebar_stack.show
        )

        self.activity.select("chat")
