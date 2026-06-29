import os
import customtkinter as ctk


FILE_ICONS = {
    ".py": "🐍",
    ".js": "🟨",
    ".ts": "🔷",
    ".json": "🟫",
    ".html": "🌐",
    ".css": "🎨",
    ".md": "📘",
    ".txt": "📄",
    ".png": "🖼",
    ".jpg": "🖼",
    ".jpeg": "🖼",
    ".gif": "🖼",
    ".svg": "🖼",
}


class ProjectExplorer(ctk.CTkFrame):

    def __init__(self, parent, open_callback):

        super().__init__(parent)

        self.open_callback = open_callback
        self.project = None
        self.selected = None

        # --------------------------------
        # Header
        # --------------------------------

        header = ctk.CTkFrame(self)

        header.pack(
            fill="x",
            padx=10,
            pady=(10, 5)
        )

        ctk.CTkLabel(
            header,
            text="📁 Explorer",
            font=("Segoe UI", 20, "bold")
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            header,
            text="⟳",
            width=36,
            command=self.refresh
        ).pack(
            side="right",
            padx=5
        )

        # --------------------------------
        # Search
        # --------------------------------

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search files..."
        )

        self.search.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        self.search.bind(
            "<KeyRelease>",
            lambda e: self.refresh()
        )

        # --------------------------------
        # File List
        # --------------------------------

        self.files = ctk.CTkScrollableFrame(self)

        self.files.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

    # --------------------------------

    def load_project(self, folder):

        self.project = folder
        self.refresh()

    # --------------------------------

    def icon(self, filename):

        ext = os.path.splitext(filename)[1].lower()

        return FILE_ICONS.get(ext, "📄")

    # --------------------------------

    def open_file(self, path):

        self.selected = path

        self.open_callback(path)

        self.refresh()

    # --------------------------------

    def refresh(self):

        for widget in self.files.winfo_children():
            widget.destroy()

        if not self.project:
            return

        query = self.search.get().lower()

        for root, dirs, files in os.walk(self.project):

            dirs.sort()
            files.sort()

            rel = os.path.relpath(
                root,
                self.project
            )

            if rel == ".":
                folder_name = os.path.basename(self.project)
            else:
                folder_name = rel

            ctk.CTkLabel(
                self.files,
                text=f"📂 {folder_name}",
                anchor="w",
                font=("Segoe UI", 13, "bold")
            ).pack(
                fill="x",
                padx=5,
                pady=(10, 2)
            )

            for filename in files:

                if query and query not in filename.lower():
                    continue

                path = os.path.join(root, filename)

                color = "#2563EB" if path == self.selected else "transparent"

                ctk.CTkButton(
                    self.files,
                    text=f"{self.icon(filename)}  {filename}",
                    anchor="w",
                    fg_color=color,
                    hover_color="#303030",
                    command=lambda p=path: self.open_file(p)
                ).pack(
                    fill="x",
                    padx=20,
                    pady=1
                )
