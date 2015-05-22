import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def show_info():
    messagebox.showinfo("More info", "First column represents the subject" \
                        " and the second represents its corresponding " \
                        "current number of tagged questions on Stack Overflow.")

root = tk.Tk()

tree = ttk.Treeview(root, columns=("Tags"), height=6)

subjects = {"Tkinter": "8,013",
            "Python": "425,865",
            "C++": "369,851",
            "Java": "858,459"}

for subject in subjects.keys():
    tree.insert("", "end", text=subject, values=(subjects[subject]))

tree.column("Tags", anchor="e")    
tree.pack(fill="both", expand=True)

informer = tk.Button(root, text="More info", command=show_info)
informer.pack(side="bottom")


root.mainloop()
