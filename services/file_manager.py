from tkinter import filedialog
import os


SUPPORTED_FILES = [
    (
        "All Supported Files",
        "*.pdf *.docx *.txt *.png *.jpg *.jpeg *.py *.html *.css *.js"
    ),
    ("PDF Files", "*.pdf"),
    ("Word Documents", "*.docx"),
    ("Text Files", "*.txt"),
    ("Python Files", "*.py"),
    ("Images", "*.png *.jpg *.jpeg"),
    ("HTML Files", "*.html"),
    ("CSS Files", "*.css"),
    ("JavaScript Files", "*.js"),
    ("All Files", "*.*")
]


def choose_file():

    return filedialog.askopenfilename(
        title="Choose a File",
        filetypes=SUPPORTED_FILES
    )


def choose_folder():

    folder = filedialog.askdirectory(
        title="Choose a Project Folder"
    )

    if not folder:
        return None

    files = []

    supported = (
        ".py",
        ".html",
        ".css",
        ".js",
        ".txt",
        ".md",
        ".json",
        ".xml",
        ".yml",
        ".yaml",
        ".pdf",
        ".docx"
    )

    for root, _, filenames in os.walk(folder):

        for filename in filenames:

            if filename.lower().endswith(supported):

                files.append(
                    os.path.join(root, filename)
                )

    return {
        "name": os.path.basename(folder),
        "path": folder,
        "files": files
    }
