import os

from services.indexer.workspace_database import WorkspaceDatabase
from services.indexer.symbol_parser import SymbolParser


class WorkspaceIndexer:

    def __init__(self):

        self.database = WorkspaceDatabase()

        self.parser = SymbolParser()

    # --------------------------------

    def index_project(self, project_path):

        self.database.clear()

        for root, _, files in os.walk(project_path):

            for filename in files:

                if not filename.endswith(".py"):
                    continue

                path = os.path.join(
                    root,
                    filename
                )

                self.index_file(path)

    # --------------------------------

    def index_file(self, filename):

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                source = file.read()

        except Exception:

            return

        self.database.add_file(
            filename,
            source
        )

        symbols = self.parser.parse(
            filename
        )

        for symbol in symbols:

            self.database.add_symbol(

                symbol["name"],

                symbol["type"],

                symbol["file"],

                symbol["line"]

            )

    # --------------------------------

    def rebuild(self, project):

        print("Indexing project...")

        self.index_project(project)

        print("Workspace index complete.")
