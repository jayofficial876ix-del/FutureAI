import os
import customtkinter as ctk

from services.file_service import (
    load_text_file,
    save_text_file
)

from gui.inline_prompt import InlinePrompt
from gui.editor_tabs import EditorTabs
from gui.editor_view import EditorView


class CodeEditor:

    def __init__(self, parent):

        self.current_file = None

        self.open_files = {}

        self.dirty_files = set()

        self.frame = ctk.CTkFrame(parent)

        # -------------------------
        # Tabs
        # -------------------------

        self.tabs = EditorTabs(
            self.frame
        )

        self.tabs.pack(
            fill="x",
            padx=10,
            pady=(10, 0)
        )

        # -------------------------
        # Toolbar
        # -------------------------

        toolbar = ctk.CTkFrame(self.frame)

        toolbar.pack(
            fill="x",
            padx=10,
            pady=(5, 0)
        )

        self.file_label = ctk.CTkLabel(
            toolbar,
            text="No file open",
            font=("Segoe UI", 14, "bold")
        )

        self.file_label.pack(side="left")

        self.improve_button = ctk.CTkButton(
            toolbar,
            text="🤖 Improve",
            width=110
        )

        self.improve_button.pack(
            side="right",
            padx=(0, 8)
        )

        self.save_button = ctk.CTkButton(
            toolbar,
            text="💾 Save",
            width=90,
            command=self.save_file
        )

        self.save_button.pack(
            side="right"
        )

        # -------------------------
        # Status
        # -------------------------

        self.status = ctk.CTkLabel(
            self.frame,
            text="Ready",
            text_color="gray",
            anchor="w"
        )

        self.status.pack(
            fill="x",
            padx=12,
            pady=(5, 0)
        )

        # -------------------------
        # Editor
        # -------------------------

        self.editor_view = EditorView(
            self.frame
        )

        self.editor_view.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Detect typing

        widget = self.editor_view.widget()

        widget.bind(
            "<<Modified>>",
            self._on_modified
        )

        widget.bind(
            "<Control-i>",
            self.inline_ai
        )

    # --------------------------------

    def _on_modified(self, event):

        widget = self.editor_view.widget()

        if not widget.edit_modified():
            return

        widget.edit_modified(False)

        if not self.current_file:
            return

        self.dirty_files.add(
            self.current_file
        )

        self.tabs.set_dirty(
            os.path.basename(
                self.current_file
            ),
            True
        )

    # --------------------------------

    def pack(self, **kwargs):

        self.frame.pack(**kwargs)

    # --------------------------------

    def open_file(self, filename):

        if self.current_file:

            self.open_files[
                self.current_file
            ] = self.get_text()

        self.current_file = filename

        short = os.path.basename(
            filename
        )

        self.tabs.add_tab(filename)

        self.file_label.configure(
            text=short
        )

        self.set_status(
            "Opening..."
        )

        if filename in self.open_files:

            text = self.open_files[
                filename
            ]

        else:

            text = load_text_file(
                filename
            )

            self.open_files[
                filename
            ] = text

        self.set_text(text)

        self.tabs.set_dirty(
            short,
            False
        )

        self.set_status("Ready")

    # --------------------------------

    def save_file(self):

        if not self.current_file:
            return

        text = self.get_text()

        save_text_file(
            self.current_file,
            text
        )

        self.open_files[
            self.current_file
        ] = text

        self.dirty_files.discard(
            self.current_file
        )

        self.tabs.set_dirty(
            os.path.basename(
                self.current_file
            ),
            False
        )

        self.set_status(
            "Saved ✓"
        )

    # --------------------------------

    def set_improve_callback(self, callback):

        self.improve_button.configure(
            command=lambda: callback(self)
        )

    # --------------------------------

    def set_status(self, text):

        self.status.configure(
            text=text
        )

    # --------------------------------

    def get_text(self):

        return self.editor_view.get()

    # --------------------------------

    def set_text(self, text):

        self.editor_view.set(text)

        widget = self.editor_view.widget()

        widget.edit_modified(False)

    # --------------------------------

    def editor_widget(self):

        return self.editor_view.widget()

    # --------------------------------

    def clear(self):

        self.current_file = None

        self.file_label.configure(
            text="No file open"
        )

        self.editor_view.clear()

        self.set_status(
            "Ready"
        )

    # --------------------------------

    def inline_ai(self, event=None):

        widget = self.editor_view.widget()

        try:
            selected = widget.get(
                "sel.first",
                "sel.last"
            )
        except Exception:
            self.set_status(
                "Select some code first."
            )
            return

        InlinePrompt(
            widget.winfo_toplevel(),
            lambda prompt: self.run_inline_ai(
                selected,
                prompt
            )
        )

    # --------------------------------

    def run_inline_ai(self, selected_code, prompt):

        self.set_status(
            "Future AI is editing..."
        )

        if not hasattr(self, "ai_actions"):

            self.set_status(
                "AI is not connected."
            )

            return

        new_code = self.ai_actions.inline_edit(
            selected_code,
            prompt
        )

        if not new_code:

            self.set_status(
                "AI failed."
            )

            return

        from services.code_diff import generate_diff
        from gui.diff_viewer import DiffViewer

        diff = generate_diff(
            selected_code,
            new_code
        )

        widget = self.editor_view.widget()

        def apply():

            try:
                widget.delete(
                    "sel.first",
                    "sel.last"
                )

                widget.insert(
                    "insert",
                    new_code
                )

                self.set_status(
                    "Inline edit complete ✓"
                )

            except Exception:

                self.set_status(
                    "Couldn't replace selection."
                )

        DiffViewer(
            widget.winfo_toplevel(),
            diff,
            apply
        )
