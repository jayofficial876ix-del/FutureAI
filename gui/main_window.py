import customtkinter as ctk
from tkinter import simpledialog

from brain import get_response, teach

from gui.sidebar import create_sidebar
from gui.chat_view import create_chat_view
from gui.input_bar import create_input_bar
from gui.message_bubble import (
    add_user_bubble,
    add_ai_bubble,
    add_system_bubble
)


def start_gui():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("🤖 Future AI")
    app.geometry("1200x720")

    # Sidebar
    create_sidebar(app)

    # Chat Area
    chat_frame, chat = create_chat_view(app)

    message = None
    welcome_cleared = False

    def send():
        nonlocal welcome_cleared

        user = message.get().strip()

        if not user:
            return

        # Remove the welcome card on the first message
        if not welcome_cleared:
            for widget in chat.winfo_children():
                widget.destroy()
            welcome_cleared = True

        # User bubble
        add_user_bubble(chat, user)

        # Thinking message
        thinking = add_system_bubble(chat, "Future AI is thinking...")
        app.update()

        # AI response
        reply = get_response(user)

        if reply is None:
            answer = simpledialog.askstring(
                "Teach Future AI",
                f"What should I answer?\n\n{user}"
            )

            if answer:
                teach(user, answer)
                reply = "Thanks! I learned something new."
            else:
                reply = "Okay."

        # Remove thinking message
        thinking.destroy()

        # AI bubble
        add_ai_bubble(chat, reply)

        message.delete(0, "end")

    # Input Bar
    message, send_button = create_input_bar(
        chat_frame,
        send
    )

    app.mainloop()
