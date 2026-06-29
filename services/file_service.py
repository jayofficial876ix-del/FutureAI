import os


def load_text_file(filename):

    if not os.path.exists(filename):
        return ""

    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def save_text_file(filename, text):

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
