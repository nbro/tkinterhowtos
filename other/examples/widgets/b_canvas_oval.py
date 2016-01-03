from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Canvas Oval')
canvas = Canvas(root, width=200, height=160, bg='white')
canvas.create_oval(10, 10, 190, 150, fill='gray80')

canvas.pack()
root.mainloop()
