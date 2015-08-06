"""fontselect.py: FontSelect, a font selector widget for Tkinter.

  For documentation, see:
    http://www.nmt.edu/tcc/help/lang/python/examples/fontselect/
"""

#================================================================
# Imports
#----------------------------------------------------------------

from tkinter import *
import tkinter.font
import tkinter.dialog
import scrolledlist

#================================================================
# Manifest constants
#----------------------------------------------------------------

LISTBOX_HEIGHT = 15
LISTBOX_WIDTH = 30
SAMPLE_TEXT = "0O 1lI| ABC abc"
DEFAULT_SIZE = 14
DEFAULT_FAMILY = "helvetica"


class FontSelect(Frame):

    """A compound widget for selecting fonts.
      Exports:
        FontSelect ( master, font=None, listCount=None, observer=None ):
          [ (master is a Frame or None) and
            (font is a tkFont.Font or None) and
            (listCount is an integer, defaulting to LISTBOX_HEIGHT) and
            (observer is a function to be called when the font
            changes) ->
              master  :=  master with a new FontSelect widget added
                          but not gridded, with that font, list count,
                          and observer function
              return that widget ]
        .scrollList:    [ a ScrolledList containing the family names ]
        .get():
          [ if a font has been selected ->
              return that font as a tkFont.Font object
            else -> return None ]
        .getName():
          [ if a font has been selected ->
              return a string describing the actual font
            else -> return None ]
        .addObserver ( f ):
          [ self  :=  self with a new observer function added ]

        .regularFont:  [ a tkFont.Font for general purposes ]
        .listFont:
           [ if a font option was passed to the constructor ->
               that option's value
             else -> self.regularFont ]

      Internal widgets:
        .familyPicker:
          [ a FamilyPicker for picking the font family ]
        .controls:
          [ a Controls widget containing other controls ]

      State/Invariants:
        .__listCount:
           [ if a listCount option was passed to the constructor ->
               that option's value
             else -> LISTBOX_HEIGHT ]
        .__observerList:
          [ a list containing all observer callback functions
            for self ]
    """

    def __init__(self, master=None, font=None, listCount=None,
                 observer=None):
        """Constructor for the FontSelect widget.
        """

        #-- 1 --
        # [ master  :=  master with a new Frame widget added
        #   self    :=  that Frame ]
        Frame.__init__(self, master, relief=RIDGE,
                       borderwidth=4)
        #-- 2 --
        self.regularFont = tkinter.font.Font(
            family="new century schoolbook", size="13")
        #-- 3 --
        # [ if font is None ->
        #     self.listFont  :=  self.regularFont
        #   else ->
        #     self.listFont  :=  font ]
        self.listFont = font or self.regularFont

        #-- 4 --
        # [ if listCount is None ->
        #     self.__listCount  :=  LISTBOX_HEIGHT
        #   else ->
        #     self.__listCount  :=  listCount ]
        self.__listCount = listCount or LISTBOX_HEIGHT
        #-- 5 --
        # [ if observer is not None ->
        #     self.__observerList  :=  [ observer ]
        #   else ->
        #     self.__observerList  :=  an empty list ]
        self.__observerList = []
        if observer:
            self.__observerList.append(observer)
        #-- 6 --
        # [ self  :=  self with all widgets and control linkages ]
        self.__createWidgets()

    def __createWidgets(self):
        """Create sub-widgets.

          [ self is a Frame ->
              self  :=  self with all widgets and control linkages ]
        """
        #-- 1 --
        # [ self  :=  self with a new FamilyPicker widget added
        #       and gridded that calls self.__familyHandler when
        #       a family is selected
        #   self.familyPicker  :=  that widget
        #   self.scrollList  :=  the .scrollList attribute of
        #                        that widget ]
        self.familyPicker = FamilyPicker(self, self.__familyHandler)
        self.familyPicker.grid(row=0, column=0, sticky=N)
        self.scrollList = self.familyPicker.scrollList

        #-- 2 --
        # [ self  :=  self with a new Controls widget added and
        #             gridded, that calls self.__controlHandler
        #             when the font changes
        #   self.controls  :=  that widget
        self.controls = Controls(self, self.__controlHandler)
        self.controls.grid(row=0, column=1, sticky=N)

    def __familyHandler(self, newFamily):
        """Handler for change of family name.

          [ newFamily is a string ->
             self.controls  :=  self.controls with its font
                 family set to newFamily ]             
        """
        self.controls.setFamily(newFamily)

    def __controlHandler(self, newFont):
        """Handler for a changed font.

          [ newFont is a tkFont.Font object ->
              call each function in self.__observerList, passing
              newFont to each one ]
        """
        for observer in self.__observerList:
            observer(newFont)

    def get(self):
        """Return the current font.
        """
        return self.controls.getFont()

    def getName(self):
        """Return the current font name.
        """
        return self.controls.getName()

    def addObserver(self, observer):
        """Add another observer callback.
        """
        self.__observerList.append(observer)


