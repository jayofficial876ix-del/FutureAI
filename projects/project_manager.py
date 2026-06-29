import os
import json

from services.folder_importer import import_folder

PROJECTS_FILE = "projects/projects.json"


# --------------------------------
# Load Projects
# --------------------------------

def load_projects():

    print("\n========== LOAD PROJECTS ==========")
    print("Current Working Directory:")
    print(os.getcwd())

    absolute_path = os.path.abspath(PROJECTS_FILE)

    print("\nProjects File:")
    print(absolute_path)

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
        "projects",
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

    project = projects[0]

    if isinstance(project, dict):
        return project.get("path")

    return project
