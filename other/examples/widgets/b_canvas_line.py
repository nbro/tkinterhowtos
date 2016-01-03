from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Canvas Line')
canvas = Canvas(root, width=200, height=160, bg='white')
for y, w in ((150, 15), (134, 10), (122, 5), (115, 3), (110, 1), ):
    canvas.create_line(10, y, 190, y, width=w)

canvas.create_line(10, 100, 40, 95, 60, 98, 70, 100, 80, 94, 120, 102, 130, 100, 190, 100,
                   width=6)
canvas.create_line(10, 80, 40, 75, 60, 78, 80, 80, 90, 70, 110, 82, 130, 80, 190, 80,
                   width=3)
canvas.create_line(10, 50, 40, 45, 60, 48, 80, 50, 90, 40, 110, 52, 130, 50, 190, 50,
                   smooth=1)
canvas.pack()
root.mainloop()
