from gui.inline_prompt import InlinePrompt
from gui.diff_viewer import DiffViewer
from projects.project_manager import load_projects
from services.context_retriever import ContextRetriever
from tkinter import simpledialog, messagebox
import os

from services.file_manager import choose_file
from services.file_reader import read_file

from ai.ai_engine import AIEngine
from services.ai_actions import AIActions
from services.agent import AIAgent

from gui.message_bubble import (
    add_user_bubble,
    add_ai_bubble,
    add_streaming_bubble,
    add_system_bubble
)

from gui.attachment_card import create_attachment_card
from gui.chat_view import create_welcome_card
from gui.agent_review import AgentReview

from services.code_diff import generate_diff
from services.project_editor import ProjectEditor

from history.chat_history import (
    create_chat,
    add_message,
    rename_chat,
    load_chats,
    get_chat,
    delete_chat
)

from ai.prompts import PROMPTS


class ChatController:

    def __init__(self, app, chat):
        self.app = app
        self.chat = chat

        self.current_chat = None
        self.welcome_cleared = False

        self.sidebar = None
        self.editor = None
        self.terminal = None
        self.right_sidebar = None

        self.context_retriever = ContextRetriever()
        self.ai = AIEngine()
        self.ai_actions = AIActions(self.ai)
        self.agent = AIAgent(self.ai)
        self.project_editor = ProjectEditor()

        self.attached_file = None

    # -------------------------------------------------
    # Chat UI
    # -------------------------------------------------

    def clear_chat(self):
        for widget in self.chat.winfo_children():
            widget.destroy()

    def open_chat(self, chat_id):
        self.current_chat = chat_id
        self.welcome_cleared = True

        self.clear_chat()

    def new_chat(self):
        self.current_chat = None
        self.welcome_cleared = False
        self.attached_file = None

        self.clear_chat()
        create_welcome_card(self.chat)

    def attach_file(self):
        filename = choose_file()

        if not filename:
            return

        self.attached_file = filename
        create_attachment_card(self.chat, filename)

    # -------------------------------------------------
    # AI Helpers
    # -------------------------------------------------

    def preview_code_change(self, old_code, new_code):

        result = {
            "filename": (
                self.editor.current_file
                if self.editor
                else "Untitled"
            ),
            "old": old_code,
            "new": new_code
        }

        def apply(updated):
            if not self.editor:
                return

            self.editor.set_text(
                updated["new"]
            )

            if self.editor.current_file:
                self.editor.save_file()

        DiffViewer(
            self.app,
            result,
            apply
        )

    # -------------------------------------------------
    # Improve Current File
    # -------------------------------------------------

    def improve_editor_code(self, editor):

        code = editor.get_text()

        if not code.strip():
            return

        thinking = add_system_bubble(
            self.chat,
            "🤖 Future AI is improving your code..."
        )

        task = None

        if self.right_sidebar:
            task = self.right_sidebar.start_task(
                "✨ Improving current file..."
            )

        self.app.update()

        improved = self.ai_actions.improve_code(code)

        if thinking.winfo_exists():
            thinking.destroy()

        if task:
            self.right_sidebar.update_task(
                task,
                1.0
            )

            self.right_sidebar.finish_task(task)

            self.right_sidebar.set_status(
                "🟢 Ready"
            )

        if not improved:
            return

        self.preview_code_change(
            code,
            improved
        )

    # -------------------------------------------------
    # Command Palette
    # -------------------------------------------------

    def run_ai_action(self, action):
        if self.editor is None:
            return

        code = self.editor.get_text()

        if not code.strip():
            return

        self.editor.set_status("Future AI is working...")
        reply = self.ai_actions.run_action(action, code)
        self.editor.set_status("Ready")

        if not reply:
            return

        replace_actions = {
            "improve",
            "optimize",
            "clean",
            "debug",
            "comments",
            "async",
            "refactor",
            "translate"
        }

        if action in replace_actions:
            self.preview_code_change(code, reply)
        else:
            add_ai_bubble(self.chat, reply)

    # -------------------------------------------------
    # Project AI
    # -------------------------------------------------

    def ask_project_ai(self, question):
        return self.ai_actions.ask_project(question)

    # -------------------------------------------------
    # Error Assistant
    # -------------------------------------------------

    def explain_error(self, error):
        thinking = add_system_bubble(
            self.chat,
            "🤖 Future AI is analyzing the error..."
        )

        task = None

        if self.right_sidebar:
            task = self.right_sidebar.start_task(
                "🐞 Explaining Python error..."
            )

        self.app.update()

        reply = self.ai_actions.explain_error(error)

        if thinking.winfo_exists():
            thinking.destroy()

        if not reply:
            reply = "I couldn't analyze the error."

        add_ai_bubble(
            self.chat,
            reply
        )

        if task:
            self.right_sidebar.finish_task(task)
            self.right_sidebar.set_status(
                "🟢 Ready"
            )

    # -------------------------------------------------
    # AI Agent
    # -------------------------------------------------

    def inline_ai(self, event=None):

        if not self.editor:
            return

        InlinePrompt(
            self.app,
            self.run_inline_ai
        )

    def run_inline_ai(self, prompt):

        if not self.editor:
            return

        selected = self.editor.get_selected_text()

        if not selected:

            messagebox.showinfo(
                "Future AI",
                "Please select some code first."
            )

            return

        self.right_sidebar.set_status(
            "🤖 Editing selection..."
        )

        conversation = [

            {
                "role": "system",
                "content":
                (
                    "You are an expert software engineer.\n"
                    "Modify ONLY the selected code.\n"
                    "Return ONLY the updated code."
                )
            },

            {
                "role": "user",
                "content":
                    f"Instruction:\n{prompt}\n\n"
                    f"Selected Code:\n\n{selected}"
            }

        ]

        new_code = self.ai.chat(conversation)

        self.right_sidebar.set_status("🟢 Ready")

        if not new_code:
            return

        result = {

            "filename": self.editor.current_file,

            "old": selected,

            "new": new_code

        }

        def apply(updated):

            self.editor.replace_selected_text(
                updated["new"]
            )

            self.editor.save_file()

        DiffViewer(

            self.app,

            result,

            apply

        )

    def run_agent(self, request):

        if not self.right_sidebar:
            return

        # --------------------------------
        # Reset Timeline
        # --------------------------------

        self.right_sidebar.tasks.timeline.clear()

        analyze = self.right_sidebar.tasks.timeline.add_step(
            "Analyze Request"
        )

        index = self.right_sidebar.tasks.timeline.add_step(
            "Index Project"
        )

        plan = self.right_sidebar.tasks.timeline.add_step(
            "Plan Changes"
        )

        edit = self.right_sidebar.tasks.timeline.add_step(
            "Generate Code"
        )

        review = self.right_sidebar.tasks.timeline.add_step(
            "Review Changes"
        )

        apply = self.right_sidebar.tasks.timeline.add_step(
            "Apply Changes"
        )

        finished = self.right_sidebar.tasks.timeline.add_step(
            "Finished"
        )

        # --------------------------------
        # Analyze
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(analyze)
        self.app.update()

        self.right_sidebar.tasks.timeline.finish(analyze)

        # --------------------------------
        # Index
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(index)
        self.app.update()

        self.right_sidebar.tasks.timeline.finish(index)

        # --------------------------------
        # Plan
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(plan)
        self.app.update()

        results = self.agent.run(request)

        if not results:
            self.right_sidebar.tasks.timeline.error(plan)
            return

        self.right_sidebar.tasks.timeline.finish(plan)

        # --------------------------------
        # Generate
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(edit)
        self.app.update()

        self.right_sidebar.tasks.timeline.finish(edit)

        # --------------------------------
        # Review
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(review)
        self.app.update()

        AgentReview(
            self.app,
            results,
            self.review_change,
            self.apply_agent_changes
        )

        self.right_sidebar.tasks.timeline.finish(review)

        # --------------------------------
        # Apply
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(apply)
        self.app.update()

        self.right_sidebar.tasks.timeline.finish(apply)

        # --------------------------------
        # Done
        # --------------------------------

        self.right_sidebar.tasks.timeline.running(finished)
        self.app.update()

        self.right_sidebar.tasks.timeline.finish(finished)

        self.right_sidebar.set_status("🟢 Ready")

    def review_change(self, result):
        DiffViewer(
            self.app,
            result,
            lambda updated: self.project_editor.apply_results([updated])
        )

    def apply_agent_changes(self, results):
        for result in results:
            DiffViewer(
                self.app,
                result,
                lambda updated: self.project_editor.apply_results([updated])
            )

        add_ai_bubble(
            self.chat,
            f"✅ Future AI successfully updated {len(results)} file(s)."
        )

        try:
            if self.editor and self.editor.current_file:
                current = self.editor.current_file
                self.editor.open_file(current)
        except Exception as e:
            print("Editor Refresh:", e)

        if self.right_sidebar:
            self.right_sidebar.set_status("🟢 Ready")

    def delete_chat(self, chat_id):
        answer = messagebox.askyesno(
            "Delete Chat",
            "Delete this conversation?"
        )

        if not answer:
            return

        delete_chat(chat_id)

        if self.current_chat == chat_id:
            self.current_chat = None
            self.attached_file = None
            self.clear_chat()
            create_welcome_card(self.chat)
            self.welcome_cleared = False
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

            if hasattr(self, "layout") and hasattr(self.layout, "center"):
                self.layout.center.show_chat()

            self.welcome_cleared = True

        add_user_bubble(self.chat, user)

        if self.current_chat is None:
            self.current_chat = create_chat("New Chat")
            if self.sidebar:
                self.sidebar.refresh()

        add_message(self.current_chat, "user", user)

        chats = load_chats()

        if len(chats[self.current_chat]["messages"]) == 1:
            rename_chat(self.current_chat, user)
            if self.sidebar:
                self.sidebar.refresh()
            chats = load_chats()

        conversation = []

        for msg in chats[self.current_chat]["messages"]:
            conversation.append({
                "role": msg["role"],
                "content": msg["text"]
            })

        if self.attached_file:
            file_text = read_file(self.attached_file)

            if file_text:
                file_text = file_text[:5000]
                conversation.append({
                    "role": "system",
                    "content":
                        f"The user attached '{os.path.basename(self.attached_file)}'.\n\n"
                        f"Contents:\n\n{file_text}"
                })
            else:
                conversation.append({
                    "role": "system",
                    "content":
                        f"The attached file '{os.path.basename(self.attached_file)}' could not be read."
                })

        thinking = add_system_bubble(
            self.chat,
            "Future AI is thinking..."
        )

        self.app.update()

        workspace = self.context_retriever.build_context(user)

        for item in workspace:
            conversation.append({
                "role": "system",
                "content":
                    f"Relevant Project File\n\n"
                    f"File:\n{item['file']}\n\n"
                    f"Symbol:\n{item['symbol']}\n\n"
                    f"Type:\n{item['type']}\n\n"
                    f"Line:\n{item['line']}\n\n"
                    f"Code:\n\n{item['content']}"
            })

        bubble = add_streaming_bubble(self.chat)
        reply = ""
        task = None

        if self.right_sidebar:
            task = self.right_sidebar.start_task(
                "🤖 Future AI is answering..."
            )

        try:
            for chunk in self.ai.stream_chat(conversation):
                if thinking.winfo_exists():
                    thinking.destroy()

                bubble.update(chunk)
                reply += chunk

                if task:
                    progress = min(len(reply) / 800, 0.95)
                    self.right_sidebar.update_task(task, progress)

                self.app.update()

            bubble.finish()

            if task:
                self.right_sidebar.finish_task(task)
                self.right_sidebar.set_status("🟢 Ready")

        except Exception as e:
            print("Streaming Error:", e)

            if thinking.winfo_exists():
                thinking.destroy()

            reply = self.ai.chat(conversation)

            if reply:
                bubble.update(reply)
                bubble.finish()

            if task:
                self.right_sidebar.finish_task(task)
                self.right_sidebar.set_status("🟢 Ready")

        if not reply:
            answer = simpledialog.askstring(
                "Teach Future AI",
                f"What should I answer?\n\n{user}"
            )

            if answer:
                self.ai.learn(user, answer)
                reply = "Thanks! I learned something new."
                bubble.update(reply)
                bubble.finish()
            else:
                reply = "Okay."
                bubble.update(reply)
                bubble.finish()

        add_message(
            self.current_chat,
            "assistant",
            reply
        )

        message_box.delete(0, "end")

    # -------------------------------------------------
    # Open Symbol
    # -------------------------------------------------

    def open_symbol(self, filename, line):

        if not self.editor:
            return

        self.editor.open_file(filename)

        try:
            widget = self.editor.editor_widget()

            widget.mark_set(
                "insert",
                f"{line}.0"
            )

            widget.see(
                f"{line}.0"
            )

            widget.focus_set()

        except Exception as e:
            print("Open Symbol:", e)
