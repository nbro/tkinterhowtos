"""
Center a Tk window by directly executing a Tk command.
"""

from tkinter import *


app = Tk()
app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
app.mainloop()
