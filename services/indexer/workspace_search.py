from services.indexer.workspace_database import WorkspaceDatabase


class WorkspaceSearch:

    def __init__(self):

        self.db = WorkspaceDatabase()

    # --------------------------------
    # Generic Symbol Search
    # --------------------------------

    def find_symbol(self, name):

        return self.db.search_symbol(name)

    # --------------------------------
    # Functions
    # --------------------------------

    def find_functions(self):

        self.db.cursor.execute(
            """
            SELECT
                name,
                file,
                line
            FROM symbols
            WHERE type='function'
            ORDER BY name
            """
        )

        return self.db.cursor.fetchall()

    # --------------------------------
    # Classes
    # --------------------------------

    def find_classes(self):

        self.db.cursor.execute(
            """
            SELECT
                name,
                file,
                line
            FROM symbols
            WHERE type='class'
            ORDER BY name
            """
        )

        return self.db.cursor.fetchall()

    # --------------------------------
    # Async Functions
    # --------------------------------

    def find_async_functions(self):

        self.db.cursor.execute(
            """
            SELECT
                name,
                file,
                line
            FROM symbols
            WHERE type='async function'
            ORDER BY name
            """
        )

        return self.db.cursor.fetchall()

    # --------------------------------
    # Imports
    # --------------------------------

    def find_imports(self):

        self.db.cursor.execute(
            """
            SELECT
                name,
                file,
                line
            FROM symbols
            WHERE type='import'
            ORDER BY name
            """
        )

        return self.db.cursor.fetchall()

    # --------------------------------
    # Files
    # --------------------------------

    def find_file(self, filename):

        self.db.cursor.execute(
            """
            SELECT
                path
            FROM files
            WHERE path LIKE ?
            """,
            (f"%{filename}%",)
        )

        return self.db.cursor.fetchall()

    # --------------------------------
    # File Content
    # --------------------------------

    def file_content(self, filename):

        self.db.cursor.execute(
            """
            SELECT
                content
            FROM files
            WHERE path = ?
            """,
            (filename,)
        )

        result = self.db.cursor.fetchone()

        if result:
            return result[0]

        return ""

    # --------------------------------
    # Project Statistics
    # --------------------------------

    def statistics(self):

        self.db.cursor.execute(
            "SELECT COUNT(*) FROM files"
        )

        files = self.db.cursor.fetchone()[0]

        self.db.cursor.execute(
            "SELECT COUNT(*) FROM symbols"
        )

        symbols = self.db.cursor.fetchone()[0]

        self.db.cursor.execute(
            "SELECT COUNT(*) FROM symbols WHERE type='class'"
        )

        classes = self.db.cursor.fetchone()[0]

        self.db.cursor.execute(
            "SELECT COUNT(*) FROM symbols WHERE type='function'"
        )

        functions = self.db.cursor.fetchone()[0]

        self.db.cursor.execute(
            "SELECT COUNT(*) FROM symbols WHERE type='async function'"
        )

        async_functions = self.db.cursor.fetchone()[0]

        self.db.cursor.execute(
            "SELECT COUNT(*) FROM symbols WHERE type='import'"
        )

        imports = self.db.cursor.fetchone()[0]

        return {
            "files": files,
            "symbols": symbols,
            "classes": classes,
            "functions": functions,
            "async_functions": async_functions,
            "imports": imports
        }
