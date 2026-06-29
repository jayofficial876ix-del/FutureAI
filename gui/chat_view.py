import customtkinter as ctk


def quick_action(parent, emoji, title, description):

    card = ctk.CTkFrame(
        parent,
        fg_color="#252526",
        corner_radius=12,
        height=90
    )

    card.pack(
        fill="x",
        padx=8,
        pady=6
    )

    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text=f"{emoji}  {title}",
        font=("Segoe UI", 17, "bold")
    ).pack(
        anchor="w",
        padx=15,
        pady=(14, 2)
    )

    ctk.CTkLabel(
        card,
        text=description,
        text_color="#A0A0A0",
        justify="left",
        font=("Segoe UI", 13)
    ).pack(
        anchor="w",
        padx=15
    )

    return card


def create_welcome_card(chat):

    container = ctk.CTkFrame(
        chat,
        fg_color="transparent"
    )

    container.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # --------------------------------
    # Title
    # --------------------------------

    ctk.CTkLabel(
        container,
        text="✨ Future AI",
        font=("Segoe UI", 30, "bold")
    ).pack(
        pady=(10, 4)
    )

    ctk.CTkLabel(
        container,
        text="Welcome back! What would you like to build today?",
        text_color="#A0A0A0",
        font=("Segoe UI", 16)
    ).pack(
        pady=(0, 20)
    )

    # --------------------------------
    # Quick Actions
    # --------------------------------

    quick_action(
        container,
        "💬",
        "New Chat",
        "Start a conversation with Future AI."
    )

    quick_action(
        container,
        "🤖",
        "AI Agent",
        "Let Future AI complete complex tasks."
    )

    quick_action(
        container,
        "🌐",
        "Build Website",
        "Generate a complete website using AI."
    )

    quick_action(
        container,
        "📂",
        "Open Project",
        "Browse and analyze an existing project."
    )

    quick_action(
        container,
        "📄",
        "Generate Code",
        "Create Python, JavaScript, HTML, and more."
    )

    quick_action(
        container,
        "🧠",
        "Explain Code",
        "Understand any code instantly."
    )

    # --------------------------------
    # Tips
    # --------------------------------

    tips = ctk.CTkFrame(
        container,
        fg_color="#1E1E1E",
        corner_radius=12
    )

    tips.pack(
        fill="x",
        padx=8,
        pady=15
    )

    ctk.CTkLabel(
        tips,
        text="💡 Quick Tips",
        font=("Segoe UI", 18, "bold")
    ).pack(
        anchor="w",
        padx=15,
        pady=(15, 8)
    )

    ctk.CTkLabel(
        tips,
        text=
        "• Press Ctrl + T to search symbols\n"
        "• Use the AI Agent for large coding tasks\n"
        "• Open a project to enable Workspace AI\n"
        "• Future AI automatically remembers your conversations",
        justify="left",
        text_color="#B0B0B0",
        font=("Segoe UI", 14)
    ).pack(
        anchor="w",
        padx=15,
        pady=(0, 15)
    )


def create_chat_view(parent):

    frame = ctk.CTkFrame(parent)

    frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    chat = ctk.CTkScrollableFrame(
        frame,
        corner_radius=12
    )

    chat.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    create_welcome_card(chat)

    return frame, chat
