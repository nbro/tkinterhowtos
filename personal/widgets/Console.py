"""
Simple console that accepts bash commands

Author: Nelson Brochado
Version: 0.0.1
"""


import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
from subprocess import Popen, PIPE
import subprocess


class Console(tk.Frame):

    """Simple console that can execute bash commands"""

    MESSAGE = """+===========================================================================+
|Insert a command in the entry field and press 'Execute' to run the command.|
|If you need to stop the command before it terminates, click 'Stop'.        |
|To clear the console output, click button 'Clear'.                         |
+===========================================================================+\n\n"""

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.text = ScrolledText(self, state="normal", bg="black", fg="#08c614",
                                 insertbackground="#08c614", selectbackground="#f01c1c")

        self.text.insert("end", Console.MESSAGE)
        self.text.config(state="disabled")

        # It seems not to work when Text is disabled...
        # self.text.bind("<<Modified>>", lambda: self.text.frame.see(tk.END))
        
        self.text.pack(expand=True, fill="both")

        # command that will be executed when "Execute" is pressed
        self.command = ""  # bash command
        self.popen = None  # will hold a reference to a Popen object
        self.running = False  # True if the process is running

        self.bottom = tk.Frame(self)

        self.prompt = tk.Label(self.bottom, text="Enter the command: ")
        self.prompt.pack(side="left", fill="x")
        self.entry = tk.Entry(self.bottom)
        self.entry.bind("<Return>", self._start)
        self.entry.focus()
        self.entry.pack(side="left", fill="x", expand=True)

        self.opts = {"width": 6}
        self.executer = tk.Button(self.bottom, text="Execute",
                                  command=self._start, **self.opts)
        self.executer.pack(side="left", padx=5, pady=2)
        self.clearer = tk.Button(self.bottom, text="Clear",
                                 command=self._clear, **self.opts)
        self.clearer.pack(side="left", padx=5, pady=2)
        self.stopper = tk.Button(self.bottom, text="Stop",
                                 command=self._stop, **self.opts)
        self.stopper.pack(side="left", padx=5, pady=2)

        self.bottom.pack(side="bottom", fill="both")

        

    def _clear(self):
        self._stop()
        self.text.config(state="normal")
        self.text.delete(1.0, "end-1c")
        self.text.insert("end", Console.MESSAGE)
        self.text.config(state="disabled")

    def _start(self, event=None):
        self._stop()
        self.running = True
        self.command = self.entry.get()
        threading.Thread(target=self._start_process).start()

    def _start_process(self):
        while self.running:
            self._execute(self.command)

    def _stop(self):
        if self.popen:
            try:
                self.popen.kill()
            except ProcessLookupError:
                pass
        self.running = False

    def _execute(self, command):
        self.text.config(state="normal")
        try:
            # self.popen will be a Popen object
            self.popen = Popen(command.split(), stdout=PIPE, bufsize=1)
            lines_iterator = iter(self.popen.stdout.readline, b"")

            # poll() return None if the process has not terminated
            # otherwise poll() returns the process's exit code
            while self.popen.poll() is None:
                for line in lines_iterator:
                    dline = line.decode("utf-8")
                    self.text.insert("end", dline)
                    self.text.see("end")

            self.text.insert("end", command  + " terminated.\n\n")

        except FileNotFoundError:
            self.text.insert("end", "Unknown command: " + command + "\n\n")
        except PermissionError:
            self.text.insert("end", "Empty command: " + command + "\n\n")
        except Exception:
            pass

        self.text.see("end")
        self.text.config(state="disabled")
        self._stop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Console")
    Console(root).pack(expand=True, fill="both")
    root.mainloop()
