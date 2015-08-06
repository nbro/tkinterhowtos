"""
Source: http://effbot.org/zone/tkinter-text-hyperlink_manager.htm

The tkHyperlinkManager module is a simple container for Text widget hyperlinks.
Just create a manager for your text widget, and use the add_action method to register actions.

    text = Text(...)
    hyperlink_manager = HyperlinkManager(text)
    text.insert("insert", "this is a link", hyperlink_manager.add_action(callback))
"""


import tkinter as tk
import webbrowser  # used to display web documents (opening websites...)


class HyperlinkManager:

    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="blue", underline=1)
        self.text.tag_bind("hyper", "<Enter>", self.on_enter)
        self.text.tag_bind("hyper", "<Leave>", self.on_leave)
        self.text.tag_bind("hyper", "<Button-1>", self.on_button_1)
        self.reset()

    def reset(self):
        self.links = {}

    def add_action(self, action):
        """Add an action to the manager.
        Returns tags to use in associated text widget."""
        
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def on_enter(self, event):
        self.text.config(cursor="hand2")

    def on_leave(self, event):
        self.text.config(cursor="")

    def on_button_1(self, event):
        for tag in self.text.tag_names("current"):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return
            

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hyperlink Manager")

    text = tk.Text(root)
    text.pack(expand=1, fill="both")

    # creation of an HyperlinkManager object for "text"
    hyperlink_manager = HyperlinkManager(text)

    def action_1():
        print("click 1")

    text.insert("insert", "This is a ")
    text.insert("insert", "link", hyperlink_manager.add_action(action_1))
    text.insert("insert", ".\n\n")


    def action_2():
        webbrowser.open("https://www.google.com", new=2, autoraise=True)

    text.insert("insert", "Search on ")
    text.insert("insert", "Google", hyperlink_manager.add_action(action_2))
    text.insert("insert", ".\n\n")

    root.mainloop()
