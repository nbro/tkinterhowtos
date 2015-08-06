"""
Simple example on how to synchronise a Entry and Label widgets.
"""

from tkinter import *


LABEL_DEFAULT_TEXT = "Your name is: "

root = Tk()

prompt = Label(root, text="Enter your name: ")
prompt.pack(side="left")

entry = Entry(root)
entry.pack(side="left")


def on_key_pressing(event, entry, label):
    # print(entry.get(), label.cget("text"))
    if entry.get() != label.cget("text"):
        label.config(text=LABEL_DEFAULT_TEXT + entry.get())

# Associando o evento <Key> com a chamada
# a funcão on_key_pressing
entry.bind("<KeyRelease>", lambda e: on_key_pressing(e, entry, label))

label = Label(root, text=LABEL_DEFAULT_TEXT)
label.pack(side="left")

root.mainloop()
