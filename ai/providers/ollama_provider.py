import requests

from .base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(self):

        self.url = "http://127.0.0.1:11434/api/generate"
        self.model = "qwen2.5-coder:7b"

    def chat(self, messages):

        prompt = ""

        for message in messages:

            role = message["role"].upper()

            prompt += f"{role}:\n{message['content']}\n\n"

        try:

            response = requests.post(

                self.url,

                json={

                    "model": self.model,
                    "prompt": prompt,
                    "stream": False

                },

                timeout=300

            )

            response.raise_for_status()

            return response.json()["response"]

        except Exception as e:

            print("Ollama Error:", e)

            return None
