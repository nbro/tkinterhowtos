from tkinter import *


class TestMenu:

    def __init__(self, master):
        self.master = master
        self.menubar = Menu(self.master)

        self.cmdmenu = Menu(self.menubar)
        self.cmdmenu.add_command(label="Undo")
        self.cmdmenu.entryconfig(1, state=DISABLED)
        self.cmdmenu.add_command(label='New...', underline=0)
        self.cmdmenu.add_command(label='Open...', underline=0)
        self.cmdmenu.add_command(label='Wild Font', underline=0,
                                 font=('Tempus Sans ITC', 14))
        self.cmdmenu.add_command(bitmap="@bitmaps/RotateLeft")
        self.cmdmenu.add('separator')
        self.cmdmenu.add_command(label='Quit', underline=0,
                                 background='white', activebackground='green',
                                 command=self.master.quit)

        self.casmenu = Menu(self.menubar)
        self.casmenu.choices = Menu(self.casmenu)
        self.casmenu.choices.wierdones = Menu(self.casmenu.choices)
        self.casmenu.choices.wierdones.add_command(label='Stockbroker')
        self.casmenu.choices.wierdones.add_command(label='Quantity Surveyor')
        self.casmenu.choices.wierdones.add_command(label='Church Warden')
        self.casmenu.choices.wierdones.add_command(label='BRM')

        self.casmenu.choices.add_command(label='Wooden Leg')
        self.casmenu.choices.add_command(label='Hire Purchase')
        self.casmenu.choices.add_command(label='Dead Crab')
        self.casmenu.choices.add_command(label='Tree Surgeon')
        self.casmenu.choices.add_command(label='Filing Cabinet')
        self.casmenu.choices.add_command(label='Goldfish')
        self.casmenu.choices.add_cascade(label='Is it a...',
                                         menu=self.casmenu.choices.wierdones)

        self.casmenu.add_cascade(label='Scripts',
                                 menu=self.casmenu.choices)

        self.chkmenu = Menu(self.menubar)
        self.chkmenu.add_checkbutton(label='Doug')
        self.chkmenu.add_checkbutton(label='Dinsdale')
        self.chkmenu.add_checkbutton(label="Stig O'Tracy")
        self.chkmenu.add_checkbutton(label='Vince')
        self.chkmenu.add_checkbutton(label='Gloria Pules')
        self.chkmenu.invoke(self.chkmenu.index('Dinsdale'))

        self.radmenu = Menu(self.menubar)
        self.radmenu.add_radiobutton(label='metonymy')
        self.radmenu.add_radiobutton(label='zeugmatists')
        self.radmenu.add_radiobutton(label='synechdotists')
        self.radmenu.add_radiobutton(label='axiomists')
        self.radmenu.add_radiobutton(label='anagogists')
        self.radmenu.add_radiobutton(label='catachresis')
        self.radmenu.add_radiobutton(label='periphrastic')
        self.radmenu.add_radiobutton(label='litotes')
        self.radmenu.add_radiobutton(label='circumlocutors')

        self.unused = Menu(self.menubar)

        self.menubar.add_cascade(label="Button Command", menu=self.cmdmenu)
        self.menubar.add_cascade(label="Cascade Menu", menu=self.casmenu)
        self.menubar.add_cascade(label="Checkbutton Menu", menu=self.chkmenu)
        self.menubar.add_cascade(label="Radiobutton Menu", menu=self.radmenu)
        self.menubar.add_cascade(label="Disabled Menu", menu=self.unused)

        self.menubar.entryconfig(4, state=DISABLED)
        self.top = Toplevel(menu=self.menubar, width=500, relief=RAISED,
                            borderwidth=2)


def main():
    root = Tk()
    root.withdraw()
    app = TestMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
