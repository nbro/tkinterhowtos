from tkinter import *


class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title('GUI Design 9')
        self.base = 'gray60'
        self.fout = Frame(self.root, borderwidth=0)
        self.f1 = Frame(self.fout, borderwidth=2, relief=RAISED)
        Label(self.f1, text='RAISED', width=10).pack(side=LEFT)
        self.f1.pack(pady=5)
        self.f2 = Frame(self.fout, borderwidth=2, relief=SUNKEN)
        Label(self.f2, text='SUNKEN', width=10).pack(side=LEFT)
        self.f2.pack(pady=5)
        self.f3 = Frame(self.fout, borderwidth=2, relief=FLAT)
        Label(self.f3, text='FLAT', width=10).pack(side=LEFT)
        self.f3.pack(pady=5)
        self.f4 = Frame(self.fout, borderwidth=3, relief=RIDGE)
        Label(self.f4, text='RIDGE', width=10).pack(side=LEFT)
        self.f4.pack(pady=5)
        self.f5 = Frame(self.fout, borderwidth=2, relief=GROOVE)
        Label(self.f5, text='GROOVE', width=10).pack(side=LEFT)
        self.f5.pack(pady=5)
        self.f6 = Frame(self.fout, borderwidth=2, relief=SOLID)
        Label(self.f6, text='SOLID', width=10).pack(side=LEFT)
        self.f6.pack(pady=5)
        self.fout.pack()

myGUI = GUI()
myGUI.root.mainloop()
