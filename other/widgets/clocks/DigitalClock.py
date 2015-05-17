"""
Based on:

http://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter
"""

import tkinter as tk
import time


class DigitalClock(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.label = tk.Label(self, text="", relief="sunken", border=1,
                              padx=10, pady=10, font=("Arial", 15))
        self.label.pack(expand=True, fill="both")
        self.update_clock()

    # recursive event
    def update_clock(self):

        # get the current local time from the PC
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        
        # calls itself every 1000 milliseconds
        self.after(1000, self.update_clock)


if __name__ == '__main__':
    root = tk.Tk()
    clock = DigitalClock(root)
    clock.pack()
    root.mainloop()
