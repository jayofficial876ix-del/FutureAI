import subprocess
import threading
import customtkinter as ctk


class Terminal:

	def __init__(self, parent):

		self.frame = ctk.CTkFrame(parent)

		self.output = ctk.CTkTextbox(
			self.frame,
			font=("Consolas", 12)
		)

		self.output.pack(
			fill="both",
			expand=True,
			padx=10,
			pady=10
		)

		self.command = ctk.CTkEntry(
			self.frame,
			placeholder_text="Enter command..."
		)

		self.command.pack(
			fill="x",
			padx=10,
			pady=(0, 10)
		)

		self.command.bind(
			"<Return>",
			lambda e: self.run_command()
		)

	def pack(self, **kwargs):
		self.frame.pack(**kwargs)

	def write(self, text):

		self.output.insert("end", text)
		self.output.see("end")

	def run_command(self):

		cmd = self.command.get().strip()

		if not cmd:
			return

		self.write(f"> {cmd}\n")

		self.command.delete(0, "end")

		threading.Thread(
			target=self.execute,
			args=(cmd,),
			daemon=True
		).start()

	def execute(self, cmd):

		try:

			result = subprocess.run(
				cmd,
				shell=True,
				capture_output=True,
				text=True
			)

			self.write(result.stdout)

			if result.stderr:
				self.write(result.stderr)

		except Exception as e:

			self.write(str(e) + "\n")


