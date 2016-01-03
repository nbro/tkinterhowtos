from tkinter import *

root = Tk()
root.option_readfile('optionDB')

f1 = Frame(root)
Checkbutton(f1, text="Checkbutton", state=ACTIVE, anchor=W,
            width=10, height=5).pack(padx=40, pady=40)
f1.pack()

root.mainloop()
