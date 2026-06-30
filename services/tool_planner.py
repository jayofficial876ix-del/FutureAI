class ToolPlanner:

    def choose(self, request):

        text = request.lower()

        # -----------------------------
        # Git
        # -----------------------------

        if "commit" in text:
            return "git_commit"

        if "push" in text:
            return "git_push"

        if "pull" in text:
            return "git_pull"

        # -----------------------------
        # Tests
        # -----------------------------

        if "test" in text:
            return "generate_tests"

        # -----------------------------
        # Explain
        # -----------------------------

        if "explain" in text:
            return "explain_code"

        # -----------------------------
        # Improve
        # -----------------------------

        if any(
            word in text
            for word in (
                "improve",
                "optimize",
                "refactor"
            )
        ):
            return "improve_code"

        # -----------------------------
        # Project
        # -----------------------------

        if any(
            word in text
            for word in (
                "project",
                "workspace",
                "where",
                "find"
            )
        ):
            return "project_chat"

        # -----------------------------
        # AI Agent
        # -----------------------------

        if any(
            word in text
            for word in (
                "every",
                "all files",
                "entire project",
                "rename",
                "logging"
            )
        ):
            return "ai_agent"

        return None
