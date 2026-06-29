import customtkinter as ctk

from history.chat_history import load_chats


class LeftSidebar(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(
            parent,
            width=260,
            corner_radius=0
        )

        self.controller = controller

        self.pack_propagate(False)

        # --------------------------------
        # Logo
        # --------------------------------

        ctk.CTkLabel(
            self,
            text="✨ Future AI",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        # --------------------------------
        # New Chat
        # --------------------------------

        ctk.CTkButton(
            self,
            text="+ New Chat",
            height=42,
            command=self.new_chat
        ).pack(
            fill="x",
            padx=15,
            pady=(0, 20)
        )

        # --------------------------------
        # Navigation
        # --------------------------------

        nav = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav.pack(
            fill="x",
            padx=10
        )

        for item in (
            "🏠 Home",
            "🔍 Discover",
            "🤖 Agents",
            "📁 Projects",
            "🧠 Knowledge",
            "🛠 Tools"
        ):

            ctk.CTkButton(
                nav,
                text=item,
                anchor="w",
                fg_color="transparent"
            ).pack(
                fill="x",
                pady=2
            )

        # --------------------------------
        # Chats
        # --------------------------------

        ctk.CTkLabel(
            self,
            text="Chats",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 8)
        )

        self.chat_frame = ctk.CTkScrollableFrame(self)

        self.chat_frame.pack(
            fill="both",
            expand=True,
            padx=10
        )

        self.refresh()

    # --------------------------------

    def refresh(self):

        for widget in self.chat_frame.winfo_children():
            widget.destroy()

        chats = load_chats()

        for index, chat in enumerate(chats):

            ctk.CTkButton(
                self.chat_frame,
                text=chat["title"],
                anchor="w",
                command=lambda i=index: self.controller.open_chat(i)
            ).pack(
                fill="x",
                pady=2
            )

    # --------------------------------

    def new_chat(self):

        self.controller.new_chat()

        self.refresh()
