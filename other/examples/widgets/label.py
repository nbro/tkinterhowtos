from tkinter import *

root = Tk()
root.option_readfile('optionDB')

f1 = Frame(root, width=300, height=140)
Label(f1, text="Label", bg='gray75').pack(side=LEFT, padx=40, pady=40)
f1.pack()

root.mainloop()
