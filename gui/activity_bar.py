import customtkinter as ctk


class ActivityBar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=60,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.buttons = {}

        self.callback = None

        # Logo
        ctk.CTkLabel(
            self,
            text="🤖",
            font=("Segoe UI", 24)
        ).pack(
            pady=(20, 30)
        )

        self.add_button("chat", "💬")
        self.add_button("explorer", "📁")
        self.add_button("search", "🔍")
        self.add_button("agent", "🧠")
        self.add_button("tools", "🛠")
        self.add_button("settings", "⚙️")

    # -------------------------

    def set_callback(self, callback):

        self.callback = callback

    # -------------------------

    def add_button(self, name, icon):

        btn = ctk.CTkButton(
            self,
            text=icon,
            width=46,
            height=46,
            fg_color="transparent",
            hover_color="#2f5fff",
            command=lambda n=name: self.select(n)
        )

        btn.pack(pady=5)

        self.buttons[name] = btn

    # -------------------------

    def select(self, name):

        for b in self.buttons.values():
            b.configure(
                fg_color="transparent"
            )

        self.buttons[name].configure(
            fg_color="#2f5fff"
        )

        if self.callback:
            self.callback(name)
