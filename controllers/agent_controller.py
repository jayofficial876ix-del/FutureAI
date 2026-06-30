from gui.agent_review import AgentReview
from gui.diff_viewer import DiffViewer


class AgentController:

    def __init__(
        self,
        app,
        agent,
        project_editor,
        right_sidebar,
        chat,
        add_ai_bubble
    ):

        self.app = app
        self.agent = agent
        self.project_editor = project_editor
        self.right_sidebar = right_sidebar
        self.chat = chat
        self.add_ai_bubble = add_ai_bubble

        self.editor = None

    # --------------------------------

    def set_editor(self, editor):

        self.editor = editor

    # --------------------------------

    def run(self, request):

        if not self.right_sidebar:
            return

        timeline = self.right_sidebar.tasks.timeline

        timeline.clear()

        steps = []

        for name in (

            "Analyze Request",
            "Index Project",
            "Plan Changes",
            "Generate Code",
            "Review Changes",
            "Apply Changes",
            "Finished"

        ):

            steps.append(
                timeline.add_step(name)
            )

        for step in steps[:3]:

            timeline.running(step)

            self.app.update()

            timeline.finish(step)

        results = self.agent.run(request)

        if not results:

            timeline.error(steps[2])

            return

        timeline.running(steps[3])

        self.app.update()

        timeline.finish(steps[3])

        timeline.running(steps[4])

        self.app.update()

        AgentReview(

            self.app,

            results,

            self.review_change,

            self.apply_changes

        )

        timeline.finish(steps[4])

        timeline.running(steps[5])

        self.app.update()

        timeline.finish(steps[5])

        timeline.running(steps[6])

        self.app.update()

        timeline.finish(steps[6])

        self.right_sidebar.set_status(
            "🟢 Ready"
        )

    # --------------------------------

    def review_change(self, result):

        DiffViewer(

            self.app,

            result,

            lambda updated:
                self.project_editor.apply_results(
                    [updated]
                )

        )

    # --------------------------------

    def apply_changes(self, results):

        for result in results:

            DiffViewer(

                self.app,

                result,

                lambda updated:
                    self.project_editor.apply_results(
                        [updated]
                    )

            )

        self.add_ai_bubble(

            self.chat,

            f"✅ Future AI updated {len(results)} file(s)."

        )

        try:

            if self.editor and self.editor.current_file:

                self.editor.open_file(
                    self.editor.current_file
                )

        except Exception as e:

            print(e)

        if self.right_sidebar:

            self.right_sidebar.set_status(
                "🟢 Ready"
            )
