import os
import customtkinter as ctk

from services.workspace_cache import workspace_cache


class QuickOpen(ctk.CTkToplevel):

	def __init__(self, parent, project_path, open_callback):

		super().__init__(parent)

		self.open_callback = open_callback

		self.title("📂 Quick Open")
		self.geometry("700x550")

		self.transient(parent)
		self.grab_set()

		# --------------------------------
		# Build cache once
		# --------------------------------

		if workspace_cache.project != project_path:

			workspace_cache.build(project_path)

		# --------------------------------
		# Header
		# --------------------------------

		ctk.CTkLabel(
			self,
			text="📂 Quick Open",
			font=("Segoe UI", 22, "bold")
		).pack(
			pady=(15, 8)
		)

		self.entry = ctk.CTkEntry(
			self,
			placeholder_text="Search files..."
		)

		self.entry.pack(
			fill="x",
			padx=15,
			pady=(0, 10)
		)

		self.entry.focus()

		self.entry.bind(
			"<KeyRelease>",
			self.search
		)

		self.results = ctk.CTkScrollableFrame(self)

		self.results.pack(
			fill="both",
			expand=True,
			padx=15,
			pady=(0, 15)
		)

		# Show everything immediately
		self.search()

	# --------------------------------

	def search(self, event=None):

		query = self.entry.get().strip()

		for widget in self.results.winfo_children():
			widget.destroy()

		if query:

			matches = workspace_cache.search(query)

		else:

			matches = workspace_cache.all_files()

		# Limit results for speed
		matches = matches[:100]

		for path in matches:

			filename = os.path.basename(path)

			button = ctk.CTkButton(
				self.results,
				text=f"📄 {filename}",
				anchor="w",
				command=lambda p=path: self.open_file(p)
			)

			button.pack(
				fill="x",
				pady=2
			)

	# --------------------------------

	def open_file(self, filename):

		self.destroy()

		self.open_callback(filename)

