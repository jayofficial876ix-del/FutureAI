import customtkinter as ctk

from gui.sidebar import create_sidebar
from gui.chat_view import create_chat_view
from gui.input_bar import create_input_bar
from gui.chat_controller import ChatController


def start_gui():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("🤖 Future AI")
    app.geometry("1200x720")

    # ==========================
    # Chat Area
    # ==========================

    chat_frame, chat = create_chat_view(app)

    # ==========================
    # Chat Controller
    # ==========================

    controller = ChatController(app, chat)

    # ==========================
    # Sidebar
    # ==========================

    create_sidebar(
        app,
        controller.open_chat,
        controller.new_chat
    )

    # ==========================
    # Input Bar
    # ==========================

    message, send_button = create_input_bar(
        chat_frame,
        lambda: controller.send(message)
    )

    app.mainloop()
