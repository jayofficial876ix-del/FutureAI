from services.tool_router import ToolRouter


class ToolManager:

    def __init__(self):

        self.router = ToolRouter()

    # --------------------------------

    def register_defaults(
        self,
        ai_actions=None,
        git=None,
        terminal=None,
        ai_agent=None
    ):

        if ai_actions:

            self.router.register(
                "improve_code",
                ai_actions.improve_code
            )

            self.router.register(
                "inline_edit",
                ai_actions.inline_edit
            )

            self.router.register(
                "explain_code",
                ai_actions.explain_code
            )

            self.router.register(
                "generate_tests",
                ai_actions.generate_tests
            )

            self.router.register(
                "project_chat",
                ai_actions.ask_project
            )

        if git:

            self.router.register(
                "git_commit",
                git.commit
            )

            self.router.register(
                "git_push",
                git.push
            )

            self.router.register(
                "git_pull",
                git.pull
            )

        if terminal:

            self.router.register(
                "terminal_output",
                terminal.get_output
            )

        if ai_agent:

            self.router.register(
                "ai_agent",
                ai_agent.run
            )

    # --------------------------------

    def execute(self, tool, *args, **kwargs):

        return self.router.execute(
            tool,
            *args,
            **kwargs
        )

    # --------------------------------

    def list_tools(self):

        return self.router.list_tools()
