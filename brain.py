from builders.website_builder import build_website
from memory import load_memory, save_memory

memory = load_memory()

def get_response(user):

    user = user.lower()

    if user in memory:
        return memory[user]

    elif user.startswith("build website "):
        website_name = user.replace("build website ", "")
        file = build_website(website_name)
        return f"Website created successfully!\n\nSaved as:\n{file}"

    elif "hello" in user:
        return "Hello! 👋"

    elif "who are you" in user:
        return "I'm Future AI."

    elif "how are you" in user:
        return "I'm doing great!"

    elif "who made you" in user:
        return "I was created by Jay!"

    return None


def teach(user, answer):
    memory[user.lower()] = answer
    save_memory(memory)
