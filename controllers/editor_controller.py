from gui.diff_viewer import DiffViewer
from gui.inline_prompt import InlinePrompt
from tkinter import messagebox


class EditorController:

    def __init__(
        self,
        app,
        editor,
        ai_actions,
        ai_engine,
        right_sidebar,
        project_editor
    ):

        self.app = app
        self.editor = editor
        self.ai_actions = ai_actions
        self.ai = ai_engine
        self.right_sidebar = right_sidebar
        self.project_editor = project_editor

    # --------------------------------

    def preview(self, old_code, new_code):

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

            self.editor.set_text(
                updated["new"]
            )

            self.editor.save_file()

        DiffViewer(
            self.app,
            result,
            apply
        )

    # --------------------------------

    def improve_current_file(self):

        code = self.editor.get_text()

        if not code.strip():
            return

        improved = self.ai_actions.improve_code(
            code
        )

        if improved:

            self.preview(
                code,
                improved
            )

    # --------------------------------

    def inline_prompt(self):

        InlinePrompt(

            self.app,

            self.inline_edit

        )

    # --------------------------------

    def inline_edit(self, instruction):

        selected = self.editor.get_selected_text()

        if not selected:

            messagebox.showinfo(

                "Future AI",

                "Please select some code first."

            )

            return

        conversation = [

            {

                "role": "system",

                "content":

                    (
                        "Modify ONLY the selected code.\n"
                        "Return ONLY updated code."
                    )

            },

            {

                "role": "user",

                "content":

                    f"Instruction:\n{instruction}\n\n"

                    f"Code:\n{selected}"

            }

        ]

        new_code = self.ai.chat(
            conversation
        )

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
