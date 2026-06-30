import json
import os

SESSION_FILE = "session.json"


class SessionManager:

    def save(

        self,

        editor,

        chats=None,

        project=None

    ):

        data = {

            "project": project,

            "current_file": editor.current_file,

            "open_files": list(

                editor.open_files.keys()

            ),

            "chats": chats or []

        }

        with open(

            SESSION_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                data,

                f,

                indent=4

            )

    # ----------------------------

    def load(self):

        if not os.path.exists(

            SESSION_FILE

        ):

            return {}

        with open(

            SESSION_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(f)
