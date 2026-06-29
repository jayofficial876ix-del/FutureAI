import customtkinter as ctk


class RichMessage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#2B2B2B",
            corner_radius=18
        )

        # Toolbar
        toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        toolbar.pack(
            fill="x",
            padx=10,
            pady=(10, 0)
        )

        self.copy_btn = ctk.CTkButton(
            toolbar,
            text="📋 Copy",
            width=90,
            command=self.copy
        )

        self.copy_btn.pack(
            side="right"
        )

        # Rich Text

        self.textbox = ctk.CTkTextbox(
            self,
            wrap="word",
            font=("Consolas", 14)
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        self.textbox.configure(
            state="disabled"
        )

    # --------------------------------

    def set_text(self, text):

        self.textbox.configure(
            state="normal"
        )

        self.textbox.delete(
            "1.0",
            "end"
        )

        self.textbox.insert(
            "end",
            text
        )

        self.textbox.configure(
            state="disabled"
        )

    # --------------------------------

    def append(self, text):

        self.textbox.configure(
            state="normal"
        )

        self.textbox.insert(
            "end",
            text
        )

        self.textbox.see(
            "end"
        )

        self.textbox.configure(
            state="disabled"
        )

    # --------------------------------

    def copy(self):

        text = self.textbox.get(
            "1.0",
            "end-1c"
        )

        self.clipboard_clear()
        self.clipboard_append(text)
