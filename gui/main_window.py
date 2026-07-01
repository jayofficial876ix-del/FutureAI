import customtkinter as ctk

from gui.app_layout import AppLayout
from gui.chat_controller import ChatController
from gui.symbol_search import SymbolSearch
from gui.quick_open import QuickOpen

from services.session_manager import SessionManager

from projects.project_manager import current_project_path


def start_gui():

    # -------------------------
    # Theme
    # -------------------------

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # -------------------------
    # Session
    # -------------------------

    session = SessionManager()

    saved = session.load()

    # -------------------------
    # App
    # -------------------------

    app = ctk.CTk()

    app.title("🤖 Future AI")

    app.geometry(
        saved.get(
            "window",
            "1800x1000"
        )
    )

    # -------------------------
    # Controller
    # -------------------------

    controller = ChatController(
        app,
        None
    )

    # -------------------------
    # Layout
    # -------------------------

    layout = AppLayout(
        app,
        controller
    )

    controller.layout = layout

    # -------------------------
    # Restore Open Tabs
    # -------------------------

    try:

        opened = set()

        for filename in saved.get(
            "open_files",
            []
        ):

            if filename in opened:
                continue

            layout.editor.open_file(filename)

            opened.add(filename)

    except Exception as e:

        print("Restore tabs:", e)

    # -------------------------
    # Restore Current File
    # -------------------------

    try:

        current = saved.get(
            "current_file"
        )

        if current:

            layout.editor.open_file(current)

    except Exception as e:

        print("Restore current file:", e)

    # -------------------------
    # Ctrl + T
    # Symbol Search
    # -------------------------

    def open_symbol_search(event=None):

        SymbolSearch(
            app,
            controller.open_symbol
        )

    app.bind_all(
        "<Control-t>",
        open_symbol_search
    )

    # -------------------------
    # Ctrl + P
    # Quick Open
    # -------------------------

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

    # -------------------------
    # Ctrl + K
    # Inline AI
    # -------------------------

    app.bind_all(
        "<Control-k>",
        controller.inline_ai
    )

    # -------------------------
    # Close
    # -------------------------

    def on_close():

        try:

            session.save(

                editor=layout.editor,

                app=app,

                project=current_project_path()

            )

        except Exception as e:

            print("Session Save:", e)

        app.destroy()

    app.protocol(
        "WM_DELETE_WINDOW",
        on_close
    )

    # -------------------------
    # Start
    # -------------------------

    app.mainloop()
