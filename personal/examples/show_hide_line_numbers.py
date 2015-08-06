"""
Lines numbers were created by Bryan Oakley,
but the fact that you can show and hide them when you want
was added by Nelson Brochado.
"""


import tkinter as tk


class TextLineNumbers(tk.Canvas):
    
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]

            # changed where text is draw: it starts from 4
            self.create_text(4, y, anchor="nw", text=linenum)  
            i = self.textwidget.index("%s+1line" % i)

            
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

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
            }
            ''')
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
