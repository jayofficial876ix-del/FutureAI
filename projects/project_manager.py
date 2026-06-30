import os
import json

from services.folder_importer import import_folder

# --------------------------------
# Paths
# --------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

PROJECTS_FILE = os.path.join(
    BASE_DIR,
    "projects",
    "projects.json"
)

# --------------------------------
# Load Projects
# --------------------------------

def load_projects():

    print("\n========== LOAD PROJECTS ========== ")

    print("Current Working Directory:")
    print(os.getcwd())

    print("\nProjects File:")
    print(PROJECTS_FILE)

    exists = os.path.exists(PROJECTS_FILE)

    print("\nExists:")
    print(exists)

    if not exists:

        print("\n❌ projects.json not found.")
        print("===================================\n")

        return []

    try:

        with open(
            PROJECTS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            projects = json.load(f)

        print("\nLoaded Projects:")
        print(projects)

        print("===================================\n")

        return projects

    except Exception as e:

        print("\n❌ Failed to load projects.json")
        print(e)
        print("===================================\n")

        return []


# --------------------------------
# Save Projects
# --------------------------------

def save_projects(projects):

    os.makedirs(
        os.path.dirname(PROJECTS_FILE),
        exist_ok=True
    )

    with open(
        PROJECTS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            projects,
            f,
            indent=4
        )


# --------------------------------
# Create Project
# --------------------------------

def create_project(name):

    projects = load_projects()

    projects.append({

        "name": name,
        "path": "",
        "files": []

    })

    save_projects(projects)

    return len(projects) - 1


# --------------------------------
# Add File
# --------------------------------

def add_file(project_id, filename):

    projects = load_projects()

    if project_id >= len(projects):
        return

    if filename not in projects[project_id]["files"]:

        projects[project_id]["files"].append(
            filename
        )

    save_projects(projects)


# --------------------------------
# Get Project
# --------------------------------

def get_project(project_id):

    projects = load_projects()

    if project_id >= len(projects):
        return None

    return projects[project_id]


# --------------------------------
# Remove File
# --------------------------------

def remove_file(project_id, filename):

    projects = load_projects()

    if project_id >= len(projects):
        return

    if filename in projects[project_id]["files"]:

        projects[project_id]["files"].remove(
            filename
        )

    save_projects(projects)


# --------------------------------
# Import Project
# --------------------------------

def import_project():

    project = import_folder()

    if not project:
        return None

    projects = load_projects()

    # Don't import the same project twice
    for existing in projects:

        if existing.get("path") == project["path"]:

            print("Project already imported.")

            return existing

    projects.append(project)

    save_projects(projects)

    return project


# --------------------------------
# Current Project Path
# --------------------------------

def current_project_path():

    projects = load_projects()

    if not projects:
        return None

    return projects[0].get("path")


# --------------------------------
# Current Project
# --------------------------------

def current_project():

    projects = load_projects()

    if not projects:
        return None

    return projects[0]
