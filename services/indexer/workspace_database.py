import sqlite3


class WorkspaceDatabase:

    def __init__(self, database="workspace.db"):

        self.connection = sqlite3.connect(database)

        self.cursor = self.connection.cursor()

        self.create_tables()

    # --------------------------------

    def create_tables(self):

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS files(

                id INTEGER PRIMARY KEY,

                path TEXT UNIQUE,

                content TEXT

            )

        """)

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS symbols(

                id INTEGER PRIMARY KEY,

                name TEXT,

                type TEXT,

                file TEXT,

                line INTEGER

            )

        """)

        self.connection.commit()

    # --------------------------------

    def clear(self):

        self.cursor.execute("DELETE FROM files")

        self.cursor.execute("DELETE FROM symbols")

        self.connection.commit()

    # --------------------------------

    def add_file(self, path, content):

        self.cursor.execute(

            """

            INSERT OR REPLACE INTO files(path,content)

            VALUES(?,?)

            """,

            (path, content)

        )

        self.connection.commit()

    # --------------------------------

    def add_symbol(

        self,

        name,

        symbol_type,

        file,

        line

    ):

        self.cursor.execute(

            """

            INSERT INTO symbols(

                name,

                type,

                file,

                line

            )

            VALUES(?,?,?,?)

            """,

            (

                name,

                symbol_type,

                file,

                line

            )

        )

        self.connection.commit()

    # --------------------------------

    def search_symbol(self, name):

        self.cursor.execute(

            """

            SELECT

                name,

                type,

                file,

                line

            FROM symbols

            WHERE name LIKE ?

            """,

            (f"%{name}%",)

        )

        return self.cursor.fetchall()
