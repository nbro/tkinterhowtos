from tkinter import *

root = Tk()
root.option_readfile('optionDB')

f1 = Frame(root, width=300, height=140)
Frame(f1, bg='gray75', relief=GROOVE, borderwidth=3,
      width=60, height=45).pack(side=LEFT, padx=40, pady=40)
f1.pack()

root.mainloop()
