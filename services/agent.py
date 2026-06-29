
from services.agent_planner import AgentPlanner
from services.agent_executor import AgentExecutor
from services.project_editor import ProjectEditor
from services.project_context import ProjectContext

from projects.project_manager import load_projects


class AIAgent:

	def __init__(self, ai):

		self.ai = ai

		self.planner = AgentPlanner(ai)
		self.executor = AgentExecutor(ai, self.planner)
		self.editor = ProjectEditor()
		self.context = ProjectContext()

	# -----------------------------------
	# Main Entry Point
	# -----------------------------------

	def run(self, request):

		print("\n========== AI AGENT ==========")
		print("Request:", request)

		projects = load_projects()

		print("Projects:", projects)

		if not projects:
			print("❌ No projects loaded.")
			return None

		project = projects[0]

		print("Project:", project["name"])

		# -----------------------------------
		# Build searchable index
		# -----------------------------------

		print("Building project index...")

		self.context.load_project(project)

		print("✅ Project indexed.")

		# -----------------------------------
		# Ask planner
		# -----------------------------------

		print("Planning changes...")

		files = self.executor.execute(request)

		print("Planner returned:", files)

		if not files:
			print("❌ Planner returned no files.")
			return None

		results = []

		# -----------------------------------
		# Process each file
		# -----------------------------------

		for filename in files:

			print("\nProcessing:", filename)

			full_path = None

			for project_file in project["files"]:

				if project_file.endswith(filename):

					full_path = project_file
					break

			print("Matched path:", full_path)

			if full_path is None:
				print("❌ File not found in project.")
				continue

			code = self.editor.read(full_path)

			print("Characters read:", len(code))

			conversation = [

				{
					"role": "system",
					"content":
					(
						"You are an expert software engineer.\n"
						"Modify ONLY this file.\n"
						"Return ONLY the updated code."
					)
				},

				{
					"role": "user",
					"content":
						f"Task:\n{request}\n\n"
						f"Filename:\n{filename}\n\n"
						f"Code:\n\n{code}"
				}

			]

			print("Sending request to AI...")

			new_code = self.ai.chat(conversation)

			if new_code is None:
				print("❌ AI returned None.")
				continue

			print("✅ AI returned", len(new_code), "characters.")

			results.append({

				"filename": full_path,
				"old": code,
				"new": new_code

			})

		print("\nResults created:", len(results))
		print("========== DONE ==========" ,"\n")

		return results
