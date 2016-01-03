import time
from tkinter import *


class AfterIdleExample:

    def __init__(self, master=None):
        self.master = master

        self.frame = Frame(master, relief=RAISED, borderwidth=2)
        Label(self.frame, text='Press the button\nto start operation').pack()
        self.frame.pack(padx=4, pady=4)
        Button(master, text='Start', command=self.startOP).pack(side=TOP)

    def startOP(self):
        self.displayBusyCursor()
        time.sleep(10.0)  # simulate a long operation

    def displayBusyCursor(self):
        self.master.configure(cursor='watch')
        self.master.update()
        self.master.after_idle(self.removeBusyCursor)

    def removeBusyCursor(self):
        self.master.configure(cursor='arrow')


root = Tk()
root.option_readfile('optionDB2')
root.title('Busy Cursor')
example = AfterIdleExample(root)
root.mainloop()
