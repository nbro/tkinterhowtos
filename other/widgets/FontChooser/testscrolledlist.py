#!/usr/bin/env python
#================================================================
# scrolledlisttest: Test driver for ScrolledList
#
# For documentation, see:
#   http://www.nmt.edu/tcc/help/lang/python/examples/scrolledlist/
#----------------------------------------------------------------

from tkinter import *
import scrolledlist


class Application(Frame):

    """GUI for scrolledlisttest
    """

    def __init__(self):
        """Constructor for the Application class.
        """
        Frame.__init__(self, None)
        self.grid()
        self.__createWidgets()
        self.__tests()

    def __createWidgets(self):
        """Lay out the widgets.
        """
        self.sbox = scrolledlist.ScrolledList(self,
                                              width=20, height=10, hscroll=1,
                                              callback=self.__pickHandler)
        self.sbox.grid(row=0, column=0)

        self.quitButton = Button(self, text="Quit",
                                 command=self.quit)
        self.quitButton.grid(row=1, column=0, columnspan=99,
                             sticky=E + W, ipadx=5, ipady=5)

    def __pickHandler(self, linex):
        """Handler for user clicks on lines in the listbox.
        """
        print("Click on line %d, '%s'" % (linex, self.sbox[linex]))

    def __tests(self):
        """Initial testing of the ScrolledList widget.
        """
        print("Initial size is", self.sbox.count())
        print("Add alpaca, buffalo, eagle:")
        self.sbox.append("alpaca")
        self.sbox.append("buffalo")
        self.sbox.append("eagle")
        print("Size is now", self.sbox.count())
        print("Clear listbox:")
        self.sbox.clear()
        print("Size is now", self.sbox.count())
        print("Add alpaca, buffalo, eagle:")
        self.sbox.append("alpaca")
        self.sbox.append("buffalo")
        self.sbox.append("eagle")
        print("Insert cachalot")
        self.sbox.insert(2, "cachalot")
        print("Size is now", self.sbox.count())
        print("Delete buffalo:")
        self.sbox.delete(1)
        print("Size is now", self.sbox.count())
        print("Insert bunches o stuff")
        self.sbox.append("finch")
        self.sbox.append("goshawk")
        self.sbox.append("harrier")
        self.sbox.append("indigobird")
        self.sbox.append("jabiru")
        self.sbox.append("kingfisher")
        self.sbox.append("Middendorff's grasshopper-warbler")
        self.sbox.append("merlin")
        self.sbox.append("northern flicker")
        self.sbox.append("ovenbird")
        self.sbox.append("parula")
        print("Size is now", self.sbox.count())
#================================================================
# Main program
#----------------------------------------------------------------

app = Application()
app.master.title("scrolledlisttest")
app.mainloop()
