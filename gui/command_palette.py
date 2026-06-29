import customtkinter as ctk


class CommandPalette(ctk.CTkToplevel):

    def __init__(self, parent, commands):

        super().__init__(parent)

        self.commands = commands
        self.filtered = list(commands.items())
        self.selected = 0

        self.title("Command Palette")
        self.geometry("650x520")
        self.resizable(False, False)

        self.transient(parent)
        self.grab_set()
        self.focus_force()

        # --------------------------------
        # Header
        # --------------------------------

        ctk.CTkLabel(
            self,
            text="⚡ Command Palette",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 8)
        )

        # --------------------------------
        # Search Box
        # --------------------------------

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Type a command..."
        )

        self.entry.pack(
            fill="x",
            padx=20,
            pady=(0, 12)
        )

        self.entry.focus()

        self.entry.bind(
            "<KeyRelease>",
            self.filter_commands
        )

        self.entry.bind(
            "<Down>",
            self.move_down
        )

        self.entry.bind(
            "<Up>",
            self.move_up
        )

        self.entry.bind(
            "<Return>",
            self.execute_selected
        )

        # --------------------------------
        # Results
        # --------------------------------

        self.results = ctk.CTkScrollableFrame(self)

        self.results.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 15)
        )

        self.refresh()

    # --------------------------------

    def refresh(self):

        for widget in self.results.winfo_children():
            widget.destroy()

        if not self.filtered:

            ctk.CTkLabel(
                self.results,
                text="No commands found.",
                text_color="gray"
            ).pack(
                pady=20
            )

            return

        for index, (name, callback) in enumerate(self.filtered):

            color = "#2563EB" if index == self.selected else "transparent"

            button = ctk.CTkButton(
                self.results,
                text=name,
                anchor="w",
                fg_color=color,
                hover_color="#303030",
                command=lambda cb=callback: self.run(cb)
            )

            button.pack(
                fill="x",
                pady=2
            )

    # --------------------------------

    def filter_commands(self, event=None):

        query = self.entry.get().strip().lower()

        if query:

            self.filtered = [
                item
                for item in self.commands.items()
                if query in item[0].lower()
            ]

        else:

            self.filtered = list(
                self.commands.items()
            )

        self.selected = 0

        self.refresh()

    # --------------------------------

    def move_down(self, event=None):

        if not self.filtered:
            return

        self.selected = min(
            self.selected + 1,
            len(self.filtered) - 1
        )

        self.refresh()

    # --------------------------------

    def move_up(self, event=None):

        if not self.filtered:
            return

        self.selected = max(
            self.selected - 1,
            0
        )

        self.refresh()

    # --------------------------------

    def execute_selected(self, event=None):

        if not self.filtered:
            return

        _, callback = self.filtered[self.selected]

        self.run(callback)

    # --------------------------------

    def run(self, callback):

        self.destroy()

        callback()
