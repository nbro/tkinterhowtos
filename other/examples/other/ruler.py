from tkinter import *


class Ruler:

    def __init__(self, master, width='14.8c', height='2.5c'):
        Label(master, text="This canvas widget shows a mock-up of a "
              "ruler.  You can create tab stops by dragging them out "
              "of the well to the right of the ruler.  You can also "
              "drag existing tab stops.  If you drag a tab stop far "
              "enough up or down so that it turns dim, it will be "
              "deleted when you release the mouse button.",
              wraplength="5i", justify=LEFT).pack(side=TOP)
        self.ctl = Frame(master)
        self.ctl.pack(side=BOTTOM, fill=X, padx=2, pady=2)
        Button(self.ctl, text='Quit', command=master.quit).pack()
        self.canvas = Canvas(master, width=width, height=height,
                             relief=FLAT, borderwidth=2)
        self.canvas.pack(side=TOP, fill=X)

        c = self.canvas
        self.grid = '0.25c'
        self.left = c.winfo_fpixels('1c')
        self.right = c.winfo_fpixels('13c')
        self.top = c.winfo_fpixels('1c')
        self.bottom = c.winfo_fpixels('1.5c')
        self.size = c.winfo_fpixels('.2c')
        self.normalStyle = 'black'
        self.activeStyle = 'green'
        self.activeStipple = ''
        self.deleteStyle = 'red'
        self.deleteStipple = 'gray25'

        c.create_line('1c', '0.5c', '1c', '1c', '13c', '1c',
                      '13c', '0.5c', width=1)
        for i in range(12):
            x = i + 1
            c.create_line('%dc' % x, '1c', '%dc' % x, '0.6c', width=1)
            c.create_line('%d.25c' % x, '1c', '%d.25c' % x,
                          '0.8c', width=1)
            c.create_line('%d.5c' % x, '1c', '%d.5c' % x,
                          '0.7c', width=1)
            c.create_line('%d.75c' % x, '1c', '%d.75c' % x,
                          '0.8c', width=1)
            c.create_text('%d.15c' % x, '.75c', text=i, anchor=SW)

            wellBorder = c.create_rectangle('13.2c', '1c', '13.8c',
                                            '0.5c', outline='black',
                                            fill=self.canvas['background'])
            wellTab = self.mkTab(c.winfo_pixels('13.5c'),
                                 c.winfo_pixels('.65c'))
            c.addtag_withtag('well', wellBorder)
            c.addtag_withtag('well', wellTab)

            c.tag_bind('well', '<1>',
                       lambda e, s=self: s.newTab(e.x, e.y))
            c.tag_bind('tab',  '<1>',
                       lambda e, s=self: s.selectTab(e.x, e.y))
            c.bind('<B1-Motion>',
                   lambda e, s=self: s.moveTab(e.x, e.y))
            c.bind('<Any-ButtonRelease-1>', self.releaseTab)

    def mkTab(self, x, y):
        return self.canvas.create_polygon(x, y, x + self.size,
                                          y + self.size, x - self.size, y + self.size)

    def newTab(self, x, y):
        newTab = self.mkTab(x, y)
        self.canvas.addtag_withtag('active', newTab)
        self.canvas.addtag_withtag('tab', newTab)
        self.x = x
        self.y = y
        self.moveTab(x, y)

    def selectTab(self, x, y):
        self.x = self.canvas.canvasx(x, self.grid)
        self.y = self.top + 2
        self.canvas.addtag_withtag('active', CURRENT)
        self.canvas.itemconfig('active', fill=self.activeStyle,
                               stipple=self.activeStipple)
        self.canvas.lift('active')

    def moveTab(self, x, y):
        tags = self.canvas.find_withtag('active')
        if not tags:
            return

        cx = self.canvas.canvasx(x, self.grid)
        cy = self.canvas.canvasx(y)
        if cx < self.left:
            cx = self.left
        if cx > self.right:
            cx = self.right
        if cy >= self.top and cy <= self.bottom:
            cy = self.top + 2
            self.canvas.itemconfig('active', fill=self.activeStyle,
                                   stipple=self.activeStipple)
        else:
            cy = cy - self.size - 2
            self.canvas.itemconfig('active', fill=self.deleteStyle,
                                   stipple=self.deleteStipple)
        self.canvas.move('active', cx - self.x, cy - self.y)
        self.x = cx
        self.y = cy

    def releaseTab(self, event):
        tags = self.canvas.find_withtag('active')
        if not tags:
            return
        if self.y != self.top + 2:
            self.canvas.delete('active')
        else:
            self.canvas.itemconfig('active', fill=self.normalStyle,
                                   stipple=self.activeStipple)
            self.canvas.dtag('active')

if __name__ == '__main__':
    root = Tk()
    root.option_add('*Font', 'Verdana 10')
    root.title('Ruler')
    ruler = Ruler(root)
    root.mainloop()
