from tkinter import *

root = Tk()
root.option_readfile('optionDB')

f1 = Frame(root, width=300, height=140)
Button(f1, text="Button", bg='gray75').pack(side=LEFT, padx=40, pady=40)
f1.pack()

root.mainloop()
