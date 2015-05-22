# simple example of use of a Listbox widget

import tkinter as tk

root = tk.Tk()

# selectmode="extended" => selects ranges of items
listbox = tk.Listbox(root, selectmode="extended")

[listbox.insert("end", "Item " + str(e)) for e in range(10)]
listbox.pack(fill="both")

selector = tk.Button(root, text="Get selected item",
                     command=lambda: print([listbox.get(i) for i in listbox.curselection()]))
selector.pack()

root.mainloop()
