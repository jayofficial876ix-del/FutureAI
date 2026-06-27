import customtkinter as ctk


def create_chat_view(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(side="left", fill="both", expand=True)

    title = ctk.CTkLabel(
        frame,
        text="👋 Welcome to Future AI",
        font=("Segoe UI", 28, "bold")
    )
    title.pack(pady=(60, 15))

    subtitle = ctk.CTkLabel(
        frame,
        text="Ask me anything or choose one of the tools on the left.",
        font=("Segoe UI", 16)
    )
    subtitle.pack(pady=(0, 25))

    chat = ctk.CTkTextbox(
        frame,
        font=("Segoe UI", 15)
    )

    chat.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    chat.insert(
        "end",
        """🤖 Future AI

Welcome!

I'm ready to help you with:

• 💬 Chat
• 🔍 Research
• 🌐 Website Builder
• 📚 Learning
• 🎨 Image Generation
• 💡 Brainstorming

--------------------------------------------

Type a message below to begin.

"""
    )

    return frame, chat
