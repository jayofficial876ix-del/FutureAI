import customtkinter as ctk

from history.chat_history import load_chats


class SidebarManager:

	def __init__(self, parent, open_chat, new_chat, delete_chat):

		self.parent = parent
		self.open_chat = open_chat
		self.new_chat = new_chat
		self.delete_chat = delete_chat

		self.sidebar = None

		self.refresh()

	def refresh(self):

		if self.sidebar:
			self.sidebar.destroy()

		self.sidebar = ctk.CTkFrame(
			self.parent,
			width=220,
			corner_radius=0
		)

		self.sidebar.pack(side="left", fill="y")
		self.sidebar.pack_propagate(False)

		# Title
		ctk.CTkLabel(
			self.sidebar,
			text="🤖 Future AI",
			font=("Segoe UI", 24, "bold")
		).pack(pady=(20, 15))

		# New Chat
		ctk.CTkButton(
			self.sidebar,
			text="+ New Chat",
			command=self.new_chat
		).pack(fill="x", padx=15, pady=(0, 15))

		# Recent Chats
		ctk.CTkLabel(
			self.sidebar,
			text="Recent Chats",
			font=("Segoe UI", 16, "bold")
		).pack(anchor="w", padx=15)

		chats = load_chats()

		for i, chat in enumerate(chats):

			row = ctk.CTkFrame(
				self.sidebar,
				fg_color="transparent"
			)

			row.pack(
				fill="x",
				padx=10,
				pady=3
			)

			title = chat["title"]

			if len(title) > 20:
				title = title[:20] + "..."

			ctk.CTkButton(
				row,
				text="💬 " + title,
				anchor="w",
				width=145,
				command=lambda i=i: self.open_chat(i)
			).pack(
				side="left",
				fill="x",
				expand=True
			)

			ctk.CTkButton(
				row,
				text="🗑",
				width=35,
				fg_color="#8B1E1E",
				hover_color="#B22222",
				command=lambda i=i: self.delete_chat(i)
			).pack(
				side="right",
				padx=(5, 0)
			)

