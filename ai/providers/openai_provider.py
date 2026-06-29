import os

from dotenv import load_dotenv
from openai import OpenAI

from .base_provider import BaseProvider

load_dotenv()


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def chat(self, messages):

        try:

            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages
            )

            return response.choices[0].message.content

        except Exception as e:

            print("OpenAI Error:", e)

            return None

    def learn(self, question, answer):
        pass
