import os
import customtkinter as ctk

from services.file_service import (
    load_text_file,
    save_text_file
)

from services.autocomplete import AutoCompleteService
from ai.ai_engine import AIEngine

from gui.ghost_text import GhostText
from gui.editor_tabs import EditorTabs
from gui.editor_view import EditorView


class CodeEditor:

    def __init__(self, parent):

        self.current_file = None
        self.open_files = {}
        self.dirty_files = set()

        self.frame = ctk.CTkFrame(parent)

        # -------------------------
        # AI Autocomplete
        # -------------------------

        self.autocomplete = AutoCompleteService(
            AIEngine()
        )

        self.autocomplete_job = None
        self.ghost_text = ""

        # -------------------------
        # Tabs
        # -------------------------

        self.tabs = EditorTabs(self.frame)

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

        self.save_button.pack(side="right")

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

        self.editor_view = EditorView(self.frame)

        self.editor_view.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.ghost = GhostText(
            self.editor_view.widget()
        )

        widget = self.editor_view.widget()

        widget.bind(
            "<<Modified>>",
            self._on_modified
        )

        widget.bind(
            "<KeyRelease>",
            self._on_key_release
        )

        widget.bind(
            "<Tab>",
            self._accept_completion
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

    def _on_key_release(self, event):

        if self.ghost.has_suggestion():
            self.ghost.clear()

        if self.autocomplete_job:
            self.frame.after_cancel(
                self.autocomplete_job
            )

        self.autocomplete_job = self.frame.after(
            500,
            self.request_completion
        )

    # --------------------------------

    def request_completion(self):

        code = self.get_text()

        if len(code.strip()) < 10:
            return

        self.set_status(
            "🤖 Thinking..."
        )

        self.autocomplete.complete(
            code,
            self.show_completion
        )

    # --------------------------------

    def show_completion(self, suggestion):

        self.ghost_text = suggestion

        self.frame.after(
            0,
            lambda: (
                self.ghost.show(suggestion),
                self.set_status(
                    "💡 Suggestion ready (Tab)"
                )
            )
        )

    # --------------------------------

    def _accept_completion(self, event=None):

        if not self.ghost.has_suggestion():
            return

        self.ghost.accept()

        self.ghost_text = ""

        self.set_status(
            "Suggestion accepted ✓"
        )

        return "break"

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

        short = os.path.basename(filename)

        self.tabs.add_tab(filename)

        self.file_label.configure(
            text=short
        )

        self.set_status("Opening...")

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

        self.set_status("Saved ✓")

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
        self.editor_view.widget().edit_modified(False)

    # --------------------------------

    def editor_widget(self):

        return self.editor_view.widget()

    # --------------------------------

    def get_selected_text(self):

        try:
            return self.editor_widget().get(
                "sel.first",
                "sel.last"
            )
        except Exception:
            return ""

    # --------------------------------

    def replace_selected_text(self, text):

        try:
            widget = self.editor_widget()
            widget.delete(
                "sel.first",
                "sel.last"
            )
            widget.insert(
                "insert",
                text
            )
        except Exception:
            pass

    # --------------------------------

    def clear(self):

        self.current_file = None

        self.file_label.configure(
            text="No file open"
        )

        self.editor_view.clear()

        self.set_status("Ready")
