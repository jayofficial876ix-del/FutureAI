from services.project_indexer import ProjectIndexer


class ProjectContext:

    def __init__(self):
        self.indexer = ProjectIndexer()

    # --------------------------------

    def load_project(self, project):
        print("📂 Building Project Index...")
        self.indexer.build(project)
        print("✅ Project indexed.")

    # --------------------------------

    def build_prompt(self, question):
        matches = self.indexer.search(question)

        if not matches:
            print("No direct matches found.")
            print("Using fallback files.")
            matches = list(
                self.indexer.index.keys()
            )[:5]

        context = self.indexer.get_context(matches)

        return [
            {
                "role": "system",
                "content":
                (
                    "You are Future AI.\n"
                    "You are an expert software engineer.\n"
                    "Answer questions using ONLY the supplied project files.\n"
                    "Never invent files, functions, or code.\n"
                    "If the answer cannot be found, clearly say so.\n"
                    "Be concise and technical."
                )
            },
            {
                "role": "system",
                "content":
                (
                    "PROJECT CONTEXT\n"
                    "====================\n\n"
                    f"{context}"
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
