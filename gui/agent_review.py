import os
import customtkinter as ctk


class AgentReview(ctk.CTkToplevel):

    def __init__(self, parent, results, review_callback, apply_callback):

        super().__init__(parent)

        self.title("🤖 Future AI Review")
        self.geometry("800x650")

        self.results = results
        self.review_callback = review_callback
        self.apply_callback = apply_callback

        self.grab_set()

        # --------------------------------
        # Header
        # --------------------------------

        ctk.CTkLabel(
            self,
            text="🤖 Future AI Review",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(15, 5)
        )

        ctk.CTkLabel(
            self,
            text="Review every change before applying it.",
            text_color="gray"
        ).pack(
            pady=(0, 15)
        )

        # --------------------------------
        # File List
        # --------------------------------

        self.frame = ctk.CTkScrollableFrame(self)

        self.frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        for result in self.results:

            row = ctk.CTkFrame(self.frame)

            row.pack(
                fill="x",
                pady=5
            )

            filename = os.path.basename(
                result["filename"]
            )

            ctk.CTkLabel(
                row,
                text="📄 " + filename,
                anchor="w",
                font=("Segoe UI", 14, "bold")
            ).pack(
                side="left",
                padx=10,
                fill="x",
                expand=True
            )

            ctk.CTkButton(
                row,
                text="Review",
                width=90,
                command=lambda r=result: self.review_callback(r)
            ).pack(
                side="right",
                padx=5
            )

        # --------------------------------
        # Bottom Buttons
        # --------------------------------

        bottom = ctk.CTkFrame(self)

        bottom.pack(
            fill="x",
            padx=15,
            pady=15
        )

        ctk.CTkButton(
            bottom,
            text="Cancel",
            width=110,
            command=self.destroy
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            bottom,
            text="✅ Apply All",
            width=150,
            command=self.apply
        ).pack(
            side="right",
            padx=5
        )

    # --------------------------------

    def apply(self):

        try:

            self.apply_callback(
                self.results
            )

        finally:

            self.destroy()
