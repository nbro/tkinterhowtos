import string
from tkinter import *


class Navigation:

    def __init__(self, master):

        frame = Frame(master, takefocus=1, highlightthickness=2,
                      highlightcolor='blue')
        Label(frame, text='   ').grid(row=0, column=0, sticky=W)
        Label(frame, text='   ').grid(row=0, column=5, sticky=W)

        for button, col in (('B1', 1), ('B2', 2), ('B3', 3), ('B4', 4)):
            setattr(self, '%s' % button, Button(frame, text=button, highlightthickness=2))
            getattr(self, '%s' % button).grid(padx=10, pady=6, row=0, column=col, sticky=NSEW)

        frame2 = Frame(master, takefocus=1, highlightthickness=2, highlightcolor='green')
        Label(frame2, text='   ').grid(row=0, column=0, sticky=W)
        Label(frame2, text='   ').grid(row=0, column=4, sticky=W)
        
        for button, col, action in (('Disable', 1, self.disable),
                                    ('Enable',  2, self.enable),
                                    ('Focus',   3, self.focus),):
            
            setattr(self, '%s' % button, Button(frame2, text=button, highlightthickness=2, command=action))
            getattr(self, '%s' % button).grid(padx=10, pady=6, row=0, column=col, sticky=NSEW)

        frame3 = Frame(master, takefocus=1, highlightthickness=2, highlightcolor='yellow')
        
        Label(frame3, text='   ').grid(row=0, column=0, sticky=W)
        Label(frame2, text='   ').grid(row=0, column=4, sticky=W)
        
        self.text = Text(frame3, width=20, height=3)
        self.text.insert(END, 'Tabs are valid here')
        self.text.grid(row=0, column=1, columnspan=3)

        frame.pack(fill=X, expand=1)
        frame2.pack(fill=X, expand=1)
        frame3.pack(fill=X, expand=1)

    def disable(self):
        self.B2.configure(state=DISABLED, background='cadetblue')
        self.Focus.configure(state=DISABLED, background='cadetblue')

    def enable(self):
        self.B2.configure(state=NORMAL, background=self.B1.cget('background'))
        self.Focus.configure(
            state=NORMAL, background=self.B1.cget('background'))

    def focus(self):
        self.B3.focus_set()

root = Tk()
root.option_add('*Font', 'Verdana 10 bold')
root.title('Navigation')
root.focusmodel('active')

top = Navigation(root)
quit = Button(root, text='Quit', command=root.destroy)
quit.pack(side='bottom')

root.mainloop()
