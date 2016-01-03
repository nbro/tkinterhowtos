from tkinter import *


class ArrowEditor:

    def __init__(self, master, width=500, height=350):
        Label(master, text="This widget allows you to experiment "
              "with different widths and arrowhead shapes for lines "
              "in canvases.  To change the line width or the shape "
              "of the arrowhead, drag any of the three boxes "
              "attached to the oversized arrow.  The arrows on the "
              "right give examples at normal scale.  The text at "
              "the bottom shows the configuration options as you'd "
              "enter them for a canvas line item.",
              wraplength="5i", justify=LEFT).pack(side=TOP)
        self.control = Frame(master)
        self.control.pack(side=BOTTOM, fill=X, padx=2)
        Button(self.control, text='Quit', command=master.quit).pack()
        self.canvas = Canvas(master, width=width, height=height,
                             relief=SUNKEN, borderwidth=2)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.a = 8       # Setup default values
        self.b = 10
        self.c = 3
        self.width = 2
        self.motionProc = None
        self.x1 = 40
        self.x2 = 350
        self.y = 150
        self.smallTips = (5, 5, 2)
        self.bigLine = 'SkyBlue2'
        self.boxFill = ''
        self.activeFill = 'red'

        self.arrowSetup()          # Draw default arrow

        self.canvas.tag_bind('box', '<Enter>', lambda e, s=self:
                             s.canvas.itemconfig(CURRENT, fill='red'))
        self.canvas.tag_bind('box', '<Leave>', lambda e, s=self:
                             s.canvas.itemconfig(CURRENT, fill=''))
        self.canvas.tag_bind('box1', '<1>', lambda e, s=self:
                             s.motion(s.arrowMove1))
        self.canvas.tag_bind('box2', '<1>', lambda e, s=self:
                             s.motion(s.arrowMove2))
        self.canvas.tag_bind('box3', '<1>', lambda e, s=self:
                             s.motion(s.arrowMove3))
        self.canvas.tag_bind('box', '<B1-Motion>', lambda e,
                             s=self: s.motionProc(e))
        self.canvas.bind('<Any-ButtonRelease-1>', lambda e,
                         s=self: s.arrowSetup())

    def motion(self, func):
        self.motionProc = func

    def arrowMove1(self, event):
        newA = (self.x2 + 5 - int(self.canvas.canvasx(event.x))) / 10
        if newA < 0:
            newA = 0
        if newA > 25:
            newA = 25
        if newA != self.a:
            self.canvas.move("box1", 10 * (self.a - newA), 0)
            self.a = newA

    def arrowMove2(self, event):
        newB = (self.x2 + 5 - int(self.canvas.canvasx(event.x))) / 10
        if newB < 0:
            newB = 0
        if newB > 25:
            newB = 25
        newC = (self.y + 5 - int(self.canvas.canvasx(event.y) +
                                 5 * self.width)) / 10
        if newC < 0:
            newC = 0
        if newC > 20:
            newC = 20
        if newB != self.b or newC != self.c:
            self.canvas.move("box2", 10 * (self.b - newB),
                             10 * (self.c - newC))
            self.b = newB
            self.c = newC

    def arrowMove3(self, event):
        newW = (self.y + 2 - int(self.canvas.canvasx(event.y))) / 5
        if newW < 0:
            newW = 0
        if newW > 20:
            newW = 20
        if newW != self.width:
            self.canvas.move("box3", 0, 5 * (self.width - newW))
            self.width = newW

    def arrowSetup(self):
        tags = self.canvas.gettags(CURRENT)
        cur = None
        if 'box' in tags:
            for tag in tags:
                if len(tag) == 4 and tag[:3] == 'box':
                    cur = tag
                    break

        self.canvas.delete(ALL)
        self.canvas.create_line(self.x1, self.y, self.x2, self.y,
                                width=10 * self.width,
                                arrowshape=(
                                    10 * self.a, 10 * self.b,  10 * self.c),
                                arrow='last', fill=self.bigLine)
        xtip = self.x2 - 10 * self.b
        deltaY = 10 * self.c + 5 * self.width
        self.canvas.create_line(self.x2, self.y, xtip, self.y + deltaY,
                                self.x2 - 10 *
                                self.a, self.y, xtip, self.y - deltaY,
                                self.x2, self.y, width=2, capstyle='round',
                                joinstyle='round')
        self.canvas.create_rectangle(self.x2 - 10 * self.a - 5, self.y - 5,
                                     self.x2 - 10 * self.a + 5, self.y + 5,
                                     fill=self.boxFill, outline='black',
                                     tags=('box1', 'box'))
        self.canvas.create_rectangle(xtip - 5, self.y - deltaY - 5,
                                     xtip + 5, self.y - deltaY + 5,
                                     fill=self.boxFill, outline='black',
                                     tags=('box2', 'box'))
        self.canvas.create_rectangle(self.x1 - 5,
                                     self.y - 5 * self.width - 5, self.x1 + 5,
                                     self.y - 5 * self.width + 5,  fill=self.boxFill,
                                     outline='black', tags=('box3', 'box'))
        if cur:
            self.canvas.itemconfig(cur, fill=self.activeFill)

        self.canvas.create_line(self.x2 + 50, 0, self.x2 + 50,
                                1000, width=2)

        tmp = self.x2 + 100
        self.canvas.create_line(tmp, self.y - 125, tmp, self.y - 75,
                                width=self.width, arrow='both',
                                arrowshape=(self.a, self.b, self.c))
        self.canvas.create_line(tmp - 25, self.y, tmp + 25, self.y,
                                width=self.width, arrow='both',
                                arrowshape=(self.a, self.b, self.c))
        self.canvas.create_line(tmp - 25, self.y + 75, tmp + 25, self.y + 125,
                                width=self.width, arrow='both',
                                arrowshape=(self.a, self.b, self.c))

        tmp = self.x2 + 10
        self.canvas.create_line(tmp, self.y - 5 * self.width, tmp,
                                self.y - deltaY, arrow='both', arrowshape=self.smallTips)
        self.canvas.create_text(self.x2 + 15, self.y - deltaY + 5 * self.c,
                                text=self.c, anchor=W)
        tmp = self.x1 - 10
        self.canvas.create_line(tmp, self.y - 5 * self.width, tmp,
                                self.y + 5 * self.width, arrow='both',
                                arrowshape=self.smallTips)
        self.canvas.create_text(self.x1 - 15, self.y,
                                text=self.width, anchor=E)
        tmp = self.y + 5 * self.width + 10 * self.c + 10
        self.canvas.create_line(self.x2 - 10 * self.a, tmp, self.x2, tmp,
                                arrow='both', arrowshape=self.smallTips)
        self.canvas.create_text(self.x2 - 5 * self.a, tmp + 5,
                                text=self.a, anchor=N)
        tmp = tmp + 25
        self.canvas.create_line(self.x2 - 10 * self.b, tmp, self.x2, tmp,
                                arrow='both', arrowshape=self.smallTips)
        self.canvas.create_text(self.x2 - 5 * self.b, tmp + 5,
                                text=self.b, anchor=N)

        self.canvas.create_text(self.x1, 310, text="width=%d" %
                                self.width, anchor=W, font=('Verdana', 18))
        self.canvas.create_text(self.x1, 330,
                                text="arrowshape=(%d,%d,%d)" %
                                (self.a, self.b, self.c),
                                anchor=W, font=('Verdana', 18))

if __name__ == '__main__':
    root = Tk()
    root.option_add('*Font', 'Verdana 10')
    root.title('Arrow Editor')
    arrow = ArrowEditor(root)
    root.mainloop()
