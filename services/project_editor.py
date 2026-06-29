import os
import shutil


class ProjectEditor:

    def __init__(self):

        pass

    # -------------------------
    # Read
    # -------------------------

    def read(self, filename):

        try:

            with open(
                filename,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                return f.read()

        except Exception:

            return ""

    # -------------------------
    # Write
    # -------------------------

    def write(self, filename, text):

        directory = os.path.dirname(filename)

        if directory:

            os.makedirs(
                directory,
                exist_ok=True
            )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

    # -------------------------
    # Backup
    # -------------------------

    def backup(self, filename):

        if not os.path.exists(filename):
            return

        shutil.copy2(
            filename,
            filename + ".bak"
        )

    # -------------------------
    # Restore
    # -------------------------

    def restore(self, filename):

        backup = filename + ".bak"

        if os.path.exists(backup):

            shutil.copy2(
                backup,
                filename
            )

    # -------------------------
    # Apply Agent Results
    # -------------------------

    def apply_results(self, results):

        for result in results:

            self.backup(
                result["filename"]
            )

            self.write(
                result["filename"],
                result["new"]
            )
