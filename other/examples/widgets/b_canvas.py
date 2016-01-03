from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('Canvas')
canvas = Canvas(root, width=200, height=160)
canvas.create_oval(10, 10, 100, 100, fill='gray80')
canvas.create_line(40, 40, 150, 115, stipple='@bitmaps/gray3', width=15)
canvas.create_rectangle(205, 10, 300, 105, outline='white', fill='gray50')
canvas.create_bitmap(175, 35, bitmap='questhead')

xy = 45, 45, 135, 140
canvas.create_arc(xy, start=0, extent=270, fill='gray60')
canvas.create_arc(xy, start=270, extent=5, fill='gray70')
canvas.create_arc(xy, start=275, extent=35, fill='gray80')
canvas.create_arc(xy, start=310, extent=49, fill='gray90')

canvas.create_text(160, 125, text='Text', fill='black', font=('verdana', 14))
canvas.pack()

root.mainloop()
