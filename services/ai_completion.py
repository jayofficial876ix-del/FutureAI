class AICompletion:

    def __init__(self, ai):

        self.ai = ai

    # --------------------------------

    def complete(self, code):

        conversation = [

            {
                "role": "system",
                "content":
                    (
                        "You are an expert programming assistant.\n"
                        "Continue the user's code.\n"
                        "Return ONLY the next few lines.\n"
                        "Do not repeat existing code."
                    )
            },

            {
                "role": "user",
                "content": code
            }

        ]

        return self.ai.chat(conversation)
