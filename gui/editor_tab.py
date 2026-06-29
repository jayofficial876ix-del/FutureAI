import customtkinter as ctk


class EditorTab(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        filename,
        callback,
        close_callback
    ):

        super().__init__(
            parent,
            corner_radius=6,
            fg_color="#2F2F2F"
        )

        self.filename = filename
        self.callback = callback
        self.close_callback = close_callback

        self.modified = False

        self.button = ctk.CTkButton(
            self,
            text=filename,
            fg_color="transparent",
            anchor="w",
            command=self.open
        )

        self.button.pack(
            side="left",
            padx=(8, 2),
            pady=4,
            fill="x",
            expand=True
        )

        self.close = ctk.CTkButton(
            self,
            text="✕",
            width=28,
            fg_color="transparent",
            command=self.close_tab
        )

        self.close.pack(
            side="right",
            padx=(0, 6)
        )

    # -----------------------------

    def open(self):

        self.callback(
            self.filename
        )

    # -----------------------------

    def close_tab(self):

        self.close_callback(
            self.filename
        )

    # -----------------------------

    def set_active(self, active):

        color = "#2563EB" if active else "#2F2F2F"

        self.configure(
            fg_color=color
        )

    # -----------------------------

    def set_modified(self, modified):

        self.modified = modified

        text = self.filename

        if modified:
            text += " ●"

        self.button.configure(
            text=text
        )
