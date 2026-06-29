import customtkinter as ctk
import os


def create_attachment_card(parent, filename):

    extension = os.path.splitext(filename)[1].lower()

    icons = {
        ".pdf": "📄",
        ".docx": "📝",
        ".txt": "📃",
        ".py": "🐍",
        ".html": "🌐",
        ".css": "🎨",
        ".js": "📜",
        ".png": "🖼",
        ".jpg": "🖼",
        ".jpeg": "🖼"
    }

    types = {
        ".pdf": "PDF Document",
        ".docx": "Word Document",
        ".txt": "Text File",
        ".py": "Python File",
        ".html": "HTML File",
        ".css": "CSS File",
        ".js": "JavaScript File",
        ".png": "Image",
        ".jpg": "Image",
        ".jpeg": "Image"
    }

    icon = icons.get(extension, "📁")
    file_type = types.get(extension, "File")

    size = os.path.getsize(filename) / 1024

    frame = ctk.CTkFrame(
        parent,
        corner_radius=14,
        fg_color="#242424"
    )

    frame.pack(
        anchor="w",
        padx=20,
        pady=8,
        fill="x"
    )

    ctk.CTkLabel(
        frame,
        text=f"{icon}  {os.path.basename(filename)}",
        font=("Segoe UI", 16, "bold")
    ).pack(
        anchor="w",
        padx=15,
        pady=(12, 2)
    )

    ctk.CTkLabel(
        frame,
        text=file_type,
        text_color="gray"
    ).pack(
        anchor="w",
        padx=15
    )

    ctk.CTkLabel(
        frame,
        text=f"{size:.1f} KB",
        text_color="gray"
    ).pack(
        anchor="w",
        padx=15,
        pady=(0, 12)
    )

    return frame
