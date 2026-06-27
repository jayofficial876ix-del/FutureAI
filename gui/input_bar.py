import customtkinter as ctk


def create_input_bar(parent, send_callback):

    bottom = ctk.CTkFrame(parent)
    bottom.pack(fill="x", padx=20, pady=(0, 20))

    # Attach Button
    attach_button = ctk.CTkButton(
        bottom,
        text="📎",
        width=40
    )
    attach_button.pack(side="left", padx=(0, 8))

    # Voice Button
    voice_button = ctk.CTkButton(
        bottom,
        text="🎤",
        width=40
    )
    voice_button.pack(side="left", padx=(0, 8))

    # Message Entry
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

    # Send Button
    send_button = ctk.CTkButton(
        bottom,
        text="Send ➜",
        command=send_callback
    )

    send_button.pack(side="right")

    # Press Enter to Send
    message.bind("<Return>", lambda event: send_callback())

    return message, send_button
