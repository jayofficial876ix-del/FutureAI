import customtkinter as ctk


def add_user_bubble(chat, message):

    bubble = ctk.CTkFrame(
        chat,
        fg_color="#2563EB",
        corner_radius=16
    )

    bubble.pack(
        anchor="e",
        padx=20,
        pady=8
    )

    ctk.CTkLabel(
        bubble,
        text=message,
        justify="left",
        wraplength=450,
        font=("Segoe UI", 15)
    ).pack(
        padx=16,
        pady=12
    )


def add_ai_bubble(chat, message):

    bubble = ctk.CTkFrame(
        chat,
        fg_color="#2F2F2F",
        corner_radius=16
    )

    bubble.pack(
        anchor="w",
        padx=20,
        pady=8
    )

    ctk.CTkLabel(
        bubble,
        text=message,
        justify="left",
        wraplength=450,
        font=("Segoe UI", 15)
    ).pack(
        padx=16,
        pady=12
    )


def add_system_bubble(chat, message):

    label = ctk.CTkLabel(
        chat,
        text=message,
        text_color="gray",
        font=("Segoe UI", 12)
    )

    label.pack(pady=5)

    return label
