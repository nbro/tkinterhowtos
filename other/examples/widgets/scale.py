from tkinter import *
import string


def setHeight(canvas, heightStr):
    height = int(heightStr)
    height = height + 21
    y2 = height - 30

    if y2 < 21:
        y2 = 21
        
    canvas.coords('poly', 15, 20, 35, 20, 35, y2, 45, y2, 25, height, 5, y2, 15, y2, 15, 20)
    canvas.coords('line', 15, 20, 35, 20, 35, y2, 45, y2, 25, height, 5, y2, 15, y2, 15, 20)

root = Tk()
root.option_readfile('optionDB')
root.title('Scale')

canvas = Canvas(root, width=50, height=50, bd=0, highlightthickness=0)
canvas.create_polygon(0, 0, 1, 1, 2, 2, fill='cadetblue', tags='poly')
canvas.create_line(0, 0, 1, 1, 2, 2, 0, 0, fill='black', tags='line')

scale = Scale(root, orient=VERTICAL, length=284, from_=0, to=250,
              tickinterval=50, command=lambda h, c=canvas: setHeight(c, h))
scale.grid(row=0, column=0, sticky='NE')

canvas.grid(row=0, column=1, sticky='NWSE')

scale.set(100)

root.mainloop()
