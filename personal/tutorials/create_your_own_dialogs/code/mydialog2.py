# Chapter: Create Your Own Dialogs
# Description: more advanced dialog derived from Toplevel
# File: mydialog2.py

import tkinter as tk


class MyDialog(tk.Toplevel):
    def __init__(self, parent, title='My Dialog', **options):
        """parent should be a Toplevel or a Frame widget"""
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.transient(self.parent)
        self.title(title)
        self.result = None

        self.body = tk.Frame(self)
        self.set_body(self.body)
        self.body.pack(expand=1, fill='both', padx=5, pady=5)
        self.body.focus_set()

        self.footer = tk.Frame(self)
        self.set_footer(parent=self.footer)
        self.footer.pack(fill='both', padx=5, pady=5)
        # Binding the Return and Escape events
        # with respectively the self.ok and self.cancel methods
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        # Handling the closing window event or protocol
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+{0}+{1}".format(self.parent.winfo_rootx() + 50,
                                        self.parent.winfo_rooty() + 50))

        # Mouse and keyword events are sent to self
        self.grab_set()
        # self waits for self

    def set_body(self, parent, *args):
        """Override this method to add widget to the body of the dialog
        parent is the top Frame where the widgets can be packed or grided"""
        message_label = tk.Label(parent, text="Hello World", border=1,
                                 relief='groove', font=('Arial', 16),
                                 padx=20, pady=10)
        message_label.pack(expand=1, fill='both', padx=40, pady=10)

    def set_footer(self, parent):
        """Standard buttons of the dialog.
        Override this method, if you don't want the standard buttons"""
        ok_button = tk.Button(parent, text="OK", width=8,
                              command=self.ok, default='active')
        ok_button.pack(padx=5, pady=5, side='right')
        cancel_button = tk.Button(parent, text="Cancel", width=8,
                                  command=self.cancel)
        cancel_button.pack(padx=5, pady=5, side='right')

    def ok(self, event=None):
        """event parameter is necessary
        because we have also binded some events with this method.
        An event is sent as first parameter 
        to its associated handler method
        when the same event occurs."""
        if not self.validate():
            self.body.focus_set()  # put focus back
            return
        self.withdraw()  # Hides self
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        """This method is called inside self.ok
        to validade eventually the contents of self.body.
        You should override this method 
        along with the self.body and self.apply method"""
        return False

    def apply(self, *args):
        """If self.validade returns True,
        this method will apply something when you click OK"""
        pass


def say_hello():
    print('Hello')


if __name__ == '__main__':
    root = tk.Tk()
    button = tk.Button(root, text='Hello', command=say_hello)
    button.pack()
    dialog = MyDialog(root)
    root.wait_window(dialog)
