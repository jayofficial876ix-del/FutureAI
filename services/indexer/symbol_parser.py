import ast
import os


class SymbolParser:

    def parse(self, filename):

        symbols = []

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                source = file.read()

            tree = ast.parse(source)

        except Exception:

            return symbols

        for node in ast.walk(tree):

            # -------------------------
            # Classes
            # -------------------------

            if isinstance(
                node,
                ast.ClassDef
            ):

                symbols.append({

                    "name": node.name,

                    "type": "class",

                    "file": filename,

                    "line": node.lineno

                })

            # -------------------------
            # Functions
            # -------------------------

            elif isinstance(
                node,
                ast.FunctionDef
            ):

                symbols.append({

                    "name": node.name,

                    "type": "function",

                    "file": filename,

                    "line": node.lineno

                })

            # -------------------------
            # Async Functions
            # -------------------------

            elif isinstance(
                node,
                ast.AsyncFunctionDef
            ):

                symbols.append({

                    "name": node.name,

                    "type": "async function",

                    "file": filename,

                    "line": node.lineno

                })

            # -------------------------
            # Imports
            # -------------------------

            elif isinstance(
                node,
                ast.Import
            ):

                for alias in node.names:

                    symbols.append({

                        "name": alias.name,

                        "type": "import",

                        "file": filename,

                        "line": node.lineno

                    })

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                module = node.module or ""

                for alias in node.names:

                    symbols.append({

                        "name": f"{module}.{alias.name}",

                        "type": "import",

                        "file": filename,

                        "line": node.lineno

                    })

        return symbols
