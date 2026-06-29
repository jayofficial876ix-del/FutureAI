from brain import get_response, teach

from .base_provider import BaseProvider


class LocalProvider(BaseProvider):

    def chat(self, messages):

        # Use the latest user message for the local brain
        last_message = ""

        for message in reversed(messages):

            if message["role"] == "user":
                last_message = message["content"]
                break

        return get_response(last_message)

    def learn(self, question, answer):
        teach(question, answer)
