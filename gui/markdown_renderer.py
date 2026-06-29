import re


def render_markdown(text):

    if not text:
        return ""

    # ----------------------------------
    # Code Blocks
    # ----------------------------------

    def code_block(match):

        language = match.group(1).strip()
        code = match.group(2).rstrip()

        title = "Code"

        if language:
            title = language.capitalize()

        return (
            f"\n"
            f"────────── {title} ──────────\n"
            f"{code}\n"
            f"─────────────────────────────\n"
        )

    text = re.sub(
        r"```(\w*)\n([\s\S]*?)```",
        code_block,
        text
    )

    # ----------------------------------
    # Inline Code
    # ----------------------------------

    text = re.sub(
        r"`([^`]+)`",
        r"[\1]",
        text
    )

    # ----------------------------------
    # Headings
    # ----------------------------------

    text = re.sub(
        r"^### (.*)$",
        r"\n\1\n----------------",
        text,
        flags=re.MULTILINE
    )

    text = re.sub(
        r"^## (.*)$",
        r"\n\1\n================",
        text,
        flags=re.MULTILINE
    )

    text = re.sub(
        r"^# (.*)$",
        r"\n\1\n==============================",
        text,
        flags=re.MULTILINE
    )

    # ----------------------------------
    # Bold
    # ----------------------------------

    text = re.sub(
        r"\*\*(.*?)\*\*",
        r"\1",
        text
    )

    # ----------------------------------
    # Italic
    # ----------------------------------

    text = re.sub(
        r"\*(.*?)\*",
        r"\1",
        text
    )

    # ----------------------------------
    # Block Quotes
    # ----------------------------------

    text = re.sub(
        r"^> (.*)$",
        r"│ \1",
        text,
        flags=re.MULTILINE
    )

    # ----------------------------------
    # Bullet Lists
    # ----------------------------------

    text = re.sub(
        r"^\s*[-*]\s+",
        "• ",
        text,
        flags=re.MULTILINE
    )

    # ----------------------------------
    # Numbered Lists
    # ----------------------------------

    text = re.sub(
        r"^\d+\.\s+",
        "• ",
        text,
        flags=re.MULTILINE
    )

    # ----------------------------------
    # Horizontal Rules
    # ----------------------------------

    text = re.sub(
        r"^---+$",
        "────────────────────────────",
        text,
        flags=re.MULTILINE
    )

    # ----------------------------------
    # Remove Excess Blank Lines
    # ----------------------------------

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()
