import os


class GlobalSearch:

    def search(self, project_path, query):

        results = []

        if not query.strip():
            return results

        for root, _, files in os.walk(project_path):

            for filename in files:

                path = os.path.join(
                    root,
                    filename
                )

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8",
                        errors="ignore"
                    ) as f:

                        lines = f.readlines()

                except Exception:
                    continue

                for number, line in enumerate(lines, 1):

                    if query.lower() in line.lower():

                        results.append({

                            "file": path,

                            "line": number,

                            "text": line.strip()

                        })

        return results
