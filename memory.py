
import json

FILE_NAME = "memory.json"

def load_memory():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

def save_memory(memory):
    with open(FILE_NAME, "w") as file:
        json.dump(memory, file, indent=4)
