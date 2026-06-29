class BaseProvider:

    def chat(self, messages):
        raise NotImplementedError

    def learn(self, question, answer):
        pass
