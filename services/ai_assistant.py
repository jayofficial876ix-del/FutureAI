from services.tool_planner import ToolPlanner


class AIAssistant:

    def __init__(self, tool_manager, ai_engine):

        self.tool_manager = tool_manager
        self.ai = ai_engine
        self.planner = ToolPlanner()

    # --------------------------------

    def handle(self, conversation):

        if not conversation:
            return None

        user_message = ""

        for message in reversed(conversation):

            if message["role"] == "user":

                user_message = message["content"]

                break

        tool = self.planner.choose(
            user_message
        )

        # -----------------------------
        # Use Tool
        # -----------------------------

        if tool:

            print(
                f"🤖 Tool Selected: {tool}"
            )

            try:

                return self.tool_manager.execute(
                    tool,
                    user_message
                )

            except Exception as e:

                print(e)

        # -----------------------------
        # Normal AI Chat
        # -----------------------------

        return self.ai.chat(
            conversation
        )

    # --------------------------------

    def stream(self, conversation):

        if not conversation:
            return

        user_message = ""

        for message in reversed(conversation):

            if message["role"] == "user":

                user_message = message["content"]

                break

        tool = self.planner.choose(
            user_message
        )

        if tool:

            reply = self.handle(
                conversation
            )

            yield reply

            return

        yield from self.ai.stream_chat(
            conversation
        )
