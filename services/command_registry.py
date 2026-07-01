class CommandRegistry:

    def __init__(self):

        self.commands = {}

    # ----------------------------

    def register(self, name, callback, description=""):

        self.commands[name] = {

            "callback": callback,

            "description": description

        }

    # ----------------------------

    def execute(self, name, *args, **kwargs):

        if name not in self.commands:

            raise ValueError(
                f"Unknown command: {name}"
            )

        return self.commands[name]["callback"](
            *args,
            **kwargs
        )

    # ----------------------------

    def search(self, text):

        text = text.lower()

        results = []

        for name, data in self.commands.items():

            if text in name.lower():

                results.append(

                    (
                        name,
                        data["description"]
                    )

                )

        return sorted(results)
