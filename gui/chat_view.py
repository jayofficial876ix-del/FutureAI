import customtkinter as ctk


def create_chat_view(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(side="left", fill="both", expand=True)

    title = ctk.CTkLabel(
        frame,
        text="👋 Welcome to Future AI",
        font=("Segoe UI", 28, "bold")
    )
    title.pack(pady=(40, 10))

    subtitle = ctk.CTkLabel(
        frame,
        text="Ask me anything or choose one of the tools on the left.",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=(0, 20))

    # Scrollable conversation area
    chat = ctk.CTkScrollableFrame(
        frame,
        corner_radius=12
    )

    chat.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    # Welcome Bubble
    welcome = ctk.CTkFrame(chat, fg_color="#1E1E1E")

    welcome.pack(
        fill="x",
        padx=10,
        pady=10
    )

    ctk.CTkLabel(
        welcome,
        text="🤖 Future AI",
        font=("Segoe UI", 18, "bold")
    ).pack(anchor="w", padx=15, pady=(15, 5))

    ctk.CTkLabel(
        welcome,
        text=(
            "Welcome!\n\n"
            "I'm ready to help you with:\n\n"
            "• 💬 Chat\n"
            "• 🔍 Research\n"
            "• 🌐 Website Builder\n"
            "• 📚 Learning\n"
            "• 🎨 Image Generation\n"
            "• 💡 Brainstorming\n\n"
            "Type a message below to begin."
        ),
        justify="left",
        font=("Segoe UI", 15)
    ).pack(anchor="w", padx=15, pady=(0, 15))

    return frame, chat
