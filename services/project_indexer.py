import os


TEXT_EXTENSIONS = {
    ".py",
    ".txt",
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".html",
    ".css",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".xml"
}


class ProjectIndexer:

    def __init__(self):

        self.index = {}

    def build(self, project):

        self.index.clear()

        for filename in project["files"]:

            ext = os.path.splitext(filename)[1].lower()

            if ext not in TEXT_EXTENSIONS:
                continue

            try:

                with open(
                    filename,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    self.index[filename] = f.read()

            except Exception:

                continue

    def search(self, text):

        results = []

        text = text.lower()

        for filename, contents in self.index.items():

            if text in contents.lower():

                results.append(filename)

        return results

    def get_file(self, filename):

        return self.index.get(
            filename,
            ""
        )

    def get_context(self, filenames):

        context = []

        for filename in filenames:

            context.append(
                f"\n===== {os.path.basename(filename)} =====\n"
            )

            context.append(
                self.get_file(filename)
            )

        return "\n".join(context)
