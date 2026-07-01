import os
import customtkinter as ctk
from tkinter import ttk


class FileExplorer(ctk.CTkFrame):

    def __init__(self, parent, open_callback):

        super().__init__(parent)

        self.open_callback = open_callback

        self.project = None

        self.tree = ttk.Treeview(
            self,
            show="tree"
        )

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self._selected
        )

    # --------------------------------

    def load_project(self, project_path):

        self.project = project_path

        self.tree.delete(
            *self.tree.get_children()
        )

        root = self.tree.insert(
            "",
            "end",
            text=os.path.basename(project_path),
            open=True,
            values=[project_path]
        )

        self._load_folder(
            root,
            project_path
        )

    # --------------------------------

    def _load_folder(self, parent, folder):

        try:
            entries = sorted(
                os.listdir(folder),
                key=lambda x: (
                    not os.path.isdir(
                        os.path.join(folder, x)
                    ),
                    x.lower()
                )
            )
        except Exception:
            return

        for name in entries:
            full = os.path.join(
                folder,
                name
            )

            node = self.tree.insert(
                parent,
                "end",
                text=name,
                open=False,
                values=[full]
            )

            if os.path.isdir(full):
                self._load_folder(
                    node,
                    full
                )

    # --------------------------------

    def _selected(self, event):

        item = self.tree.focus()

        if not item:
            return

        values = self.tree.item(
            item,
            "values"
        )

        if not values:
            return

        path = values[0]

        if os.path.isfile(path):
            self.open_callback(path)
