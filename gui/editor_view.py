import threading
import customtkinter as ctk

from ai.ai_engine import AIEngine
from gui.ghost_text import GhostText
from services.ai_completion import AICompletion
from services.syntax_highlighter import highlight


class EditorView:

	def __init__(self, parent):

		self.frame = ctk.CTkFrame(parent)

		# -------------------------
		# Line Numbers
		# -------------------------

		self.lines = ctk.CTkTextbox(
			self.frame,
			width=55,
			font=("Consolas", 14)
		)

		self.lines.pack(
			side="left",
			fill="y"
		)

		self.lines.configure(
			state="disabled"
		)

		# -------------------------
		# Editor
		# -------------------------

		self.editor = ctk.CTkTextbox(
			self.frame,
			font=("Consolas", 14)
		)

		self.editor.pack(
			side="right",
			fill="both",
			expand=True
		)

		# -------------------------
		# AI Completion
		# -------------------------

		self.ai = AIEngine()

		self.completion = AICompletion(
			self.ai
		)

		self.ghost = GhostText(
			self.editor
		)

		self.after_id = None

		# -------------------------
		# Current Line Highlight
		# -------------------------

		self.editor.tag_config(
			"current_line",
			background="#2D2D30"
		)

		# -------------------------
		# Events
		# -------------------------

		self.editor.bind(
			"<KeyRelease>",
			self.on_key_release
		)

		self.editor.bind(
			"<ButtonRelease>",
			self.update
		)

		self.editor.bind(
			"<FocusIn>",
			self.update
		)

		self.editor.bind(
			"<Tab>",
			self.accept_completion
		)

		self.update()

	# ------------------------------------------------

	def pack(self, **kwargs):

		self.frame.pack(**kwargs)

	# ------------------------------------------------

	def on_key_release(self, event=None):

		self.update()

		self.ghost.clear()

		if self.after_id:

			self.editor.after_cancel(
				self.after_id
			)

		self.after_id = self.editor.after(
			400,
			self.request_completion
		)

	# ------------------------------------------------

	def request_completion(self):

		code = self.get()

		def worker():

			try:

				suggestion = self.completion.complete(
					code
				)

				if suggestion:

					self.editor.after(
						0,
						lambda: self.ghost.show(
							suggestion
						)
					)

			except Exception as e:

				print("Completion Error:", e)

		threading.Thread(
			target=worker,
			daemon=True
		).start()

	# ------------------------------------------------

	def accept_completion(self, event=None):

		self.ghost.accept()

		return "break"

	# ------------------------------------------------

	def update(self, event=None):

		self.update_line_numbers()

		self.highlight_current_line()

		highlight(
			self.editor
		)

	# ------------------------------------------------

	def update_line_numbers(self):

		text = self.editor.get(
			"1.0",
			"end-1c"
		)

		count = max(
			1,
			text.count("\n") + 1
		)

		self.lines.configure(
			state="normal"
		)

		self.lines.delete(
			"1.0",
			"end"
		)

		self.lines.insert(
			"1.0",
			"\n".join(
				str(i)
				for i in range(
					1,
					count + 1
				)
			)
		)

		self.lines.configure(
			state="disabled"
		)

	# ------------------------------------------------

	def highlight_current_line(self):

		self.editor.tag_remove(
			"current_line",
			"1.0",
			"end"
		)

		line = self.editor.index(
			"insert"
		).split(".")[0]

		self.editor.tag_add(
			"current_line",
			f"{line}.0",
			f"{line}.0 lineend+1c"
		)

	# ------------------------------------------------

	def get(self):

		return self.editor.get(
			"1.0",
			"end-1c"
		)

	# ------------------------------------------------

	def set(self, text):

		self.editor.delete(
			"1.0",
			"end"
		)

		self.editor.insert(
			"1.0",
			text
		)

		self.ghost.clear()

		self.update()

	# ------------------------------------------------

	def clear(self):

		self.editor.delete(
			"1.0",
			"end"
		)

		self.ghost.clear()

		self.update()

	# ------------------------------------------------

	def widget(self):

		return self.editor

