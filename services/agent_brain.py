class AgentBrain:

    def __init__(self):
        self.history = []

    def remember(self, request):
        self.history.append(request)

    def last_request(self):
        if not self.history:
            return None
        return self.history[-1]

    def clear(self):
        self.history.clear()
