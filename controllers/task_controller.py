from services.task_engine import TaskEngine


class TaskController:

    def __init__(self, right_sidebar=None):

        self.right_sidebar = right_sidebar

        self.engine = TaskEngine()

    # --------------------------------

    def clear(self):

        self.engine.clear()

        if self.right_sidebar:

            self.right_sidebar.tasks.timeline.clear()

    # --------------------------------

    def add(self, title, action):

        if self.right_sidebar:

            timeline = self.right_sidebar.tasks.timeline

            step = timeline.add_step(title)

            def wrapped():

                timeline.running(step)

                try:

                    result = action()

                    timeline.finish(step)

                    return result

                except Exception:

                    timeline.error(step)

                    raise

        else:

            wrapped = action

        self.engine.add(

            title,

            wrapped

        )

    # --------------------------------

    def run(self):

        self.engine.run()
