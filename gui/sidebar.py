import customtkinter as ctk
import os

# Only import Pillow if we actually use a logo
try:
    from PIL import Image
except ImportError:
    Image = None


def create_sidebar(parent):
    sidebar = ctk.CTkFrame(
        parent,
        width=190,
        corner_radius=0
    )
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    # ===== Logo (Optional) =====

    logo_path = os.path.join("assets", "logo.png")

    if Image is not None and os.path.exists(logo_path):
        try:
            logo = ctk.CTkImage(
                light_image=Image.open(logo_path),
                dark_image=Image.open(logo_path),
                size=(70, 70)
            )

            logo_label = ctk.CTkLabel(
                sidebar,
                image=logo,
                text=""
            )
            logo_label.pack(pady=(25, 10))

        except Exception:
            # Ignore bad or corrupted logo files
            pass

    # ===== Title =====

    title = ctk.CTkLabel(
        sidebar,
        text="🤖 Future AI",
        font=("Segoe UI", 24, "bold")
    )
    title.pack(pady=(20, 25))

    # ===== Navigation =====

    buttons = [
        "+ New Chat",
        "💬 Chat",
        "🔍 Research",
        "📚 Learn",
        "🎨 Images",
        "💡 Brainstorm",
        "🌐 Website Builder",
        "⚙️ Settings"
    ]

    for text in buttons:
        button = ctk.CTkButton(
            sidebar,
            text=text,
            height=42,
            corner_radius=10
        )
        button.pack(fill="x", padx=15, pady=6)

    return sidebar
