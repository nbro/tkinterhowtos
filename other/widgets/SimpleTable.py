"""
Source: http://stackoverflow.com/questions/11047803/creating-a-table-look-a-like-tkinter

Author: Bryan Oakley
"""

import tkinter as tk


class SimpleTable(tk.Frame):

    """Simple table created with Label widgets"""

    def __init__(self, parent, rows=5, columns=4, *args, **kwargs):
        # use black background so it "peeks through" to form grid lines
        tk.Frame.__init__(self, parent, bg="black", *args, **kwargs)

        self.widgets = []

        # creating the rows and columns
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="row: %s, col: %s" % (row, column), bd=0, width=15)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)                
            self.widgets.append(current_row)

        # making columns expand
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        self.widgets[row][column].configure(text=value)


class ExampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("SimpleTable demo")
        table = SimpleTable(self)
        table.pack(side="top", fill="x")
        table.set(0, 0, "Hello, World")
        table.set(1, 0, "Hello, Mama!")
        

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
