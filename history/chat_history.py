import json
import os

FILE = "history/chats.json"


def load_chats():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_chats(chats):
    os.makedirs("history", exist_ok=True)

    with open(FILE, "w") as f:
        json.dump(chats, f, indent=4)


def create_chat(title="New Chat"):
    chats = load_chats()

    chat = {
        "title": title,
        "messages": []
    }

    chats.append(chat)
    save_chats(chats)

    return len(chats) - 1


def add_message(chat_id, role, text):
    chats = load_chats()

    chats[chat_id]["messages"].append({
        "role": role,
        "text": text
    })

    save_chats(chats)


def rename_chat(chat_id, title):
    chats = load_chats()

    if chat_id < len(chats):
        chats[chat_id]["title"] = title[:35]

    save_chats(chats)


def get_chat(chat_id):
    chats = load_chats()

    if chat_id < len(chats):
        return chats[chat_id]

    return None
