"""
Window of a dialog that returns a value
Author: Bryan Oakley (Stackoverflow)
"""

import tkinter as tk


class CustomDialog(tk.Toplevel):

    def __init__(self, parent, prompt):
        tk.Toplevel.__init__(self, parent)
        self.var = tk.StringVar()
        self.label = tk.Label(self, text=prompt)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.done = tk.Button(self, text="OK", command=self.on_ok)
        self.label.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x")
        self.done.pack(side="right")
        self.entry.bind("<Return>", self.on_ok)

    def on_ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()


class Window(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.button = tk.Button(self, text="Get Input", command=self.on_button)
        self.label = tk.Label(self, text="", width=20)
        self.button.pack(padx=8, pady=8)
        self.label.pack(side="bottom", fill="both", expand=True)

    def on_button(self):
        string = CustomDialog(self, "Enter something:").show()
        self.label.configure(text="You entered:\n" + string)


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_geometry("400x200")
    Window(root).pack(fill="both", expand=True)
    root.mainloop()
