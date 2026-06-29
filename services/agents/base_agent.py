class BaseAgent:

    def __init__(self, ai):
        self.ai = ai

    def system_prompt(self):
        return "You are an AI assistant."

    def execute(self, request, context=""):
        conversation = [
            {
                "role": "system",
                "content": self.system_prompt()
            },
            {
                "role": "user",
                "content": f"{context}\n\n{request}"
            }
        ]

        return self.ai.chat(conversation)
