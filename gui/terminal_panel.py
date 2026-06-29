import subprocess
import threading
import customtkinter as ctk

from services.error_detector import (
    contains_error,
    extract_error
)


class TerminalPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.process = None
        self.running = False

        self.run_callback = None
        self.error_callback = None

        # -------------------------
        # Toolbar
        # -------------------------

        toolbar = ctk.CTkFrame(self)
        toolbar.pack(fill="x")

        ctk.CTkLabel(
            toolbar,
            text="🖥 Terminal",
            font=("Segoe UI", 16, "bold")
        ).pack(
            side="left",
            padx=10,
            pady=8
        )

        self.run_button = ctk.CTkButton(
            toolbar,
            text="▶ Run",
            width=80,
            command=self.run_current
        )

        self.run_button.pack(
            side="right",
            padx=5
        )

        self.stop_button = ctk.CTkButton(
            toolbar,
            text="■ Stop",
            width=80,
            command=self.stop,
            state="disabled"
        )

        self.stop_button.pack(
            side="right"
        )

        ctk.CTkButton(
            toolbar,
            text="🧹 Clear",
            width=80,
            command=self.clear
        ).pack(
            side="right",
            padx=5
        )

        # -------------------------
        # Output
        # -------------------------

        self.output = ctk.CTkTextbox(
            self,
            font=("Consolas", 12)
        )

        self.output.pack(
            fill="both",
            expand=True
        )

    # -------------------------------------------------

    def set_run_callback(self, callback):

        self.run_callback = callback

    def set_error_callback(self, callback):

        self.error_callback = callback

    # -------------------------------------------------

    def run_current(self):

        if self.running:
            return

        if self.run_callback:
            self.run_callback()

    # -------------------------------------------------

    def run_python(self, filename):

        self.clear()

        self.running = True

        self.run_button.configure(
            state="disabled"
        )

        self.stop_button.configure(
            state="normal"
        )

        def worker():

            output = ""

            try:

                self.process = subprocess.Popen(
                    ["python", filename],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1
                )

                for line in self.process.stdout:

                    output += line

                    self.output.after(
                        0,
                        lambda l=line: self.append_output(l)
                    )

                self.process.wait()

            except Exception as e:

                output += str(e)

                self.output.after(
                    0,
                    lambda: self.append_output(
                        f"\n{e}\n"
                    )
                )

            finally:

                self.running = False

                self.output.after(
                    0,
                    self.finish_run
                )

                if contains_error(output):

                    if self.error_callback:

                        self.output.after(
                            0,
                            lambda: self.error_callback(
                                extract_error(output)
                            )
                        )

        threading.Thread(
            target=worker,
            daemon=True
        ).start()

    # -------------------------------------------------

    def finish_run(self):

        self.run_button.configure(
            state="normal"
        )

        self.stop_button.configure(
            state="disabled"
        )

    # -------------------------------------------------

    def append_output(self, text):

        self.output.insert(
            "end",
            text
        )

        self.output.see("end")

    # -------------------------------------------------

    def clear(self):

        self.output.delete(
            "1.0",
            "end"
        )

    # -------------------------------------------------

    def stop(self):

        if self.process:

            self.process.kill()

            self.append_output(
                "\nProcess stopped.\n"
            )

            self.finish_run()

    # -------------------------------------------------

    def get_output(self):

        return self.output.get(
            "1.0",
            "end-1c"
        )
