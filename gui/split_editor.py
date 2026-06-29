import customtkinter as ctk

from gui.code_editor import CodeEditor


class SplitEditor(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left = CodeEditor(self)
        self.left.frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.right = CodeEditor(self)
        self.right.frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.right.frame.grid_remove()

        self.split = False

        # Track which editor is active
        self.active = self.left

        self._bind_focus(self.left)
        self._bind_focus(self.right)

    # --------------------------------

    def _bind_focus(self, editor):

        widget = editor.editor_widget()

        widget.bind(
            "<FocusIn>",
            lambda e, ed=editor: self.set_active(ed),
            add="+"
        )

    # --------------------------------

    def set_active(self, editor):

        self.active = editor

    # --------------------------------

    def enable_split(self):

        if self.split:
            return

        self.split = True

        self.right.frame.grid()

    # --------------------------------

    def disable_split(self):

        self.split = False

        self.right.frame.grid_remove()

        self.active = self.left

    # --------------------------------

    def active_editor(self):

        return self.active

    # --------------------------------

    def open_file(self, filename):

        self.active_editor().open_file(
            filename
        )
