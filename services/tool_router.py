"""Simple ToolRouter for registering and executing named callables."""


class ToolRouter:

    def __init__(self):
        self.tools = {}

    # --------------------------------

    def register(self, name, handler):
        self.tools[name] = handler

    # --------------------------------

    def has_tool(self, name):
        return name in self.tools

    # --------------------------------

    def list_tools(self):
        return sorted(self.tools.keys())

    # --------------------------------

    def execute(self, name, *args, **kwargs):
        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")

        return self.tools[name](*args, **kwargs)
