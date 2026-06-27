import customtkinter as ctk


def start_gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("🤖 Future AI")
    app.geometry("1100x700")

    title = ctk.CTkLabel(
        app,
        text="🤖 Future AI v0.3",
        font=("Segoe UI", 28, "bold")
    )
    title.pack(pady=30)

    subtitle = ctk.CTkLabel(
        app,
        text="Welcome to the new modular version of Future AI!",
        font=("Segoe UI", 16)
    )
    subtitle.pack()

    app.mainloop()