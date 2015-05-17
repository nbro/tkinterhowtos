"""
Similar to this: https://github.com/emcek/pyton/blob/master/ToolTip.py


This is how it looks, shown with one of the new Movable Python dialogs :

Tooltips in Action
To use it, simply create a button (or label or whatever) and call :

    createToolTip(widget, "This is a tooltip")

Another useful thing to do is bind Return to the action of the button.
That way when it is focussed the user can activate it with the return or enter key :

    widget.bind('<Return>', command)

I won't give away quite all my secrets,
but I thought this was nice.
The tooltips are shown when the mouse is over the widget,
and it is remarkably smooth in action.
"""

from tkinter import *


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "12", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
    

if __name__ == '__main__':
    master = Tk()
    btn = Button(master, text='Enter!')
    btn.pack()
    createToolTip(btn, 'This is a tool tip for the button!!')
    master.mainloop()
