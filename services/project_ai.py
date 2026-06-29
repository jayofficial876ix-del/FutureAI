from services.project_memory import build_project_context


def build_project_conversation(project, question):

    context = build_project_context(project)

    return [
        {
            "role": "system",
            "content": (
                "You are an expert software engineer.\n"
                "Answer questions about the user's entire project.\n"
                "Use the supplied project files as your source of truth.\n"
                "If the answer cannot be found, clearly say so."
            )
        },
        {
            "role": "system",
            "content": context
        },
        {
            "role": "user",
            "content": question
        }
    ]
