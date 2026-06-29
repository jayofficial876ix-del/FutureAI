import os
import customtkinter as ctk

from gui.editor_tab import EditorTab


class EditorTabs(ctk.CTkFrame):

    def __init__(self, parent, on_select=None):

        super().__init__(
            parent,
            height=40,
            fg_color="#202020"
        )

        self.pack_propagate(False)

        self.on_select = on_select

        self.tabs = {}

        self.active = None

    # --------------------------------

    def add_tab(self, filename):

        name = os.path.basename(filename)

        if name in self.tabs:

            self.select_tab(name)
            return

        tab = EditorTab(

            self,

            name,

            self.select_tab,

            self.close_tab

        )

        tab.pack(

            side="left",

            padx=2,

            pady=4

        )

        self.tabs[name] = tab

        self.select_tab(name)

    # --------------------------------

    def select_tab(self, name):

        self.active = name

        for tab_name, tab in self.tabs.items():

            tab.set_active(
                tab_name == name
            )

        if self.on_select:

            self.on_select(name)

    # --------------------------------

    def set_dirty(self, name, dirty=True):

        if name not in self.tabs:
            return

        self.tabs[name].set_modified(dirty)

    # --------------------------------

    def close_tab(self, name):

        if name not in self.tabs:
            return

        self.tabs[name].destroy()

        del self.tabs[name]

        if self.active == name:

            self.active = None

            if self.tabs:

                first = next(iter(self.tabs))

                self.select_tab(first)
