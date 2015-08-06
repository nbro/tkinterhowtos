#!/usr/bin/env python
#================================================================
# fontselector: Test driver for FontSelect
#
# For documentation, see:
#   http://www.nmt.edu/tcc/help/lang/python/examples/fontselect/
#----------------------------------------------------------------

from tkinter import *
import tkinter.font
import fontselect


class Application(Frame):

    """GUI for fontselector

      State/Invariants:
        .fontSelect:  [ self's FontSelect widget ]
    """

    def __init__(self):
        """Constructor for the Application class.
        """
        Frame.__init__(self, None)
        self.buttonFont = tkinter.font.Font(family="Helvetica", size=20)
        self.grid(padx=5, pady=5)
        self.__createWidgets()

    def __createWidgets(self):
        """Lay out the widgets.
        """
        self.fontSelect = fontselect.FontSelect(self,
                                                listCount=10,
                                                observer=self.__callback)
        self.fontSelect.grid(row=0, column=0, padx=5, pady=5)

        self.quitButton = Button(self, text="Quit",
                                 font=self.buttonFont,
                                 command=self.quit)
        self.quitButton.grid(row=1, column=0, columnspan=99,
                             sticky=E + W, ipadx=5, ipady=5)

    def __callback(self, font):
        """Observer for font changes.

          [ sys.stdout  +:=  current font name from self.fontSelect ]
        """
        print(("Change to:", self.fontSelect.getName()))
#================================================================
# Main program
#----------------------------------------------------------------

app = Application()
app.master.title("fontselector")
app.mainloop()
