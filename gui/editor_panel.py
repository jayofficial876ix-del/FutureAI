import os
import customtkinter as ctk

from tkinter import simpledialog

from gui.editor_tabs import EditorTabs
from gui.split_editor import SplitEditor
from gui.terminal_panel import TerminalPanel


class EditorPanel(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(
            parent,
            corner_radius=0
        )

        self.controller = controller
        self.open_files = {}

        # --------------------------------
        # Toolbar
        # --------------------------------

        toolbar = ctk.CTkFrame(
            self,
            height=45
        )

        toolbar.pack(
            fill="x",
            padx=8,
            pady=(8, 0)
        )

        toolbar.pack_propagate(False)

        ctk.CTkButton(
            toolbar,
            text="💾 Save",
            width=95,
            command=self.save_current
        ).pack(
            side="left",
            padx=4
        )

        ctk.CTkButton(
            toolbar,
            text="▶ Run",
            width=95,
            command=self.run_current
        ).pack(
            side="left",
            padx=4
        )

        ctk.CTkButton(
            toolbar,
            text="🤖 Improve",
            width=110,
            command=lambda: controller.improve_editor_code(
                self.editor.active_editor()
            )
        ).pack(
            side="left",
            padx=4
        )

        ctk.CTkButton(
            toolbar,
            text="⚡ Commands",
            width=110
        ).pack(
            side="left",
            padx=4
        )

        ctk.CTkButton(
            toolbar,
            text="🤖 Agent",
            width=100,
            command=self.open_agent
        ).pack(
            side="left",
            padx=4
        )

        self.split_button = ctk.CTkButton(
            toolbar,
            text="🪟 Split",
            width=100,
            command=self.toggle_split
        )

        self.split_button.pack(
            side="right",
            padx=4
        )

        # --------------------------------
        # Tabs
        # --------------------------------

        self.tabs = EditorTabs(
            self,
            self.switch_file
        )

        self.tabs.pack(
            fill="x",
            padx=8,
            pady=(6, 0)
        )

        # --------------------------------
        # Split Editor
        # --------------------------------

        self.editor = SplitEditor(
            self,
            controller
        )

        self.editor.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(5, 0)
        )

        controller.editor = self.editor.active_editor()

        # Connect AI to both editors
        self.editor.left.ai_actions = controller.ai_actions
        self.editor.right.ai_actions = controller.ai_actions

        # --------------------------------
        # Terminal
        # --------------------------------

        self.terminal = TerminalPanel(self)

        self.terminal.pack(
            fill="x",
            padx=8,
            pady=8
        )

        controller.terminal = self.terminal

        if hasattr(
            self.terminal,
            "set_error_callback"
        ):

            self.terminal.set_error_callback(
                controller.explain_error
            )

    # --------------------------------

    def open_agent(self):

        request = simpledialog.askstring(
            "Future AI Agent",
            "What would you like Future AI to build or modify?"
        )

        if not request:
            return

        self.controller.run_agent(request)

    # --------------------------------

    def toggle_split(self):

        if self.editor.split:

            self.editor.disable_split()

            self.split_button.configure(
                text="🪟 Split"
            )

        else:

            self.editor.enable_split()

            self.split_button.configure(
                text="🪟 Single"
            )

    # --------------------------------

    def open_file(self, filename):

        self.open_files[filename] = filename

        self.tabs.add_tab(filename)

        self.editor.open_file(filename)

    # --------------------------------

    def switch_file(self, tab):

        for path in self.open_files:

            if os.path.basename(path) == tab:

                self.editor.open_file(path)

                break

    # --------------------------------

    def save_current(self):

        self.editor.active_editor().save_file()

    # --------------------------------

    def run_current(self):

        editor = self.editor.active_editor()

        if not editor.current_file:
            return

        editor.save_file()

        self.terminal.run_python(
            editor.current_file
        )

    # --------------------------------

    def get_selected_text(self):

        return self.editor.active_editor().get_selected_text()

    # --------------------------------

    def replace_selected_text(self, text):

        self.editor.active_editor().replace_selected_text(text)

    # --------------------------------

    def get_text(self):

        return self.editor.active_editor().get_text()

    # --------------------------------

    def set_text(self, text):

        self.editor.active_editor().set_text(text)

    # --------------------------------

    @property
    def current_file(self):

        return self.editor.active_editor().current_file
