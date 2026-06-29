import os
from tkinter import filedialog


def import_folder():

    folder = filedialog.askdirectory(
        title="Select a Project Folder"
    )

    if not folder:
        return None

    files = []

    for root, _, filenames in os.walk(folder):

        for filename in filenames:

            files.append(
                os.path.join(root, filename)
            )

    return {
        "name": os.path.basename(folder),
        "path": folder,
        "files": files
    }
