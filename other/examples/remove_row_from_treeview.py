"""
How to delete a row from a Treeview.
"""

from tkinter import Tk, Button, ttk, Frame, Toplevel, Label, Entry, StringVar
from tkinter import messagebox


class InputDialog:

    def __init__(self, master):
        self.dialog = Toplevel(master)
        self.master = master
        self.dialog.title("Select new job and current money")

        self.job_var = StringVar()
        self.money_var = StringVar()

        self.top = Frame(self.dialog)
        self.job_label = Label(self.top, text="Job")
        self.job_label.pack(side="left")
        self.job_entry = Entry(self.top, textvariable=self.job_var)
        self.job_entry.pack(side="right")
        self.top.pack(side="top", fill="both")

        self.mid = Frame(self.dialog)
        self.money_label = Label(self.mid, text="Money")
        self.money_label.pack(side="left")
        self.money_entry = Entry(self.mid, textvariable=self.money_var)
        self.money_entry.pack(side="right")
        self.mid.pack(side="top", fill="both")

        self.bottom = Frame(self.dialog)
        self.ok_button = Button(self.bottom, text="Confirm", command=self.ok)
        self.ok_button.pack(side="right")
        self.bottom.pack(side="top", fill="both")

    def show(self):
        self.dialog.wait_window(self.dialog)
        return self.ok()

    def ok(self):
        job = self.job_var.get()
        money = self.money_var.get()
        self.dialog.destroy()
        return job, money


class CustomTree(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.top = Frame(self)
        self.delete_button = Button(self.top, text="Delete", command=self.delete)
        self.delete_button.pack(side="left")
        self.edit_button = Button(self.top, text="Edit", command=self.edit)
        self.edit_button.pack(side="left")
        self.top.pack(fill="x")

        self.tree = ttk.Treeview(self)

        self.tree["columns"] = ("one", "two")
        self.tree.column("one", width=100)
        self.tree.column("two", width=100)
        self.tree.heading("one", text="Job")
        self.tree.heading("two", text="Money")

        self.tree.insert("", 0, text="Bill Gates", values=("Unemployed", "Some billions"))

        bob_id = self.tree.insert("", 1, "marley", text="Marley")

        # Sub rows of row with text Marley
        self.tree.insert(bob_id, "end", "ziggy-marley", text="Ziggy Marley", values=("Singer", "Some millions"))
        self.tree.insert(bob_id, "end", "damian-marley", text="Damian Marley", values=("Singer", "Some millions"))
        self.tree.insert(bob_id, "end", "bob-marley", text="Bob Marley", values=("Singer", "Some millions"))

        self.tree.pack(expand=1, fill="both")

    def edit(self):
        job, money = InputDialog(self.master).show()

        try:
            selected_item = self.tree.selection()[0]  # Get selected item
            self.tree.column(selected_item)
            messagebox.showinfo("", str(selected_item))
        except IndexError:
            messagebox.showinfo("No row selected", "No row selected.")

    def delete(self):
        try:
            selected_item = self.tree.selection()[0]  # Get selected item
            self.tree.delete(selected_item)
        except IndexError:
            pass


if __name__ == "__main__":
    root = Tk()
    root.title("Delete a row from a Treeview.")
    CustomTree(root).pack(expand=1, fill="both")
    root.mainloop()
