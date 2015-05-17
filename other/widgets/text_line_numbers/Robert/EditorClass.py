"""
SOURCE: http://tkinter.unpythonic.net/wiki/A_Text_Widget_with_Line_Numbers

A Text widget with line numbers:

Here is a prototype of a tkinter text widget that displays line numbers and copes well with wrapped lines.

I have taken a lazy way out and update the line numbers using a periodic interrupt.
This saves having to monitor every action on the text widget to see if the line numbers have changed.
The line numbers are displayed in a separate Text widget,
so normal editing operations on the main widget do not have to take account of line numbers.

Features:
 - Line numbers are displayed in a seperate Text widget.
 - Line number display is entirely automatic.
 - Text in the main Text widget can be manipulated normally, without regard to line numbers.
 - Line numbers are displayed correctly for wrapped lines.
  
Drawbacks:
 - The height of each line in the main Text widget must all be the same.
 - The height of the lines in the line number display Text
   widget must be the same as for the main Text widget.
 - There is a slight delay in line numbers catching up with reality.
   This is most noticable when fast scrolling is taking place.
"""

__version__ = 0.2
__date__ = "2009-07-25"
__author__ = "robert@pytrash.co.uk"
__licence__ = "Public Domain"


__changelog__ = (

    ('2009-07-25', '0.2', 'PyTrash',
     """Fixed bugs, improved efficiency, added PanedWindow to demo."""),
    ('2009-07-24', '0.1', 'PyTrash',
     """Initial version."""))


from tkinter import *


class EditorClass:

    UPDATE_PERIOD = 100  # in milliseconds

    editors = []
    update_id = None

    def __init__(self, master):

        self.__class__.editors.append(self)

        self.line_numbers = ''

        # A frame to hold the three components of the widget.
        self.frame = Frame(master, bd=1, relief="sunken")

        # The Text widget holding the line numbers.
        self.lnText = Text(self.frame,width=4, padx=4, highlightthickness=0, takefocus=0,
                           bd=0, bg='#eee', fg='magenta', state='disabled')
        self.lnText.pack(side=LEFT, fill='y')

        # The widgets vertical scrollbar
        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vScrollbar.pack(fill='y', side=RIGHT)
        # The Main Text Widget
        self.text = Text(self.frame, width=30, bd=0, padx=4,
                         highlightthickness=0, undo=True, bg='white')
        self.text.pack(side=LEFT, fill=BOTH, expand=1)

        self.text.config(yscrollcommand=self.vScrollbar.set)
        self.vScrollbar.config(command=self.text.yview)

        if self.__class__.update_id is None:
            self.update_all_line_numbers()

    def get_line_numbers(self):

        x = 0
        line = '0'
        col = ''
        ln = ''

        # assume each line is at least 6 pixels high
        step = 6

        nl = '\n'
        lineMask = '    %s\n'
        indexMask = '@0,%d'

        for i in range(0, self.text.winfo_height(), step):

            ll, cc = self.text.index(indexMask % i).split('.')

            if line == ll:
                if col != cc:
                    col = cc
                    ln += nl
            else:
                line, col = ll, cc
                ln += (lineMask % line)[-5:]

        return ln

    def update_line_numbers(self):
        tt = self.lnText
        ln = self.get_line_numbers()
        if self.line_numbers != ln:
            self.line_numbers = ln
            tt.config(state='normal')
            tt.delete('1.0', END)
            tt.insert('1.0', self.line_numbers)
            tt.config(state='disabled')

    @classmethod
    def update_all_line_numbers(cls):
        if len(cls.editors) < 1:
            cls.update_id = None
            return

        for ed in cls.editors:
            ed.update_line_numbers()

        cls.update_id = ed.text.after(cls.UPDATE_PERIOD, cls.update_all_line_numbers)


def demo(num_of_editors, num_of_lines):

    root = Tk()
    pane = PanedWindow(root, orient="horizontal", opaqueresize=True)
    
    for e in range(num_of_editors):
        ed = EditorClass(root)
        pane.add(ed.frame)

    s = 'line .......................%s'
    s = '\n'.join(s % i for i in range(1, num_of_lines + 1))

    for ed in EditorClass.editors:
        ed.text.insert(END, s)

    pane.pack(fill='both', expand=1)

    root.title("Example: Line numbers for Text widgets")
    root.mainloop()

if __name__ == '__main__':
    demo(2, 5)
    
