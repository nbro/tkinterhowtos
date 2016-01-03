from tkinter import *


def new_file():
    print("Open new file")


def open_file():
    print("Open existing file")


def stub_action():
    print("Menu select")


def makeCommandMenu():
    CmdBtn = Menubutton(mBar, text='Button Commands', underline=0)
    CmdBtn.pack(side=LEFT, padx="2m")
    CmdBtn.menu = Menu(CmdBtn)

    CmdBtn.menu.add_command(label="Undo")
    CmdBtn.menu.entryconfig(0, state=DISABLED)

    CmdBtn.menu.add_command(label='New...', underline=0, command=new_file)
    CmdBtn.menu.add_command(label='Open...', underline=0, command=open_file)
    CmdBtn.menu.add_command(label='Wild Font', underline=0,
                            font=('Tempus Sans ITC', 14), command=stub_action)
    CmdBtn.menu.add_command(bitmap="@bitmaps/RotateLeft")
    CmdBtn.menu.add('separator')
    CmdBtn.menu.add_command(label='Quit', underline=0,
                            background='white', activebackground='green',
                            command=CmdBtn.quit)

    CmdBtn['menu'] = CmdBtn.menu
    return CmdBtn


def makeCascadeMenu():
    CasBtn = Menubutton(mBar, text='Cascading Menus', underline=0)
    CasBtn.pack(side=LEFT, padx="2m")
    CasBtn.menu = Menu(CasBtn)
    CasBtn.menu.choices = Menu(CasBtn.menu)
    CasBtn.menu.choices.wierdones = Menu(CasBtn.menu.choices)

    CasBtn.menu.choices.wierdones.add_command(label='Stockbroker')
    CasBtn.menu.choices.wierdones.add_command(label='Quantity Surveyor')
    CasBtn.menu.choices.wierdones.add_command(label='Church Warden')
    CasBtn.menu.choices.wierdones.add_command(label='BRM')

    CasBtn.menu.choices.add_command(label='Wooden Leg')
    CasBtn.menu.choices.add_command(label='Hire Purchase')
    CasBtn.menu.choices.add_command(label='Dead Crab')
    CasBtn.menu.choices.add_command(label='Tree Surgeon')
    CasBtn.menu.choices.add_command(label='Filing Cabinet')
    CasBtn.menu.choices.add_command(label='Goldfish')
    CasBtn.menu.choices.add_cascade(label='Is it a...',
                                    menu=CasBtn.menu.choices.wierdones)

    CasBtn.menu.add_cascade(label='Scipts', menu=CasBtn.menu.choices)
    CasBtn['menu'] = CasBtn.menu
    return CasBtn


def makeCheckbuttonMenu():
    ChkBtn = Menubutton(mBar, text='Checkbutton Menus', underline=0)
    ChkBtn.pack(side=LEFT, padx='2m')
    ChkBtn.menu = Menu(ChkBtn)

    ChkBtn.menu.add_checkbutton(label='Doug')
    ChkBtn.menu.add_checkbutton(label='Dinsdale')
    ChkBtn.menu.add_checkbutton(label="Stig O'Tracy")
    ChkBtn.menu.add_checkbutton(label='Vince')
    ChkBtn.menu.add_checkbutton(label='Gloria Pules')
    ChkBtn.menu.invoke(ChkBtn.menu.index('Dinsdale'))

    ChkBtn['menu'] = ChkBtn.menu
    return ChkBtn


def makeRadiobuttonMenu():
    RadBtn = Menubutton(mBar, text='Radiobutton Menus', underline=0)
    RadBtn.pack(side=LEFT, padx='2m')
    RadBtn.menu = Menu(RadBtn)

    RadBtn.menu.add_radiobutton(label='metonymy')
    RadBtn.menu.add_radiobutton(label='zeugmatists')
    RadBtn.menu.add_radiobutton(label='synechdotists')
    RadBtn.menu.add_radiobutton(label='axiomists')
    RadBtn.menu.add_radiobutton(label='anagogists')
    RadBtn.menu.add_radiobutton(label='catachresis')
    RadBtn.menu.add_radiobutton(label='periphrastic')
    RadBtn.menu.add_radiobutton(label='litotes')
    RadBtn.menu.add_radiobutton(label='circumlocutors')

    RadBtn['menu'] = RadBtn.menu
    return RadBtn


def makeDisabledMenu():
    Dummy_button = Menubutton(mBar, text='Disabled Menu', underline=0)
    Dummy_button.pack(side=LEFT, padx='2m')
    Dummy_button["state"] = DISABLED
    return Dummy_button

root = Tk()
mBar = Frame(root, relief=RAISED, borderwidth=2)
mBar.pack(fill=X)

CmdBtn = makeCommandMenu()
CasBtn = makeCascadeMenu()
ChkBtn = makeCheckbuttonMenu()
RadBtn = makeRadiobuttonMenu()
NoMenu = makeDisabledMenu()

mBar.tk_menuBar(CmdBtn, CasBtn, ChkBtn, RadBtn, NoMenu)

root.title('Menus')
root.mainloop()
