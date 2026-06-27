from pages import *
import customtkinter as ctk
from tkinter import simpledialog
from brain import get_response, teach

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def start_gui():

    app = ctk.CTk()
    app.title("🤖 Future AI")
    app.geometry("1100x700")

    # ==========================
    # Main Area
    # ==========================

    main = ctk.CTkFrame(app)
    main.pack(side="right", fill="both", expand=True)

    chat = ctk.CTkTextbox(main, font=("Arial", 15))
    chat.pack(fill="both", expand=True, padx=15, pady=15)

    def new_chat():
        chat.delete("1.0", "end")

    # ==========================
    # Sidebar
    # ==========================

    sidebar = ctk.CTkFrame(app, width=220)
    sidebar.pack(side="left", fill="y")

    title = ctk.CTkLabel(
        sidebar,
        text="🤖 Future AI",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    ctk.CTkButton(
        sidebar,
        text="+ New Chat",
        command=new_chat
    ).pack(fill="x", padx=15, pady=(0, 15))

    ctk.CTkButton(
        sidebar,
        text="💬 Chat",
        command=lambda: show_chat(chat)
    ).pack(fill="x", padx=15, pady=6)

    ctk.CTkButton(
        sidebar,
        text="🔍 Research",
        command=lambda: show_research(chat)
    ).pack(fill="x", padx=15, pady=6)

    ctk.CTkButton(
        sidebar,
        text="📚 Learn",
        command=lambda: show_learn(chat)
    ).pack(fill="x", padx=15, pady=6)

    ctk.CTkButton(
        sidebar,
        text="🎨 Images",
        command=lambda: show_images(chat)
    ).pack(fill="x", padx=15, pady=6)

    ctk.CTkButton(
        sidebar,
        text="💡 Brainstorm",
        command=lambda: show_brainstorm(chat)
    ).pack(fill="x", padx=15, pady=6)

    ctk.CTkButton(
        sidebar,
        text="🌐 Website Builder",
        command=lambda: show_websites(chat)
    ).pack(fill="x", padx=15, pady=6)

    ctk.CTkButton(
        sidebar,
        text="⚙️ Settings",
        command=lambda: show_settings(chat)
    ).pack(fill="x", padx=15, pady=6)

    # ==========================
    # Bottom Input
    # ==========================

    bottom = ctk.CTkFrame(main)
    bottom.pack(fill="x", padx=15, pady=15)

    message = ctk.CTkEntry(
        bottom,
        placeholder_text="Ask Future AI anything..."
    )
    message.pack(side="left", fill="x", expand=True, padx=(0, 10))

    def send():

        user = message.get().strip()

        if not user:
            return

        chat.insert("end", f"👤 You:\n{user}\n\n")

        reply = get_response(user)

        if reply is None:
            answer = simpledialog.askstring(
                "Teach Future AI",
                f"What should I answer?\n\n{user}"
            )

            if answer:
                teach(user, answer)
                reply = "Thanks! I learned something new."
            else:
                reply = "Okay."

        chat.insert("end", f"🤖 Future AI:\n{reply}\n\n")
        chat.see("end")

        message.delete(0, "end")

    ctk.CTkButton(
        bottom,
        text="Send",
        command=send
    ).pack(side="right")

    message.bind("<Return>", lambda event: send())

    app.mainloop()
