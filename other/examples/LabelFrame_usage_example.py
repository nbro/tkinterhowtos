"""Author: Bryan Oakley
Source: http://stackoverflow.com/questions/16613040/table-of-widgets-in-python-with-tkinter?rq=1
"""


import tkinter as tk
import time


class Table(tk.LabelFrame):

    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        data = [
            # Nr. Name  Active
            [1,   "ST", True],
            [2,   "SO", False],
            [3,   "SX", True],
        ]

        self.grid_columnconfigure(1, weight=1)
        tk.Label(self, text="Nr.", anchor="w").grid(row=0, column=0, sticky="ew")
        tk.Label(self, text="Name", anchor="w").grid(row=0, column=1, sticky="ew")
        tk.Label(self, text="Active", anchor="w").grid(row=0, column=2, sticky="ew")
        tk.Label(self, text="Action", anchor="w").grid(row=0, column=3, sticky="ew")

        row = 1
        for (nr, name, active) in data:
            nr_label = tk.Label(self, text=str(nr), anchor="w")
            name_label = tk.Label(self, text=name, anchor="w")
            action_button = tk.Button(self, text="Delete", command=lambda nr=nr: self.delete(nr))
            active_cb = tk.Checkbutton(self, onvalue=True, offvalue=False)
            if active:
                active_cb.select()
            else:
                active_cb.deselect()

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")
            active_cb.grid(row=row, column=2, sticky="ew")
            action_button.grid(row=row, column=3, sticky="ew")

            row += 1

    def delete(self, nr):
        print(("deleting...nr=", nr))


if __name__ == "__main__":
    root = tk.Tk()
    Table(root, text="Hello").pack(side="top", fill="both", expand=True, padx=10, pady=10)
    root.mainloop()
