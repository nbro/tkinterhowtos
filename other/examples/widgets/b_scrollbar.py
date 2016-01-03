from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Scrollbar')

list = Listbox(root, height=6, width=15)
list.grid(row=0, column=0, rowspan=3, columnspan=3)

yscroll = Scrollbar(root, command=list.yview)
yscroll.grid(row=0, column=3, rowspan=3, sticky='ns')

list.configure(yscrollcommand=yscroll.set)

xscroll = Scrollbar(root, orient=HORIZONTAL, command=list.xview)
xscroll.grid(row=3, column=0, columnspan=3, sticky='we')

list.configure(xscrollcommand=xscroll.set)
list.insert(END, " " * 100)

for item in range(30):
    list.insert(END, "")

root.mainloop()
