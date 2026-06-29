import customtkinter as ctk


class FindDialog(ctk.CTkToplevel):

    def __init__(self, parent, editor):

        super().__init__(parent)

        self.editor = editor

        self.title("Find")
        self.geometry("420x120")
        self.resizable(False, False)

        self.transient(parent)
        self.focus_force()

        ctk.CTkLabel(
            self,
            text="Find",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Search..."
        )

        self.entry.pack(
            fill="x",
            padx=15
        )

        self.entry.focus()

        self.entry.bind(
            "<KeyRelease>",
            self.find
        )

        self.entry.bind(
            "<Return>",
            self.find
        )

        editor.tag_config(
            "find_match",
            background="#FFD54A",
            foreground="black"
        )

    def find(self, event=None):

        text = self.entry.get()

        self.editor.tag_remove(
            "find_match",
            "1.0",
            "end"
        )

        if not text:
            return

        start = "1.0"

        while True:

            pos = self.editor.search(
                text,
                start,
                stopindex="end"
            )

            if not pos:
                break

            end = f"{pos}+{len(text)}c"

            self.editor.tag_add(
                "find_match",
                pos,
                end
            )

            start = end

        first = self.editor.search(
            text,
            "1.0",
            stopindex="end"
        )

        if first:
            self.editor.see(first)
            self.editor.mark_set(
                "insert",
                first
            )
