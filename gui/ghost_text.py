class GhostText:

    def __init__(self, editor):

        self.editor = editor

        self.suggestion = ""

        self.start = None
        self.end = None

        self.editor.tag_configure(

            "ghost",

            foreground="#666666"

        )

    # --------------------------------

    def show(self, text):

        self.clear()

        if not text:
            return

        self.suggestion = text

        self.start = self.editor.index(
            "insert"
        )

        self.editor.insert(

            self.start,

            text,

            "ghost"

        )

        self.end = self.editor.index(

            f"{self.start}+{len(text)}c"

        )

        # Put the cursor back where it was
        self.editor.mark_set(

            "insert",

            self.start

        )

    # --------------------------------

    def clear(self):

        if not self.suggestion:
            return

        try:

            self.editor.delete(

                self.start,

                self.end

            )

        except Exception:

            pass

        self.suggestion = ""

        self.start = None
        self.end = None

    # --------------------------------

    def accept(self):

        if not self.suggestion:
            return

        self.editor.tag_remove(

            "ghost",

            self.start,

            self.end

        )

        self.editor.mark_set(

            "insert",

            self.end

        )

        self.suggestion = ""

        self.start = None
        self.end = None

    # --------------------------------

    def has_suggestion(self):

        return bool(self.suggestion)
