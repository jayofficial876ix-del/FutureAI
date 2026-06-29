import keyword
import re


PYTHON_KEYWORDS = keyword.kwlist


def highlight(editor):

    # Remove old tags
    for tag in editor.tag_names():
        editor.tag_delete(tag)

    # Configure colors
    editor.tag_config(
        "keyword",
        foreground="#4FC3F7"
    )

    editor.tag_config(
        "string",
        foreground="#A5D6A7"
    )

    editor.tag_config(
        "comment",
        foreground="#9E9E9E"
    )

    editor.tag_config(
        "number",
        foreground="#FFB74D"
    )

    text = editor.get(
        "1.0",
        "end-1c"
    )

    # ---------------------
    # Keywords
    # ---------------------

    for word in PYTHON_KEYWORDS:

        for match in re.finditer(
            rf"\b{word}\b",
            text
        ):

            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"

            editor.tag_add(
                "keyword",
                start,
                end
            )

    # ---------------------
    # Strings
    # ---------------------

    for match in re.finditer(
        r'".*?"|\'.*?\'',
        text
    ):

        editor.tag_add(
            "string",
            f"1.0+{match.start()}c",
            f"1.0+{match.end()}c"
        )

    # ---------------------
    # Comments
    # ---------------------

    for match in re.finditer(
        r"#.*",
        text
    ):

        editor.tag_add(
            "comment",
            f"1.0+{match.start()}c",
            f"1.0+{match.end()}c"
        )

    # ---------------------
    # Numbers
    # ---------------------

    for match in re.finditer(
        r"\b\d+\b",
        text
    ):

        editor.tag_add(
            "number",
            f"1.0+{match.start()}c",
            f"1.0+{match.end()}c"
        )
