import ast


class DiagnosticsEngine:

    # --------------------------------

    def analyze(self, code):

        diagnostics = []

        try:

            ast.parse(code)

        except SyntaxError as e:

            diagnostics.append({

                "type": "Syntax Error",

                "line": e.lineno,

                "column": e.offset,

                "message": e.msg

            })

        return diagnostics