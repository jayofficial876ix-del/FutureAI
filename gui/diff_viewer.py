import customtkinter as ctk


class DiffViewer(ctk.CTkToplevel):

    def __init__(self, parent, result, apply_callback):

        super().__init__(parent)

        self.result = result
        self.apply_callback = apply_callback

        self.title("🤖 Future AI Review")
        self.geometry("1200x700")

        # --------------------------
        # Title
        # --------------------------

        ctk.CTkLabel(
            self,
            text="AI Suggested Changes",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=10
        )

        # --------------------------
        # Editors
        # --------------------------

        editors = ctk.CTkFrame(self)

        editors.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        editors.grid_columnconfigure(0, weight=1)
        editors.grid_columnconfigure(1, weight=1)
        editors.grid_rowconfigure(0, weight=1)

        # --------------------------
        # Current File
        # --------------------------

        left = ctk.CTkFrame(editors)

        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 5)
        )

        ctk.CTkLabel(
            left,
            text="Current File",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=5)

        self.old = ctk.CTkTextbox(
            left,
            font=("Consolas", 13)
        )

        self.old.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.old.insert(
            "1.0",
            result["old"]
        )

        # --------------------------
        # AI Version
        # --------------------------

        right = ctk.CTkFrame(editors)

        right.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(5, 0)
        )

        ctk.CTkLabel(
            right,
            text="Future AI Version",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=5)

        self.new = ctk.CTkTextbox(
            right,
            font=("Consolas", 13)
        )

        self.new.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.new.insert(
            "1.0",
            result["new"]
        )

        # --------------------------
        # Buttons
        # --------------------------

        buttons = ctk.CTkFrame(self)

        buttons.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ctk.CTkButton(
            buttons,
            text="❌ Reject",
            command=self.destroy
        ).pack(
            side="right",
            padx=5
        )

        ctk.CTkButton(
            buttons,
            text="✅ Apply Changes",
            command=self.apply
        ).pack(
            side="right"
        )

    # --------------------------

    def apply(self):

        self.result["new"] = self.new.get(
            "1.0",
            "end-1c"
        )

        self.apply_callback(self.result)

        self.destroy()
