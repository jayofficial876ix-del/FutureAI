from services.tool_planner import ToolPlanner
from services.tool_manager import ToolManager


class AIAssistant:

    def __init__(self, tool_manager=None):

        self.planner = ToolPlanner()

        self.tool_manager = tool_manager or ToolManager()

    # --------------------------------

    def handle(self, request, *args):

        tool = self.planner.choose(request)

        if tool is None:

            return (
                "I couldn't determine which tool "
                "should handle that request."
            )

        print(f"🤖 Selected Tool: {tool}")

        try:

            return self.tool_manager.execute(
                tool,
                *args
            )

        except Exception as e:

            return (
                f"Tool '{tool}' failed:\n\n{e}"
            )
