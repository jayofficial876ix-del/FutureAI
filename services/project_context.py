from services.project_indexer import ProjectIndexer


class ProjectContext:

    def __init__(self):
        self.indexer = ProjectIndexer()

    def load_project(self, project):
        self.indexer.build(project)

    def build_prompt(self, question):
        matches = self.indexer.search(question)

        if not matches:
            # Fall back to the first few files
            matches = list(self.indexer.index.keys())[:5]

        context = self.indexer.get_context(matches)

        return [
            {
                "role": "system",
                "content": (
                    "You are an expert software engineer.\n"
                    "Answer questions using ONLY the supplied project files."
                )
            },
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": question
            }
        ]
