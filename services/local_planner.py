import os


class LocalPlanner:

    def plan(self, request, project):

        request = request.lower()

        files = []

        keywords = []

        for word in request.replace(",", " ").split():

            word = word.strip()

            if len(word) > 2:
                keywords.append(word)

        for filename in project["files"]:

            name = os.path.basename(filename).lower()

            score = 0

            for keyword in keywords:

                if keyword in name:
                    score += 10

                try:

                    with open(
                        filename,
                        "r",
                        encoding="utf-8",
                        errors="ignore"
                    ) as f:

                        code = f.read().lower()

                    score += code.count(keyword)

                except Exception:
                    pass

            if score > 0:

                files.append(
                    (score, filename)
                )

        files.sort(reverse=True)

        return [

            os.path.basename(f)

            for _, f in files[:10]

        ]
