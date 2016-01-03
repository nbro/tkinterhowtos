from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Canvas Bitmap')

canvas = Canvas(root, width=200, height=160, bg='white')

for x, y, g in ((10, 10, 'gray30'), (50, 30, 'gray50'), (90, 50, 'gray70')):
    canvas.create_rectangle(x, y, x + 100, y + 100, fill=g)
    
canvas.pack()

root.mainloop()
