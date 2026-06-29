import os
import customtkinter as ctk


class GlobalSearch(ctk.CTkToplevel):

    def __init__(self, parent, project, open_file):

        super().__init__(parent)

        self.project = project
        self.open_file = open_file

        self.title("🔍 Search Across Project")
        self.geometry("700x600")

        self.transient(parent)
        self.focus_force()

        ctk.CTkLabel(
            self,
            text="🔍 Search Across Project",
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(15, 10)
        )

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search..."
        )

        self.search.pack(
            fill="x",
            padx=15
        )

        self.search.focus()

        self.search.bind(
            "<KeyRelease>",
            self.search_project
        )

        self.results = ctk.CTkScrollableFrame(self)

        self.results.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

    def search_project(self, event=None):

        for widget in self.results.winfo_children():
            widget.destroy()

        text = self.search.get().lower()

        if not text:
            return

        for filename in self.project["files"]:

            try:

                with open(
                    filename,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    for line_no, line in enumerate(f, start=1):

                        if text not in line.lower():
                            continue

                        preview = line.strip()

                        button = ctk.CTkButton(
                            self.results,
                            anchor="w",
                            text=f"{os.path.basename(filename)} : {line_no}\n{preview}",
                            height=55,
                            command=lambda f=filename: self.open_file(f)
                        )

                        button.pack(
                            fill="x",
                            pady=2
                        )

            except Exception:
                pass
