from tkinter import simpledialog, messagebox

from brain import get_response, teach

from gui.message_bubble import (
    add_user_bubble,
    add_ai_bubble,
    add_system_bubble
)

from gui.chat_view import create_welcome_card

from history.chat_history import (
    create_chat,
    add_message,
    rename_chat,
    load_chats,
    get_chat,
    delete_chat
)


class ChatController:

    def __init__(self, app, chat):

        self.app = app
        self.chat = chat

        self.current_chat = None

        self.welcome_cleared = False

        self.sidebar = None

    def clear_chat(self):

        for widget in self.chat.winfo_children():
            widget.destroy()

    def open_chat(self, chat_id):

        self.current_chat = chat_id
        self.welcome_cleared = True

        self.clear_chat()

        conversation = get_chat(chat_id)

        if conversation is None:
            create_welcome_card(self.chat)
            return

        if len(conversation["messages"]) == 0:
            create_welcome_card(self.chat)
            return

        for msg in conversation["messages"]:

            if msg["role"] == "user":
                add_user_bubble(self.chat, msg["text"])

            elif msg["role"] == "assistant":
                add_ai_bubble(self.chat, msg["text"])

    def new_chat(self):

        self.current_chat = None

        self.welcome_cleared = False

        self.clear_chat()

        create_welcome_card(self.chat)

    def delete_chat(self, chat_id):

        answer = messagebox.askyesno(
            "Delete Chat",
            "Delete this conversation?"
        )

        if not answer:
            return

        delete_chat(chat_id)

        # If the deleted chat was open, reset the screen
        if self.current_chat == chat_id:

            self.current_chat = None

            self.clear_chat()

            create_welcome_card(self.chat)

            self.welcome_cleared = False

        # If a chat before the current one was deleted,
        # shift the current index down by one.
        elif self.current_chat is not None and chat_id < self.current_chat:
            self.current_chat -= 1

        if self.sidebar:
            self.sidebar.refresh()

    def send(self, message_box):

        user = message_box.get().strip()

        if not user:
            return

        if not self.welcome_cleared:
            self.clear_chat()
            self.welcome_cleared = True

        add_user_bubble(self.chat, user)

        if self.current_chat is None:

            self.current_chat = create_chat("New Chat")

            if self.sidebar:
                self.sidebar.refresh()

        add_message(
            self.current_chat,
            "user",
            user
        )

        chats = load_chats()

        if len(chats[self.current_chat]["messages"]) == 1:

            rename_chat(
                self.current_chat,
                user
            )

            if self.sidebar:
                self.sidebar.refresh()

        thinking = add_system_bubble(
            self.chat,
            "Future AI is thinking..."
        )

        self.app.update()

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

        thinking.destroy()

        add_ai_bubble(
            self.chat,
            reply
        )

        add_message(
            self.current_chat,
            "assistant",
            reply
        )

        message_box.delete(0, "end")
