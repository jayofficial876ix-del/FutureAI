TRACEBACK_WORDS = [
    "Traceback",
    "Error",
    "Exception",
    "SyntaxError",
    "TypeError",
    "AttributeError",
    "NameError",
    "ValueError",
    "ImportError",
    "ModuleNotFoundError",
    "IndexError",
    "KeyError",
    "RuntimeError",
    "FileNotFoundError",
    "PermissionError",
    "RecursionError",
    "ZeroDivisionError"
]


def contains_error(output):

    for word in TRACEBACK_WORDS:

        if word in output:
            return True

    return False


def extract_error(output):

    lines = output.splitlines()

    start = 0

    for i, line in enumerate(lines):

        if "Traceback" in line:
            start = i
            break

    return "\n".join(lines[start:])
