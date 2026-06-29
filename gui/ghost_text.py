class GhostText:

    def __init__(self, editor):

        self.editor = editor
        self.suggestion = ""

        self.editor.tag_config(
            "ghost",
            foreground="#666666"
        )

    # --------------------------------

    def show(self, text):

        self.clear()

        if not text:
            return

        self.suggestion = text

        index = self.editor.index("insert")

        self.editor.insert(
            index,
            text,
            "ghost"
        )

        self.editor.mark_set(
            "insert",
            index
        )

    # --------------------------------

    def clear(self):

        if not self.suggestion:
            return

        start = self.editor.index("insert")

        end = f"{start}+{len(self.suggestion)}c"

        try:

            self.editor.delete(
                start,
                end
            )

        except Exception:
            pass

        self.suggestion = ""

    # --------------------------------

    def accept(self):

        if not self.suggestion:
            return

        index = self.editor.index("insert")

        end = f"{index}+{len(self.suggestion)}c"

        self.editor.tag_remove(
            "ghost",
            index,
            end
        )

        self.editor.mark_set(
            "insert",
            end
        )

        self.suggestion = ""
