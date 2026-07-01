from tkinter import messagebox

from history.chat_history import (
    create_chat,
    delete_chat,
    load_chats,
    rename_chat
)

from gui.chat_view import create_welcome_card


class ChatHistoryController:

    def __init__(self, controller):

        self.controller = controller

    # --------------------------------

    def clear_chat(self):

        if not self.controller.chat:
            return

        for widget in self.controller.chat.winfo_children():
            widget.destroy()

    # --------------------------------

    def new_chat(self):

        self.controller.current_chat = None
        self.controller.welcome_cleared = False
        self.controller.attached_file = None

        self.clear_chat()

        create_welcome_card(
            self.controller.chat
        )

    # --------------------------------

    def open_chat(self, chat_id):

        self.controller.current_chat = chat_id
        self.controller.welcome_cleared = True

        self.clear_chat()

    # --------------------------------

    def rename_if_needed(self, user_message):

        chats = load_chats()

        if self.controller.current_chat is None:
            return

        if len(
            chats[self.controller.current_chat]["messages"]
        ) != 1:
            return

        rename_chat(

            self.controller.current_chat,

            user_message

        )

        if self.controller.sidebar:

            self.controller.sidebar.refresh()

    # --------------------------------

    def delete_chat(self, chat_id):

        answer = messagebox.askyesno(

            "Delete Chat",

            "Delete this conversation?"

        )

        if not answer:
            return

        delete_chat(chat_id)

        if self.controller.current_chat == chat_id:

            self.controller.current_chat = None
            self.controller.attached_file = None
            self.controller.welcome_cleared = False

            self.clear_chat()

            create_welcome_card(
                self.controller.chat
            )

        elif (

            self.controller.current_chat is not None
            and chat_id < self.controller.current_chat

        ):

            self.controller.current_chat -= 1

        if self.controller.sidebar:

            self.controller.sidebar.refresh()
