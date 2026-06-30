class LocalCoder:

    def generate(self, request, filename, code):

        request = request.lower()

        # --------------------------------
        # Add comment
        # --------------------------------

        if "comment" in request:

            comment = "# Created by Future AI\n"

            if not code.startswith(comment):
                return comment + code

        # --------------------------------
        # Add docstring
        # --------------------------------

        if "docstring" in request:

            lines = code.splitlines()
            output = []

            for line in lines:
                output.append(line)

                if line.strip().startswith("def "):
                    indent = " " * (len(line) - len(line.lstrip()) + 4)
                    output.append(indent + '"""TODO: Description."""')

            return "\n".join(output)

        # --------------------------------
        # Add logging
        # --------------------------------

        if "logging" in request:

            lines = code.splitlines()
            output = []
            imported = False

            for line in lines:
                if line.strip() == "import logging":
                    imported = True
                output.append(line)

            if not imported:
                output.insert(0, "import logging")

            return "\n".join(output)

        # --------------------------------
        # Default
        # --------------------------------

        return code
