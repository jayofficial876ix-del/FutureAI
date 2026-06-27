import customtkinter as ctk

from gui.sidebar import create_sidebar
from gui.chat_view import create_chat_view
from gui.input_bar import create_input_bar


def start_gui():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("🤖 Future AI")
    app.geometry("1200x720")

    create_sidebar(app)

    chat_frame, chat = create_chat_view(app)

    message, send_button = create_input_bar(chat_frame)

    app.mainloop()
