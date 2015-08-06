# from SO
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Iconify on closing')

        # Calls the method "iconify" when you try to close the window
        self.protocol("WM_DELETE_WINDOW", self.iconify)

        # Click Esc to destroy the window
        self.bind('<Escape>', lambda e: self.destroy())

        # Create a menu bar with an Exit command
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

        # create a Text widget with a Scrollbar attached
        txt = ScrolledText(self, undo=True)
        txt['font'] = ('consolas', '12')
        txt.pack(expand=True, fill='both')
        

app = App()
app.mainloop()
