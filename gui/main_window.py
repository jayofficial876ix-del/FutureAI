import customtkinter as ctk

from gui.app_layout import AppLayout
from gui.chat_controller import ChatController
from gui.symbol_search import SymbolSearch
from gui.quick_open import QuickOpen

from projects.project_manager import current_project_path


def start_gui():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("🤖 Future AI")
    app.geometry("1800x1000")

    # --------------------------------
    # Controller
    # --------------------------------

    controller = ChatController(
        app,
        None
    )

    # --------------------------------
    # Main Layout
    # --------------------------------

    layout = AppLayout(
        app,
        controller
    )

    controller.layout = layout

    # --------------------------------
    # Ctrl + T
    # Go To Symbol
    # --------------------------------

    def open_symbol_search(event=None):

        SymbolSearch(
            app,
            controller.open_symbol
        )

    app.bind_all(
        "<Control-t>",
        open_symbol_search
    )

    # --------------------------------
    # Ctrl + P
    # Quick Open
    # --------------------------------

    def quick_open(event=None):

        project = current_project_path()

        if not project:
            return

        QuickOpen(
            app,
            project,
            layout.editor.open_file
        )

    app.bind_all(
        "<Control-p>",
        quick_open
    )

    # --------------------------------
    # Ctrl + K
    # Inline AI
    # --------------------------------

    app.bind_all(
        "<Control-k>",
        controller.inline_ai
    )

    app.mainloop()
