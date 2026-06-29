import customtkinter as ctk

from tkinter import messagebox

from gui.action_card import ActionCard
from gui.agent_dialog import AgentDialog

from projects.project_manager import import_project


class WelcomeDashboard(ctk.CTkFrame):

	def __init__(self, parent, controller):

		super().__init__(
			parent,
			fg_color="transparent"
		)

		self.controller = controller

		# --------------------------------
		# Title
		# --------------------------------

		ctk.CTkLabel(
			self,
			text="✨ Future AI",
			font=("Segoe UI", 34, "bold")
		).pack(
			pady=(30, 5)
		)

		ctk.CTkLabel(
			self,
			text="Welcome back! What would you like to do today?",
			font=("Segoe UI", 16),
			text_color="#A0A0A0"
		).pack(
			pady=(0, 25)
		)

		# --------------------------------
		# Quick Actions
		# --------------------------------

		self.cards = ctk.CTkFrame(
			self,
			fg_color="transparent"
		)

		self.cards.pack(
			fill="x",
			padx=40
		)

		self.add_card(
			"💬",
			"New Chat",
			"Start a new conversation.",
			self.new_chat
		)

		self.add_card(
			"🤖",
			"AI Agent",
			"Run an autonomous AI task.",
			self.ai_agent
		)

		self.add_card(
			"📂",
			"Open Project",
			"Import a project into Future AI.",
			self.open_project
		)

		self.add_card(
			"📄",
			"Generate Code",
			"Generate new code instantly.",
			self.generate_code
		)

		self.add_card(
			"🌐",
			"Build Website",
			"Generate a website with AI.",
			self.website
		)

		self.add_card(
			"🧠",
			"Explain Code",
			"Understand any code instantly.",
			self.explain
		)

		# --------------------------------
		# Status
		# --------------------------------

		status = ctk.CTkFrame(
			self,
			corner_radius=12
		)

		status.pack(
			fill="x",
			padx=40,
			pady=30
		)

		ctk.CTkLabel(
			status,
			text="🚀 Future AI Ready",
			font=("Segoe UI", 18, "bold")
		).pack(
			anchor="w",
			padx=15,
			pady=(15, 5)
		)

		ctk.CTkLabel(
			status,
			text=
			"• AI Engine Online\n"
			"• Workspace Ready\n"
			"• Project Index Enabled\n"
			"• AI Agent Available",
			justify="left",
			text_color="#B0B0B0"
		).pack(
			anchor="w",
			padx=15,
			pady=(0, 15)
		)

	# --------------------------------

	def add_card(self, icon, title, description, command):

		card = ActionCard(
			self.cards,
			icon,
			title,
			description,
			command
		)

		card.pack(
			fill="x",
			pady=6
		)

	# --------------------------------
	# Actions
	# --------------------------------

	def new_chat(self):

		self.controller.new_chat()

	# --------------------------------

	def ai_agent(self):

		AgentDialog(
			self.winfo_toplevel(),
			self.controller.run_agent
		)

	# --------------------------------

	def open_project(self):

		project = import_project()

		print("Imported Project:", project)

		if not project:
			return

		try:

			self.controller.layout.explorer_page.load_project(
				project["path"]
			)

		except Exception as e:

			print("Explorer Error:", e)

		messagebox.showinfo(
			"Future AI",
			f"Project imported successfully!\n\n{project['name']}"
		)

	# --------------------------------

	def generate_code(self):

		print("Generate Code")

	# --------------------------------

	def website(self):

		print("Website Builder")

	# --------------------------------

	def explain(self):

		print("Explain Code")

