from history.chat_history import (
    create_chat,
    add_message,
    rename_chat,
    load_chats
)

from gui.message_bubble import (
    add_user_bubble,
    add_streaming_bubble,
    add_system_bubble
)

from services.workspace_context import WorkspaceContext


class ChatController:

    def __init__(
        self,
        app,
        chat,
        ai,
        assistant,
        sidebar=None,
        right_sidebar=None
    ):

        self.app = app
        self.chat = chat

        self.ai = ai
        self.assistant = assistant

        self.sidebar = sidebar
        self.right_sidebar = right_sidebar

        self.workspace = WorkspaceContext()

        self.current_chat = None
        self.welcome_cleared = False

        self.editor = None
        self.terminal = None

        self.attached_file = None

    # --------------------------------

    def set_editor(self, editor):

        self.editor = editor

    # --------------------------------

    def set_terminal(self, terminal):

        self.terminal = terminal

    # --------------------------------

    def send(self, text):

        if not text.strip():
            return

        add_user_bubble(
            self.chat,
            text
        )

        if self.current_chat is None:

            self.current_chat = create_chat(
                "New Chat"
            )

            if self.sidebar:
                self.sidebar.refresh()

        add_message(

            self.current_chat,

            "user",

            text

        )

        chats = load_chats()

        if len(
            chats[self.current_chat]["messages"]
        ) == 1:

            rename_chat(

                self.current_chat,

                text

            )

            if self.sidebar:

                self.sidebar.refresh()

        conversation = []

        for msg in chats[
            self.current_chat
        ]["messages"]:

            conversation.append({

                "role": msg["role"],

                "content": msg["text"]

            })

        # ----------------------------
        # Workspace
        # ----------------------------

        if self.editor:

            conversation.extend(

                self.workspace.build(

                    self.editor,

                    terminal=self.terminal,

                    open_files=list(
                        self.editor.open_files.keys()
                    )

                )

            )

        thinking = add_system_bubble(

            self.chat,

            "🤖 Future AI is thinking..."

        )

        bubble = add_streaming_bubble(
            self.chat
        )

        reply = ""

        try:

            tool_reply = self.assistant.handle(
                text
            )

            if tool_reply:

                if thinking.winfo_exists():
                    thinking.destroy()

                bubble.update(tool_reply)
                bubble.finish()

                reply = tool_reply

            else:

                for chunk in self.ai.stream_chat(
                    conversation
                ):

                    if thinking.winfo_exists():
                        thinking.destroy()

                    bubble.update(chunk)

                    reply += chunk

                    self.app.update()

                bubble.finish()

        except Exception:

            if thinking.winfo_exists():
                thinking.destroy()

            reply = self.ai.chat(
                conversation
            )

            bubble.update(reply)
            bubble.finish()

        add_message(

            self.current_chat,

            "assistant",

            reply

        )
