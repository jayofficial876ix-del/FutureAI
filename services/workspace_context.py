import os


class WorkspaceContext:

    def build(
        self,
        editor,
        terminal=None,
        open_files=None
    ):

        context = []

        # -----------------------
        # Current File
        # -----------------------

        if editor.current_file:

            context.append({

                "role": "system",

                "content":
                    f"Current file: "
                    f"{os.path.basename(editor.current_file)}\n\n"
                    f"{editor.get_text()}"

            })

        # -----------------------
        # Open Files
        # -----------------------

        if open_files:

            names = [
                os.path.basename(f)
                for f in open_files
            ]

            context.append({

                "role": "system",

                "content":
                    "Open files:\n"
                    + "\n".join(names)

            })

        # -----------------------
        # Selected Code
        # -----------------------

        try:

            widget = editor.editor_widget()

            selected = widget.get(
                "sel.first",
                "sel.last"
            )

            if selected:

                context.append({

                    "role": "system",

                    "content":
                        "Selected code:\n\n"
                        + selected

                })

        except Exception:

            pass

        # -----------------------
        # Terminal
        # -----------------------

        if terminal:

            try:

                output = terminal.get_output()

                if output.strip():

                    context.append({

                        "role": "system",

                        "content":
                            "Recent terminal output:\n\n"
                            + output[-4000:]

                    })

            except Exception:

                pass

        return context