class FamilyPicker(Frame):

    """Widget to select a font family.

      Exports:
        FamilyPicker ( fontSelect, observer=None ):
          [ (fontSelect is a FontSelect widget) and
            (observer is a function or None) ->
              fontSelect  :=  fontSelect with a new FamilyPicker
                  widget added but not gridded, with that
                  observer callback if given
              return that FamilyPicker widget ]

      Internal widgets:
        .topLabel:  [ a Label above the family list ]
        .scrollList:
          [ a ScrolledList containing the family names ]
    """

    def __init__(self, fontSelect, observer):
        """Constructor for FamilyPicker
        """
        #-- 1 --
        # [ fontSelect  :=  fontSelect with a new Frame added
        #   self  :=  that Frame ]
        Frame.__init__(self, fontSelect)
        #-- 2 --
        self.fontSelect = fontSelect
        self.observer = observer

        #-- 3 --
        # [ self  :=   self with a new Label widget added
        #              and gridded
        #   self.topLabel  :=  that widget ]
        self.topLabel = Label(self,
                              font=fontSelect.regularFont,
                              text="Click to select font family:")
        self.topLabel.grid(row=0, column=0, sticky=W)

        #-- 4 --
        # [ self  :=  self with a new ScrolledList widget added
        #             and gridded
        #   self.scrollList  :=  that widget ]
        self.scrollList = scrolledlist.ScrolledList(self,
                                                    width=LISTBOX_WIDTH, height=LISTBOX_HEIGHT,
                                                    callback=self.__listboxHandler)
        self.scrollList.grid(row=1, column=0)
        self.scrollList.listbox["font"] = fontSelect.listFont
        #-- 5 --
        # [ self.scrollList  :=  self.scrollList with a list of
        #       the font families from tkFont added ]
        familySet = list(tkinter.font.families())
        familySet.sort()
        for name in familySet:
            self.scrollList.append(name)

    def __listboxHandler(self, lineNo):
        """Handler for selection in the listbox.
        """
        #-- 1 --
        # [ familyName  :=  text from the (lineNo)th line of
        #       self.scrollList ]
        familyName = self.scrollList[lineNo]

        #-- 2 --
        self.observer(familyName)


