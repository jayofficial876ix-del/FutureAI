import threading


class Task:

    def __init__(self, title, action):

        self.title = title

        self.action = action

        self.status = "Waiting"

        self.result = None


class TaskEngine:

    def __init__(self):

        self.tasks = []

        self.running = False

    # -----------------------------

    def add(self, title, action):

        self.tasks.append(

            Task(title, action)

        )

    # -----------------------------

    def clear(self):

        self.tasks.clear()

    # -----------------------------

    def run(self):

        if self.running:
            return

        self.running = True

        thread = threading.Thread(

            target=self._worker,

            daemon=True

        )

        thread.start()

    # -----------------------------

    def _worker(self):

        for task in self.tasks:

            task.status = "Running"

            try:

                task.result = task.action()

                task.status = "Done"

            except Exception as e:

                task.result = str(e)

                task.status = "Error"

        self.running = False
