import os
import customtkinter as ctk


class FileSearch(ctk.CTkToplevel):

    def __init__(self, parent, project, open_file):

        super().__init__(parent)

        self.project = project
        self.open_file = open_file

        self.title("Quick Open")
        self.geometry("500x500")

        self.transient(parent)
        self.focus_force()

        ctk.CTkLabel(
            self,
            text="📂 Quick Open",
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(15, 10)
        )

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Type a filename..."
        )

        self.search.pack(
            fill="x",
            padx=15
        )

        self.search.focus()

        self.search.bind(
            "<KeyRelease>",
            self.update_results
        )

        self.results = ctk.CTkScrollableFrame(self)

        self.results.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.update_results()

    def update_results(self, event=None):

        for widget in self.results.winfo_children():
            widget.destroy()

        text = self.search.get().lower()

        for filename in self.project["files"]:

            short = os.path.basename(filename)

            if text not in short.lower():
                continue

            ctk.CTkButton(
                self.results,
                text=short,
                anchor="w",
                command=lambda f=filename: self.open(f)
            ).pack(
                fill="x",
                pady=2
            )

    def open(self, filename):

        self.destroy()

        self.open_file(filename)
