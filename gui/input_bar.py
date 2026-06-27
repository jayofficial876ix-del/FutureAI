import customtkinter as ctk


def create_input_bar(parent):

    bottom = ctk.CTkFrame(parent)
    bottom.pack(fill="x", padx=20, pady=(0, 20))

    attach_button = ctk.CTkButton(
        bottom,
        text="📎",
        width=40
    )
    attach_button.pack(side="left", padx=(0, 8))

    voice_button = ctk.CTkButton(
        bottom,
        text="🎤",
        width=40
    )
    voice_button.pack(side="left", padx=(0, 8))

    message = ctk.CTkEntry(
        bottom,
        placeholder_text="Ask Future AI anything..."
    )

    message.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 10)
    )

    send_button = ctk.CTkButton(
        bottom,
        text="Send ➜"
    )

    send_button.pack(side="right")

    return message, send_button
