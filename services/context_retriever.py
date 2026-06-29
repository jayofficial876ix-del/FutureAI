from services.indexer.workspace_search import WorkspaceSearch


class ContextRetriever:

    def __init__(self):
        self.search = WorkspaceSearch()

    # --------------------------------

    def build_context(self, question):
        context = []

        # --------------------------------
        # Search symbols
        # --------------------------------

        matches = self.search.find_symbol(question)

        for name, symbol_type, filename, line in matches:
            content = self.search.file_content(filename)

            if not content:
                continue

            context.append({
                "file": filename,
                "symbol": name,
                "type": symbol_type,
                "line": line,
                "content": content
            })

        return context