class Controls(Frame):

    """Frame for all the small widgets in the application.

      Exports:
        Controls ( fontSelect, observer ):
          [ (fontSelect is a FontSelect widget) and
            (observer is a callback function or None) ->
              fontSelect  :=  fontSelect with a new Controls widget
                  added but not gridded, with that observer callback
                  if given
              return that new Controls widget ]
        .setFamily ( familyName ):
          [ familyName is the name of a font family in tkFont ->
              self  :=  self with that font family set ]
        .getName():
          [ return a string describing self's current font ]
        .getFont():
          [ returns self's current font as a tkFont.Font ]

      Internal widgets:

          0
        +--------------+
      0 | .annunciator | Label:  Shows the current font name.
        +--------------+
      1 | .sample      | Text:  Some sample text in the current font.
        +--------------+
      2 | .buttons     | Frame:  Remaining small controls.
        +--------------+
      Internal widgets inside self.buttons are stacked
       sideways.

       Column
       ------
         0    .sizeLabel: Label, 'Size:'
         1    .sizeField: Entry, text size in pixels
         2    .sizeButton: Button, applies .sizeField
         3        (spacer column, absorbs remaining space)
         4    .boldButton: Checkbutton, turns boldface on and off
         5    .italicButton:  Checkbutton, turns italics on and off

      Control variables:
        .__fontName:
          [ string control variable for .annunciator ]
        .__sizeText:
          [ string control variable for .sizeField ]
        .__isBold:
          [ int control variable for .boldButton ]
        .__isItalic:
          [ int control variable for .italicButton ]

      State/Invariants:
        .fontSelect:   [ self's parent, a FontSelect ]
        .__currentFamily:
          [ if a family has been selected ->
              that family's name as a string
            else -> None ]
        .__currentFont:
          [ if a font has been selected ->
              a tkFont.Font representing that font
            else ->
              None ]
        .__observer:   [ as passed to the constructor, read-only ]
    """

    def __init__(self, fontSelect, observer=None):
        """Constructor for the Controls widget.
        """

        #-- 1 --
        # [ fontSelect  :=  fontSelect with a new Frame added
        #   self  :=  that Frame ]
        Frame.__init__(self, fontSelect)

        #-- 2 --
        self.fontSelect = fontSelect
        self.__currentFont = None
        self.__currentFamily = None

        #-- 3 --
        # [ self  :=  self with all widgets added and gridded ]
        self.__createWidgets()
        #-- 4 --
        # [ self  :=  self with DEFAULT_FAMILY as the selected family ]
        self.__observer = None
        self.setFamily(DEFAULT_FAMILY)

        #-- 5 --
        self.__observer = observer

    def __createWidgets(self):
        """Widget layout.
        """
        #-- 1 --
        # [ self  :=  self with a new Label added and gridded
        #             with a string control variable
        #   self.annunciator  :=  that Label
        #   self.__fontName   :=  that control variable ]
        self.__fontName = StringVar()
        self.annunciator = Label(self,
                                 font=self.fontSelect.regularFont,
                                 textvariable=self.__fontName,
                                 text="")
        rowx = 0
        self.annunciator.grid(row=rowx, sticky=W)
        #-- 2 --
        # [ self  :=  self with a new Text widget added and gridded,
        #             displaying SAMPLE_TEXT
        #   self.sample  :=  that widget ]
        self.sample = Text(self,
                           width=20, height=2,
                           font=self.fontSelect.regularFont)
        rowx += 1
        self.sample.grid(row=rowx, sticky=W)
        self.sample.insert(END, SAMPLE_TEXT)
        #-- 3 --
        # [ self  :=  self with a new Frame widget added and gridded
        #   self.buttons  :=  that widget ]
        self.buttons = Frame(self)
        rowx += 1
        self.buttons.grid(row=rowx, sticky=W)
        #-- 4 --
        # [ self  :=  self with .sizeLabel, .sizeField, .sizeButton,
        #       .boldButton, and .italicButton added and gridded ]
        self.__createButtons()

    def __createButtons(self):
        """Create all the widgets and control variables in self.buttons.
        """

        #-- 1 --
        # [ self.buttons  :=  self.buttons with a new Label added and
        #                     gridded
        #   self.sizeLabel  :=  that Label ]
        self.sizeLabel = Label(self.buttons,
                               font=self.fontSelect.regularFont,
                               text="Size:")
        colx = 0
        self.sizeLabel.grid(row=0, column=colx)
        #-- 2 --
        # [ self.buttons  :=  self.buttons with a new Entry added
        #       and gridded, with a string control variable, that
        #       calls self.__setFont on Return or Tab keypresses
        #   self.sizeField  :=  that Entry
        #   self.__sizeText  :=  that control variable ]
        self.__sizeText = StringVar()
        self.__sizeText.set(DEFAULT_SIZE)
        self.sizeField = Entry(self.buttons,
                               font=self.fontSelect.regularFont,
                               width=4,
                               textvariable=self.__sizeText)
        colx += 1
        self.sizeField.grid(row=0, column=colx)

        self.sizeField.bind("<KeyPress-Return>",
                            self.__setFont)
        self.sizeField.bind("<FocusOut>", self.__setFont)

        #-- 3 --
        # [ self.buttons  :=  self.buttons with a new Button added
        #       and gridded, that calls self.__setFont when clicked
        #   self.sizeButton  :=  that Button ]
        self.sizeButton = Button(self.buttons,
                                 text="Set Size",
                                 font=self.fontSelect.regularFont,
                                 command=self.__setFont)
        colx += 1
        self.sizeButton.grid(row=0, column=colx)
        #-- 4 --
        # [ self.buttons  :=  self.buttons with column (colx+1)
        #       made stretchable
        #   colx  +:=  1 ]
        colx += 1
        self.buttons.columnconfigure(colx, pad=10)
        self.spacer = Frame(self.buttons)
        self.spacer.grid(row=0, column=colx)
        #-- 5 --
        # [ self.buttons  :=  self.buttons with a Checkbutton added
        #       and gridded, with an integer control variable
        #   self.boldButton  :=  that Checkbutton
        #   self.__isBold    :=  that control variable ]
        self.__isBold = IntVar()
        self.boldFont = self.fontSelect.regularFont.copy()
        self.boldFont.configure(weight=tkinter.font.BOLD)
        self.boldButton = Checkbutton(self.buttons,
                                      command=self.__setFont,
                                      variable=self.__isBold,
                                      selectcolor="#bbbbbb",
                                      indicatoron=0,
                                      font=self.boldFont,
                                      text="Bold")
        colx += 1
        self.boldButton.grid(row=0, column=colx)

        #-- 6 --
        # [ self.buttons  :=  self.buttons with a Checkbutton added
        #       and gridded, with an integer control variable
        #   self.italicButton  :=  that Checkbutton
        #   self.__isItalic  :=  that control variable ]
        self.__isItalic = IntVar()
        self.italicFont = self.fontSelect.regularFont.copy()
        self.italicFont.configure(slant=tkinter.font.ITALIC)
        self.italicButton = Checkbutton(self.buttons,
                                        command=self.__setFont,
                                        variable=self.__isItalic,
                                        selectcolor="#bbbbbb",
                                        indicatoron=0,
                                        font=self.italicFont,
                                        text="Italic")
        colx += 1
        self.italicButton.grid(row=0, column=colx)

    def __setFont(self, event=None):
        """Handler for size button or size field events.

          [ event is an Event object or None ->
              if self's controls describe a valid font ->
                self  :=  self displaying that new font
                call self's observers with that new font
              else ->
                pop up an error dialog ]
        """
        #-- 1 --
        # [ if the text in self.sizeField is an integer ->
        #     sizeValue  :=  that text as an integer
        #   else ->
        #     pop up a dialog
        #     return ]
        try:
            sizeValue = int(self.__sizeText.get())
        except ValueError:
            d = tkinter.dialog.Dialog(self,
                                      title="Message", bitmap="info",
                                      text="Size must be an integer.",
                                      default=0, strings=("OK",))
            return
        #-- 2 --
        # [ if self.__currentFamily is None ->
        #     pop up a dialog
        #     return
        #   else -> I ]
        if self.__currentFamily is None:
            d = tkinter.dialog.Dialog(self,
                                      title="Message", bitmap="info",
                                      text="No family selected.",
                                      default=0, strings=("OK",))
            return
        #-- 3 --
        if self.__isBold.get():
            weightValue = tkinter.font.BOLD
        else:
            weightValue = tkinter.font.NORMAL
        #-- 4 --
        if self.__isItalic.get():
            slantValue = tkinter.font.ITALIC
        else:
            slantValue = "roman"
        #-- 5 --
        # [ self.__currentFont  :=  a new font with
        #       family=self.__currentFamily, weight=weightValue,
        #       slant=slantValue, and size=sizeValue ]
        self.__currentFont = tkinter.font.Font(family=self.__currentFamily,
                                               size=sizeValue, weight=weightValue, slant=slantValue)
        #-- 6 --
        # [ self.sample  :=  self.sample with font self.__currentFont
        #   self.annunciator  :=  self.annunciator with the actual
        #       name of self.__currentFont ]
        self.sample.configure(font=self.__currentFont)
        self.__fontName.set(self.getName())

        #-- 7 --
        if self.__observer:
            self.__observer(self.__currentFont)

    def setFamily(self, newFamily):
        """Sets self's font family name.
        """
        #-- 1 --
        self.__currentFamily = newFamily

        #-- 2 --
        # [ if self's controls describe a valid font ->
        #     self  :=  self displaying that new font
        #     call self's observers with that new font
        #   else ->
        #     pop up an error dialog ]
        self.__setFont()

    def getName(self):
        """Return a string describing the current font's options.

          [ if self.__currentFont is None ->
              return None
            else ->
              return a string describing the current font's options ]
        """

        #-- 1 --
        if self.__currentFont is None:
            return None

        #-- 2 --
        # [ attrs  :=  a list containing self.__currentFont's
        #       actual family name and actual size (as a string) ]
        attrs = [self.__currentFont.actual("family"),
                 str(self.__currentFont.actual("size"))]

        #-- 3 --
        # [ if self.__currentFont is bold ->
        #     attrs  +:=  "bold"
        #   else -> I ]
        if self.__currentFont.actual("weight") == tkinter.font.BOLD:
            attrs.append("bold")

        #-- 4 --
        # [ if self.__currentFont is italic ->
        #     attrs  +:=  "italic"
        #   else -> I ]
        if self.__currentFont.actual("slant") == tkinter.font.ITALIC:
            attrs.append("italic")
        #-- 5 --
        return " ".join(attrs)
# - - -   C o n t r o l s . g e t F o n t

    def getFont(self):
        """Return the current tkFont.Font instance.
        """
        return self.__currentFont

if __name__ == "__main__":
    root = Tk()
    FontSelect(root).pack()
    root.mainloop()
