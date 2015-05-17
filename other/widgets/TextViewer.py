"""
Taken from idlelib module (Python 3.4)

Modified by Nelson Brochado

Simple text browser for IDLE
"""

from tkinter import *
import tkinter.messagebox as tkMessageBox


class TextViewer(Toplevel):

    """A simple text viewer dialog for IDLE"""

    def __init__(self, parent, title, text, modal=True):
        """Show the given text in a scrollable window with a 'close' button

        """
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.geometry("=%dx%d+%d+%d" % (625, 500, parent.winfo_rootx() + 10,
                                        parent.winfo_rooty() + 10))
        # elguavas - config placeholders til config stuff completed
        self.bg = '#ffffff'
        self.fg = '#000000'

        self.create_widgets()
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.Ok)
        self.parent = parent
        self.textView.focus_set()
        # key bindings for this dialog
        self.bind('<Return>', self.Ok)  # dismiss dialog
        self.bind('<Escape>', self.Ok)  # dismiss dialog
        self.textView.insert(0.0, text)
        self.textView.config(state=DISABLED)

        if modal:
            self.transient(parent)
            self.grab_set()
            self.wait_window()

    def create_widgets(self):
        frameText = Frame(self, relief=SUNKEN, height=700)
        frameButtons = Frame(self)
        self.buttonOk = Button(frameButtons, text='Close',
                               command=self.Ok, takefocus=FALSE)
        self.scrollbarView = Scrollbar(frameText, orient=VERTICAL,
                                       takefocus=FALSE, highlightthickness=0)
        self.textView = Text(frameText, wrap=WORD, highlightthickness=0,
                             fg=self.fg, bg=self.bg)
        self.scrollbarView.config(command=self.textView.yview)
        self.textView.config(yscrollcommand=self.scrollbarView.set)
        self.buttonOk.pack()
        self.scrollbarView.pack(side=RIGHT, fill=Y)
        self.textView.pack(side=LEFT, expand=TRUE, fill=BOTH)
        frameButtons.pack(side=BOTTOM, fill=X)
        frameText.pack(side=TOP, expand=TRUE, fill=BOTH)

    def Ok(self, event=None):
        self.destroy()


def view_text(parent, title, text, modal=True):
    return TextViewer(parent, title, text, modal)


def view_file(parent, title, filename, encoding=None, modal=True):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            contents = file.read()
    except OSError:
        import tkinter.messagebox as tkMessageBox
        tkMessageBox.showerror(title='File Load Error',
                               message='Unable to load file %r .' % filename,
                               parent=parent)
    else:
        return view_text(parent, title, contents, modal)


if __name__ == '__main__':
    root = Tk()
    root.title('TextView test')
    
    filename = './TextView.py'

    with open(filename, 'r') as f:
        text = f.read()

    btn1 = Button(root, text='See this script', command=lambda: view_text(root, filename, text))
    btn1.pack(side=LEFT)

    close = Button(root, text='Close', command=root.destroy)
    close.pack(side=RIGHT)
    
    root.mainloop()
