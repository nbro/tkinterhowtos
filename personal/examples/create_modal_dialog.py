"""

Example of how to create a modal dialog.

Based on: http://tkinter.unpythonic.net/wiki/ModalWindow

To create a modal dialog, we need basically three key methods:

    1. transient
    2. grab_set
    3. wait_window
"""

import tkinter as tk


class ModalDialog(tk.Toplevel):

    """Simple modal dialog with a button"""

    def __init__(self, root, *args, **kwargs):
        tk.Toplevel.__init__(self, root, *args, **kwargs)
        
        self.body = tk.Frame(self, bd=1, relief="groove")
        self.body.pack(expand=True, fill="both", padx=1, pady=1)

        self.bottom = tk.Frame(self, bd=1, relief="groove")
        self.bottom.pack(fill="x", side="bottom", padx=1, pady=1)

        self.ok_button = tk.Button(self.bottom, text="Ok", command=self._ok)
        self.ok_button.pack(side="right")

        self.close_button = tk.Button(self.bottom, text="Close", command=self.destroy)
        self.close_button.pack(side="right")

        # Makes the window modal
        self.transient(root)  # http://effbot.org/tkinterbook/wm.htm#Tkinter.Wm.transient-method
        self.grab_set()  # http://effbot.org/tkinterbook/tkinter-dialog-windows.htm
        self.wait_window(self)  # http://effbot.org/tkinterbook/widget.htm#Tkinter.Widget.wait_window-method

    def _ok(self):
        print("Ok")


if __name__ == "__main__":
    root = tk.Tk()
    opener = tk.Button(root, text="Open modal dialog", command=lambda: ModalDialog(root))
    opener.pack()
    root.mainloop()
