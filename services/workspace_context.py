import os


class WorkspaceContext:

    def build(
        self,
        editor,
        terminal=None,
        open_files=None,
        git=None
    ):

        context = []

        # --------------------------------
        # Current File
        # --------------------------------

        if getattr(editor, "current_file", None):

            context.append({

                "role": "system",

                "content":
                    (
                        f"Current file:\n"
                        f"{os.path.basename(editor.current_file)}\n\n"
                        f"{editor.get_text()}"
                    )

            })

        # --------------------------------
        # Open Files
        # --------------------------------

        if open_files:

            names = [

                os.path.basename(f)

                for f in open_files

            ]

            context.append({

                "role": "system",

                "content":
                    (
                        "Open files:\n\n"
                        + "\n".join(names)
                    )

            })

        # --------------------------------
        # Selected Code
        # --------------------------------

        try:

            widget = editor.editor_widget()

            selected = widget.get(
                "sel.first",
                "sel.last"
            )

            if selected.strip():

                context.append({

                    "role": "system",

                    "content":
                        (
                            "Selected code:\n\n"
                            + selected
                        )

                })

        except Exception:

            pass

        # --------------------------------
        # Terminal Output
        # --------------------------------

        if terminal:

            try:

                output = terminal.get_output()

                if output.strip():

                    context.append({

                        "role": "system",

                        "content":
                            (
                                "Recent terminal output:\n\n"
                                + output[-4000:]
                            )

                    })

            except Exception:

                pass

        # --------------------------------
        # Git Status
        # --------------------------------

        if git:

            try:

                changes = git.changed_files()

                if changes:

                    lines = [

                        f"{status}  {filename}"

                        for status, filename in changes

                    ]

                    context.append({

                        "role": "system",

                        "content":
                            (
                                "Git changes:\n\n"
                                + "\n".join(lines)
                            )

                    })

            except Exception:

                pass

        return context
