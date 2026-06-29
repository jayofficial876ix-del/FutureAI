import difflib


def generate_diff(old_code, new_code):

    old_lines = old_code.splitlines()
    new_lines = new_code.splitlines()

    return "\n".join(

        difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile="Current",
            tofile="AI Suggestion",
            lineterm=""
        )

    )
