import os


class ContextBuilder:

	def build(
		self,
		editor,
		terminal=None
	):

		context = []

		# Current file

		if getattr(editor, "current_file", None):

			context.append(
				{
					"type": "file",
					"name": os.path.basename(
						editor.current_file
					),
					"content": editor.get_text()
				}
			)

		# Selected text

		try:

			widget = editor.editor_widget()

			selected = widget.get(
				"sel.first",
				"sel.last"
			)

			if selected:

				context.append(
					{
						"type": "selection",
						"content": selected
					}
				)

		except Exception:
			pass

		# Terminal output

		if terminal:

			try:

				output = terminal.get_output()

				if output.strip():

					context.append(
						{
							"type": "terminal",
							"content": output[-5000:]
						}
					)

			except Exception:
				pass

		return context

