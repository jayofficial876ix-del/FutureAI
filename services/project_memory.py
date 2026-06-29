
import os


def build_project_context(project):

	context = ""

	for filename in project.get("files", []):

		if not os.path.exists(filename):
			continue

		try:

			with open(
				filename,
				"r",
				encoding="utf-8",
				errors="ignore"
			) as f:

				text = f.read()

			context += (
				f"\n\n===== {os.path.basename(filename)} =====\n"
			)

			context += text[:4000]

		except Exception:

			continue

	return context
