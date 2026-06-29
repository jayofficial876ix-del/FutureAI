import customtkinter as ctk


def create_code_block(parent, language, code):

    frame = ctk.CTkFrame(
        parent,
        fg_color="#1E1E1E",
        corner_radius=12
    )

    frame.pack(
        fill="x",
        padx=15,
        pady=10
    )

    # Header
    header = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    header.pack(
        fill="x",
        padx=10,
        pady=(10, 5)
    )

    ctk.CTkLabel(
        header,
        text=language.upper(),
        font=("Segoe UI", 13, "bold")
    ).pack(side="left")

    def copy_code():

        parent.clipboard_clear()
        parent.clipboard_append(code)

    ctk.CTkButton(
        header,
        text="📋 Copy",
        width=80,
        command=copy_code
    ).pack(side="right")

    # Code Box
    code_box = ctk.CTkTextbox(
        frame,
        height=180,
        font=("Consolas", 13)
    )

    code_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=(0, 10)
    )

    code_box.insert("1.0", code)

    code_box.configure(
        state="disabled"
    )

    return frame
