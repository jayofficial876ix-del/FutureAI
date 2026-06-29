import threading


class StreamWorker:

    def __init__(self, engine):
        self.engine = engine

    def start(self, conversation, callback):

        def run():

            try:

                for chunk in self.engine.stream_chat(conversation):
                    callback(chunk)

            except Exception as e:

                print("Streaming Error:", e)

        threading.Thread(
            target=run,
            daemon=True
        ).start()
