import customtkinter as ctk
from datetime import datetime

from gui.markdown_renderer import render_markdown


def current_time():
    return datetime.now().strftime("%I:%M %p")


# ==========================================================
# USER MESSAGE
# ==========================================================

def add_user_bubble(chat, message):

    outer = ctk.CTkFrame(
        chat,
        fg_color="transparent"
    )

    outer.pack(
        fill="x",
        padx=20,
        pady=8
    )

    bubble = ctk.CTkFrame(
        outer,
        fg_color="#2563EB",
        corner_radius=18
    )

    bubble.pack(
        anchor="e",
        padx=10
    )

    ctk.CTkLabel(
        bubble,
        text=message,
        wraplength=520,
        justify="left",
        font=("Segoe UI", 15)
    ).pack(
        padx=16,
        pady=12
    )

    return bubble


# ==========================================================
# STREAMING AI BUBBLE
# ==========================================================

class StreamingBubble:

    def __init__(self, chat):

        self.text = ""

        self.outer = ctk.CTkFrame(
            chat,
            fg_color="transparent"
        )

        self.outer.pack(
            fill="x",
            padx=20,
            pady=8
        )

        # Header

        header = ctk.CTkFrame(
            self.outer,
            fg_color="transparent"
        )

        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="🤖 Future AI",
            font=("Segoe UI", 14, "bold")
        ).pack(side="left")

        ctk.CTkLabel(
            header,
            text=current_time(),
            text_color="gray"
        ).pack(side="right")

        # Bubble

        self.bubble = ctk.CTkFrame(
            self.outer,
            fg_color="#2B2B2B",
            corner_radius=18
        )

        self.bubble.pack(
            fill="x",
            pady=(5, 0)
        )

        self.label = ctk.CTkLabel(
            self.bubble,
            text="▋",
            wraplength=700,
            justify="left",
            font=("Segoe UI", 15)
        )

        self.label.pack(
            padx=18,
            pady=15,
            anchor="w"
        )

    # ---------------------------------

    def update(self, text):

        self.text = text

        self.label.configure(
            text=render_markdown(text) + "▋"
        )

        self.label.update_idletasks()

    # ---------------------------------

    def finish(self):

        self.label.configure(
            text=render_markdown(self.text)
        )


# ==========================================================
# NORMAL AI MESSAGE
# ==========================================================

def add_ai_bubble(chat, message):

    bubble = StreamingBubble(chat)

    bubble.update(message)

    bubble.finish()

    return bubble


# ==========================================================
# CREATE STREAMING BUBBLE
# ==========================================================

def add_streaming_bubble(chat):

    return StreamingBubble(chat)


# ==========================================================
# SYSTEM MESSAGE
# ==========================================================

def add_system_bubble(chat, message):

    label = ctk.CTkLabel(
        chat,
        text=message,
        text_color="gray",
        font=("Segoe UI", 12)
    )

    label.pack(
        pady=6
    )

    return label
