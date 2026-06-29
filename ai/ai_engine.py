from ai.config import AI_PROVIDER

from ai.providers.local_provider import LocalProvider
from ai.providers.openai_provider import OpenAIProvider


class AIEngine:

    def __init__(self):

        self.local = LocalProvider()

        if AI_PROVIDER == "openai":
            self.provider = OpenAIProvider()
        else:
            self.provider = self.local

    # -------------------------------------------------
    # Normal Chat (existing)
    # -------------------------------------------------

    def chat(self, conversation):

        reply = self.provider.chat(conversation)

        if reply is None:

            print("Falling back to Local AI...")

            reply = self.local.chat(conversation)

        return reply

    # -------------------------------------------------
    # Streaming Chat (NEW)
    # -------------------------------------------------

    def stream_chat(self, conversation):

        # Provider supports native streaming
        if hasattr(self.provider, "stream_chat"):

            try:

                yield from self.provider.stream_chat(
                    conversation
                )

                return

            except Exception:

                print("Streaming failed.")

        # ---------------------------------------------
        # Fallback
        # ---------------------------------------------

        reply = self.chat(conversation)

        if reply is None:
            return

        text = ""

        for ch in reply:

            text += ch

            yield text

    # -------------------------------------------------
    # Learn
    # -------------------------------------------------

    def learn(self, question, answer):

        self.local.learn(
            question,
            answer
        )
