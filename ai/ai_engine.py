from ai.config import AI_PROVIDER

from ai.providers.local_provider import LocalProvider
from ai.providers.openai_provider import OpenAIProvider
from ai.providers.ollama_provider import OllamaProvider


class AIEngine:

    def __init__(self):

        self.local = LocalProvider()
        self.ollama = OllamaProvider()

        if AI_PROVIDER == "openai":

            self.provider = OpenAIProvider()

        elif AI_PROVIDER == "ollama":

            self.provider = self.ollama

        else:

            self.provider = self.local

    # -------------------------------------------------
    # Normal Chat
    # -------------------------------------------------

    def chat(self, conversation):

        reply = self.provider.chat(conversation)

        if reply is not None:
            return reply

        print("Provider failed.")

        # ---------------------------------------------
        # Fallback to Ollama
        # ---------------------------------------------

        if self.provider != self.ollama:

            print("Falling back to Ollama...")

            reply = self.ollama.chat(conversation)

            if reply is not None:
                return reply

        # ---------------------------------------------
        # Final fallback
        # ---------------------------------------------

        print("Falling back to Local AI...")

        return self.local.chat(conversation)

    # -------------------------------------------------
    # Streaming Chat
    # -------------------------------------------------

    def stream_chat(self, conversation):

        if hasattr(self.provider, "stream_chat"):

            try:

                yield from self.provider.stream_chat(
                    conversation
                )

                return

            except Exception:

                print("Streaming failed.")

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
