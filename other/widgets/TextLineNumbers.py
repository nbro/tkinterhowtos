"""
Lines numbers were created by Bryan Oakley,
but the fact that you can show and hide them when you want
was added by Nelson Brochado.
"""


import tkinter as tk


class TextLineNumbers(tk.Canvas):

    """Using a Canvas to display the line numbers precisely.

    If you associate this with a text widget and then call the redraw method,
    it should display the line numbers just fine.

    This works, but has a fatal flaw:
    you have to know when to call redraw.

    You could create a binding that fires on every key press,
    but you also have to fire on mouse buttons,
    and you have to handle the case where a user presses a key
    and uses the auto-repeat function, etc.
    
    The line numbers also need to be redrawn,
    if the window is grown or shrunk or the user scrolls,
    so we fall into a rabbit hole of trying to figure out
    every possible event that could cause the numbers to change.


    There is another solution,
    which is to have the text widget fire an event
    whenever "something changes".

    Unfortunately, the Text widget doesn't have direct support for that.

    However, we can write a little Tcl code
    to intercept changes to the Text widget
    and generate an Event for us.

    The idea is to have a Text widget generate an Event,
    whenever something changes in the Text widget itself.
    You can find this new Text widget below, called CustomText.
    It contains some Tcl code...
    """
    
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text_widget = None

    def attach(self, text_widget):
        """Associates a text widget with this widget"""
        self.text_widget = text_widget

    def redraw(self, *args):
        """Redraws the line numbers for an associated text widget"""
        
        self.delete("all")  # Deletes all items in the Canvas

        # position before the character closest to the coordinate 0,0
        i = self.text_widget.index("@0,0")

        while True :
            
            """A Text widget can tell us exactly
            where a line of text starts and ends
            via the "dlineinfo" method,
            which returns a 5-tuple: (x, y, width, height, offset)
            and receives a character index.
            "dlineinfo" only works if the Text widget is updated,
            to ensure this call "update_idletasks".
            
            This tell us precisely where to draw
            the line numbers on our Canvas.

            "dlineinfo" returns None if a line is not visible,
            which we can use to know when to stop displaying line numbers."""
            
            dline= self.text_widget.dlineinfo(i)

            # breaks the look when a line is not visible
            if dline is None:  
                break

            y = dline[1]  # y coordinate

            linenum = str(i).split(".")[0]
            
            # adding the line number to the Canvas
            self.create_text(3, y, anchor="nw", text=linenum, fill="#207f9f")
            
            i = self.text_widget.index("%s+1line" % i)


class CustomText(tk.Text):

    """Custom Text widget that generates a <<Change>> Event,
    whenever text is inserted or deleted or whenever the view is scrolled.
    
    You should use the CustomText widget instead of the normal one,
    if you want a Text widget with line numbers!"""
    
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # Somce Tcl code...
        self.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Change>> -when tail
                }

                # return the result from the real widget command
                return $result
            } ''')
        
        self.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(self)))


class LinedText(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.settings = self.Settings()
        self.linenumbers = None
        
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
    
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.text.insert("end", "one\ntwo\nthree\n")
        self.text.insert("end", "four\n",("bigfont",))
        self.text.insert("end", "five\n")
        self.text.focus()        
        self.text.pack(side="right", fill="both", expand=True)
        
    def hide(self,event=None):
        if not self.settings.hide_linenumbers:
            self.settings.hide_linenumbers = True
            self.linenumbers.pack_forget()
            self.linenumbers = None

    def show(self,event=None):
        if self.linenumbers is None:
            self.linenumbers = TextLineNumbers(self, width=30)
            self.linenumbers.attach(self.text)
            self.linenumbers.pack(side="left", fill="y")
            self.settings.hide_linenumbers = False

    def _on_change(self, event):
        if self.linenumbers:
            self.linenumbers.redraw()

    class Settings():
        def __init__(self):
            self.hide_linenumbers = True


if __name__ == "__main__":
    root = tk.Tk()

    top_frame = tk.Frame(root)
    text = LinedText(top_frame)
    text.pack(expand=1, fill="both")
    top_frame.pack(side="top", expand=1, fill="both")
    
    bottom_frame = tk.Frame(root)
    button = tk.Button(bottom_frame, text="Hide", command=text.hide)
    button.pack(side="right")
    button = tk.Button(bottom_frame, text="Show", command=text.show)
    button.pack(side="right")
    bottom_frame.pack(side="bottom", fill="x")
    
    root.mainloop()
