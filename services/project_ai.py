from services.project_memory import build_project_context


def build_project_conversation(project, question):

    context = build_project_context(project)

    return [

        {
            "role": "system",
            "content":
            (
                "You are Future AI.\n"
                "You are an expert software engineer.\n"
                "You are assisting with the user's software project.\n"
                "Use ONLY the supplied project context when answering questions.\n"
                "If information is missing, say you cannot find it.\n"
                "Do not invent files or functions.\n"
                "Keep answers concise and technical."
            )
        },

        {
            "role": "system",
            "content":
            (
                "PROJECT CONTEXT\n"
                "================\n\n"
                f"{context}"
            )
        },

        {
            "role": "user",
            "content": question
        }

    ]
