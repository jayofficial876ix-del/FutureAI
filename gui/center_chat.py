import customtkinter as ctk

from gui.welcome_dashboard import WelcomeDashboard


class CenterChat(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller

        # --------------------------------
        # Welcome Dashboard
        # --------------------------------

        self.dashboard = WelcomeDashboard(
            self,
            controller
        )

        self.dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(20, 0)
        )

        # --------------------------------
        # Chat Area
        # --------------------------------

        self.chat = ctk.CTkScrollableFrame(self)

        # Tell controller where messages go
        controller.chat = self.chat

        # --------------------------------
        # Bottom Input
        # --------------------------------

        bottom = ctk.CTkFrame(self)

        bottom.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=20
        )

        self.entry = ctk.CTkEntry(
            bottom,
            placeholder_text="Message Future AI..."
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 5),
            pady=10
        )

        send = ctk.CTkButton(
            bottom,
            text="➤",
            width=60,
            command=self.send
        )

        send.pack(
            side="right",
            padx=(5, 10),
            pady=10
        )

        self.entry.bind(
            "<Return>",
            lambda e: self.send()
        )

    # --------------------------------
    # Dashboard
    # --------------------------------

    def show_dashboard(self):

        self.chat.pack_forget()

        self.dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(20, 0)
        )

    # --------------------------------
    # Chat
    # --------------------------------

    def show_chat(self):

        self.dashboard.pack_forget()

        self.chat.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 10)
        )

    # --------------------------------
    # Send Message
    # --------------------------------

    def send(self):

        if not self.entry.get().strip():
            return

        self.show_chat()

        self.controller.send(
            self.entry
        )
