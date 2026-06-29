import customtkinter as ctk

from services.indexer.workspace_search import WorkspaceSearch


class SymbolSearch(ctk.CTkToplevel):

    def __init__(self, parent, open_callback):

        super().__init__(parent)

        self.search = WorkspaceSearch()
        self.open_callback = open_callback

        self.title("Go To Symbol")
        self.geometry("650x500")

        self.transient(parent)
        self.grab_set()

        ctk.CTkLabel(
            self,
            text="🔎 Go To Symbol",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(15, 10)
        )

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Search classes, functions, files..."
        )

        self.entry.pack(
            fill="x",
            padx=15,
            pady=(0, 10)
        )

        self.entry.focus()

        self.entry.bind(
            "<KeyRelease>",
            self.filter
        )

        self.results = ctk.CTkScrollableFrame(self)

        self.results.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    # --------------------------------

    def filter(self, event=None):

        query = self.entry.get().strip()

        for widget in self.results.winfo_children():
            widget.destroy()

        if not query:
            return

        matches = self.search.find_symbol(query)

        for name, symbol_type, filename, line in matches:

            text = (
                f"{symbol_type.upper()} • "
                f"{name}  "
                f"({filename}:{line})"
            )

            ctk.CTkButton(
                self.results,
                text=text,
                anchor="w",
                command=lambda f=filename, l=line: self.open_symbol(f, l)
            ).pack(
                fill="x",
                pady=2
            )

    # --------------------------------

    def open_symbol(self, filename, line):

        self.destroy()

        self.open_callback(
            filename,
            line
        )
