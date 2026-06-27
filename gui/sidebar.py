import customtkinter as ctk

from history.chat_history import load_chats


def create_sidebar(parent, open_chat, new_chat):

	sidebar = ctk.CTkFrame(
		parent,
		width=220,
		corner_radius=0
	)

	sidebar.pack(side="left", fill="y")
	sidebar.pack_propagate(False)

	# ===== Title =====

	title = ctk.CTkLabel(
		sidebar,
		text="🤖 Future AI",
		font=("Segoe UI", 24, "bold")
	)
	title.pack(pady=(20, 15))

	# ===== New Chat =====

	ctk.CTkButton(
		sidebar,
		text="+ New Chat",
		command=new_chat
	).pack(fill="x", padx=15, pady=(0, 15))

	# ===== Recent Chats =====

	ctk.CTkLabel(
		sidebar,
		text="Recent Chats",
		font=("Segoe UI", 16, "bold")
	).pack(anchor="w", padx=15)

	chats = load_chats()

	if not chats:

		ctk.CTkLabel(
			sidebar,
			text="No chats yet",
			text_color="gray"
		).pack(anchor="w", padx=20, pady=10)

	else:

		for i, chat in enumerate(chats):

			title = chat["title"]

			if len(title) > 28:
				title = title[:28] + "..."

			ctk.CTkButton(
				sidebar,
				text="💬 " + title,
				anchor="w",
				height=34,
				command=lambda i=i: open_chat(i)
			).pack(
				fill="x",
				padx=15,
				pady=3
			)

	# ===== Divider =====

	ctk.CTkLabel(
		sidebar,
		text="────────────────"
	).pack(pady=10)

	# ===== Tools =====

	tools = [
		"🔍 Research",
		"📚 Learn",
		"🎨 Images",
		"💡 Brainstorm",
		"🌐 Website Builder",
		"⚙️ Settings"
	]

	for tool in tools:

		ctk.CTkButton(
			sidebar,
			text=tool,
			height=38
		).pack(
			fill="x",
			padx=15,
			pady=4
		)

	return sidebar

