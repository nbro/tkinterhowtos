# from SO
# center a Tk window by directly executing a tk command
from tkinter import *

app = Tk()
app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
app.mainloop()
