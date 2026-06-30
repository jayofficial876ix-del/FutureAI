import os


class ProjectIndex:

	def __init__(self):

		self.files = []

	# --------------------------------

	def build(self, project_path):

		self.files.clear()

		for root, _, filenames in os.walk(project_path):

			for filename in filenames:

				if filename.endswith(

					(
						".py",
						".js",
						".ts",
						".tsx",
						".jsx",
						".html",
						".css",
						".json",
						".md"
					)

				):

					full = os.path.join(
						root,
						filename
					)

					try:

						with open(
							full,
							"r",
							encoding="utf-8",
							errors="ignore"
						) as f:

							code = f.read()

					except Exception:

						continue

					self.files.append(

						{
							"path": full,
							"name": filename,
							"code": code,
							"lower": code.lower()
						}

					)

	# --------------------------------

	def search(self, query, limit=6):

		words = query.lower().split()

		scores = []

		for file in self.files:

			score = 0

			for word in words:

				score += file["lower"].count(word)

				score += file["name"].lower().count(word) * 5

			if score:

				scores.append(

					(score, file)

				)

		scores.sort(
			reverse=True,
			key=lambda x: x[0]
		)

		return [

			item[1]

			for item in scores[:limit]

		]

