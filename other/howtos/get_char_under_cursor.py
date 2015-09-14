"""
Author: Bryan Oakley

How to find the text widget's index and character under the cursor.
How to find the indices of the selected text range.
"""

import tkinter as tk


class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.status = tk.Text(self, width=60, height=4, bg="#efefef", state="disabled")
        self.status.pack(side="bottom", fill="x")

        self.text = tk.Text(self, wrap="word", width=60, height=10)
        self.text.pack(side="top", fill="both", expand=True)
        self.text.insert("1.0", "Move your cursor around to see what " +
                         "index is under the cursor, and what text is selected.\n")
        self.text.tag_add("sel", "1.10", "1.16")

        # When the cursor moves, show the index of the character under the cursor
        self.text.bind("<Any-Motion>", self.on_mouse_move)

    def on_mouse_move(self, event):
        cursor = "x = %s, y = %s" % (event.x, event.y)
        index = self.text.index("@%s,%s" % (event.x, event.y))

        char = self.text.get(index).strip()
        if not char:
            char = "No character"
        else:
            char = "Character: %s" % char

        index = "Index: %s" % index  # Text widget's index
            
        try:
            sel = "Selection: %s-%s" % (self.text.index("sel.first"), self.text.index("sel.last"))
        except tk.TclError:
            sel = "No selection"

        self.update(cursor, index, char, sel)            

    def update(self, cursor, index, char, sel):
        self.status.configure(state="normal")
        self.status.delete("1.0", "end-1c")
        self.status.insert("end", cursor + "\n" + index + "\n" + char + "\n" + sel)
        self.status.configure(state="disabled")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Text's indices and characters under the cursor")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
