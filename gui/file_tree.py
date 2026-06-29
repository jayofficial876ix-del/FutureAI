import os
import customtkinter as ctk


class FileTree:

    def __init__(self, parent, open_file):

        self.parent = parent
        self.open_file = open_file

        self.frame = ctk.CTkScrollableFrame(parent)

        # Keeps track of expanded folders
        self.expanded = {}

        self.project = None

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def clear(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

    def load_project(self, project):

        self.project = project

        self.refresh()

    def refresh(self):

        self.clear()

        if not self.project:
            return

        ctk.CTkLabel(
            self.frame,
            text=f"📁 {self.project['name']}",
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=5,
            pady=(5, 10)
        )

        folders = {}

        for filepath in self.project["files"]:

            filepath = filepath.replace("\\", "/")

            rel = filepath

            parts = rel.split("/")

            if len(parts) < 2:
                continue

            folder = "/".join(parts[:-1])

            folders.setdefault(folder, [])

            folders[folder].append(filepath)

        for folder in sorted(folders):

            self.draw_folder(
                folder,
                folders[folder]
            )

    def draw_folder(self, folder, files):

        name = os.path.basename(folder)

        expanded = self.expanded.get(folder, False)

        arrow = "▼" if expanded else "▶"

        ctk.CTkButton(
            self.frame,
            text=f"{arrow} 📂 {name}",
            anchor="w",
            fg_color="transparent",
            command=lambda f=folder: self.toggle(f)
        ).pack(
            fill="x",
            padx=10,
            pady=2
        )

        if not expanded:
            return

        for filepath in sorted(files):

            filename = os.path.basename(filepath)

            ctk.CTkButton(
                self.frame,
                text=f"      📄 {filename}",
                anchor="w",
                fg_color="transparent",
                command=lambda f=filepath: self.open_file(f)
            ).pack(
                fill="x",
                padx=20,
                pady=1
            )

    def toggle(self, folder):

        self.expanded[folder] = not self.expanded.get(folder, False)

        self.refresh()
