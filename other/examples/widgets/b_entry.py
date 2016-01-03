from tkinter import *

root = Tk()
root.option_readfile('optionDB')

f1 = Frame(root, width=300, height=140)
entry = Entry(f1, bg='gray75', width=5)
entry.pack(side=LEFT, padx=40, pady=40)
entry.insert(0, "Entry")
f1.pack()

root.mainloop()
