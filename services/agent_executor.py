import os


class AgentExecutor:

    def __init__(self, ai, planner):

        self.ai = ai
        self.planner = planner

    # ------------------------------------------

    def execute(self, request):

        print("\n")
        print("=" * 60)
        print("FUTURE AI AGENT")
        print("=" * 60)
        print("Request:")
        print(request)
        print("=" * 60)

        # ----------------------------
        # Ask planner
        # ----------------------------

        plan = self.planner.plan(request)

        print("\nPlanner returned:\n")

        print(plan)

        print("\n" + "=" * 60)

        if not plan:

            print("Planner returned nothing.")
            return None

        # ----------------------------
        # Parse planner output
        # ----------------------------

        files = []

        for line in plan.splitlines():

            line = line.strip()

            if not line:
                continue

            if line[0].isdigit():

                try:
                    line = line.split(".", 1)[1].strip()
                except Exception:
                    pass

            if "." not in line:
                continue

            files.append(line)

        print("Files selected by planner:\n")

        if not files:

            print("No files were detected.")

        else:

            for f in files:
                print(" -", f)

        print("=" * 60)
        print()

        return files
