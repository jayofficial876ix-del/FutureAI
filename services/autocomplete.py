import threading


class AutoCompleteService:

    def __init__(self, ai):

        self.ai = ai

    # -----------------------------

    def complete(self, code, callback):

        threading.Thread(

            target=self._worker,

            args=(code, callback),

            daemon=True

        ).start()

    # -----------------------------

    def _worker(self, code, callback):

        conversation = [

            {
                "role": "system",
                "content":
                (
                    "You are an expert software engineer.\n"
                    "Continue the user's code.\n"
                    "Return ONLY the continuation.\n"
                    "No markdown.\n"
                    "No explanations."
                )
            },

            {
                "role": "user",
                "content": code
            }

        ]

        result = self.ai.chat(conversation)

        if result:

            callback(result.strip())
